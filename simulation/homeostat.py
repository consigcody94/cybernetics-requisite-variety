#!/usr/bin/env python3
"""
homeostat.py -- a minimal model of Ashby's Homeostat and ULTRASTABILITY.

Ashby's Homeostat (Design for a Brain, 1952/1960) was a machine of four coupled
units.  Each unit's output is driven by a weighted sum of the others' outputs.
Each output is an *essential variable* that must stay inside a survival band.
When a unit's essential variable leaves the band, a stepping switch (the
"uniselector") re-randomizes that unit's input weights.  The machine therefore
searches, by trial, over the space of internal wirings until it lands on one
that is dynamically stable -- and then it stays there.  Ashby called this
ultrastability: not merely stability, but the capacity to *find* a stable
configuration after any disturbance that destabilizes the current one.

This model.  The units are a vector x in R^N with linear coupling
        x(t+1) = A x(t),        clamped to the physical range [-C, C].
A random coupling matrix A is stable iff its spectral radius rho(A) < 1, in
which case x decays to 0 and every essential variable settles inside the band.
An unstable A drives x to the rails and out of the survival band, tripping the
uniselector, which installs a fresh random A.  A wiring that has NOT brought the
system back inside the band and held it there within a patience window is judged
non-viable and re-selected.  Because a fresh wiring is viable with some fixed
probability p, the number of re-selections is geometric with mean ~ 1/p -- the
system reliably restabilizes, and does so faster the higher p is.

Simplification worth flagging: the real Homeostat re-selects each out-of-band
unit's weights independently; here every trip redraws the whole matrix.  This
keeps the search statistics clean (an independent Bernoulli(p) trial per trip)
while preserving the essential phenomenon: an ultrastable system that adapts its
own parameters to survive.

Standard library only.  Reproducible via --seed.
"""

from __future__ import annotations

import argparse
import random
from statistics import mean, median


# --------------------------------------------------------------------------
# Tiny linear-algebra helpers (no numpy).
# --------------------------------------------------------------------------
def matvec(a: list[list[float]], x: list[float]) -> list[float]:
    return [sum(a[i][j] * x[j] for j in range(len(x))) for i in range(len(a))]


def random_matrix(n: int, g: float, rng: random.Random) -> list[list[float]]:
    return [[rng.uniform(-g, g) for _ in range(n)] for _ in range(n)]


def clamp_vec(x, c):
    return [max(-c, min(c, v)) for v in x]


# --------------------------------------------------------------------------
# The homeostat mechanism.
# --------------------------------------------------------------------------
def try_wiring(x, a, n, theta, clamp, hold, patience):
    """Run wiring `a` from state x for up to `patience` steps.  Success = every
    essential variable inside +/- theta for `hold` consecutive steps.  Returns
    (settled_ok, steps_used, final_x)."""
    settled = 0
    for step in range(1, patience + 1):
        x = clamp_vec(matvec(a, x), clamp)
        if all(abs(v) <= theta for v in x):
            settled += 1
            if settled >= hold:
                return True, step, x
        else:
            settled = 0
    return False, patience, x


def restabilize(x, a, n, theta, clamp, g, hold, patience, max_trips, rng):
    """Test the current wiring first; if it cannot hold the essential variables
    in band, trip the uniselector and install fresh wirings until one does.
    Returns (total_steps, reselections, viable_matrix)."""
    total_steps = 0
    reselections = 0
    while reselections <= max_trips:
        ok, used, x = try_wiring(x, a, n, theta, clamp, hold, patience)
        total_steps += used
        if ok:
            return total_steps, reselections, a
        a = random_matrix(n, g, rng)   # uniselector trip
        reselections += 1
    return total_steps, reselections, a


def is_viable(n, theta, clamp, g, hold, patience, rng):
    """Operational stability test: does a fresh random wiring pull the system
    back into the band (and hold it) from a rail-edge start?"""
    a = random_matrix(n, g, rng)
    x = [clamp * rng.choice((-1, 1)) for _ in range(n)]
    ok, _, _ = try_wiring(x, a, n, theta, clamp, hold, patience)
    return ok


def kick(n, theta, clamp, rng):
    """A step-change disturbance that pushes the state outside the band."""
    return [rng.uniform(theta, clamp) * rng.choice((-1, 1)) for _ in range(n)]


def draw_nonviable_wiring(n, theta, clamp, g, hold, patience, rng):
    """A wiring under which the system is currently unstable -- the regime a big
    disturbance leaves the machine in.  Cold-start searches begin here."""
    while True:
        a = random_matrix(n, g, rng)
        x = [clamp * rng.choice((-1, 1)) for _ in range(n)]
        ok, _, _ = try_wiring(x, a, n, theta, clamp, hold, patience)
        if not ok:
            return a


def ascii_hist(values, buckets):
    counts = {}
    for v in values:
        counts[v] = counts.get(v, 0) + 1
    top = max((counts.get(k, 0) for k in buckets), default=1) or 1
    lines = []
    for k in buckets:
        c = counts.get(k, 0)
        bar = "#" * int(round((c / top) * 40))
        lines.append(f"    {k:>3} | {bar} {c}")
    return "\n".join(lines)


# --------------------------------------------------------------------------
# Driver.
# --------------------------------------------------------------------------
def run(seed: int, n: int, trials: int) -> None:
    rng = random.Random(seed)
    g = 1.05          # coupling scale: tuned so viable wirings are a minority
    theta = 1.0       # essential-variable survival band: |x_i| <= theta
    clamp = 3.0       # physical range of each needle
    hold = 12         # consecutive in-band steps required to declare "settled"
    patience = 45     # steps a wiring gets to prove itself before re-selection
    max_trips = 200

    print("=" * 74)
    print("Ashby's Homeostat -- ultrastability by parameter search")
    print("=" * 74)
    print(f"units N = {n}   coupling scale g = {g}   band |x_i| <= {theta}   seed = {seed}")
    print()

    # ---- estimate P(a fresh wiring is viable) ----------------------------
    probe = 3000
    p = sum(is_viable(n, theta, clamp, g, hold, patience, rng) for _ in range(probe)) / probe
    print(f"P(fresh wiring viable)  ~ {p:.3f}")
    if p > 0:
        print(f"predicted re-selections per disturbance ~ 1/p = {1/p:.2f} (geometric search)")
    print()

    # ---- cold-start restabilization statistics ---------------------------
    steps_list, resel_list = [], []
    for _ in range(trials):
        a = draw_nonviable_wiring(n, theta, clamp, g, hold, patience, rng)
        x = kick(n, theta, clamp, rng)
        steps, resel, _ = restabilize(x, a, n, theta, clamp, g, hold, patience, max_trips, rng)
        steps_list.append(steps)
        resel_list.append(resel)

    print(f"Cold-start restabilization over {trials} disturbances "
          "(each starting in an unstable regime):")
    print(f"  re-selections : mean {mean(resel_list):.2f}  median {median(resel_list):.0f}"
          f"  max {max(resel_list)}")
    print(f"  steps-to-settle: mean {mean(steps_list):.1f}  median {median(steps_list):.0f}"
          f"  max {max(steps_list)}")
    print(f"  restabilized  : {sum(1 for r in resel_list if r <= max_trips)}/{trials}"
          " (all disturbances absorbed)")
    print()
    print("  distribution of re-selections (uniselector trips) until viable:")
    print(ascii_hist(resel_list, buckets=list(range(0, min(16, max(resel_list) + 1)))))
    print()

    # ---- ultrastability: once wired viable, kicks need no fresh search ----
    a0 = draw_nonviable_wiring(n, theta, clamp, g, hold, patience, rng)
    _, _, a_stable = restabilize(kick(n, theta, clamp, rng), a0, n, theta, clamp,
                                 g, hold, patience, max_trips, rng)
    follow_resel, follow_steps = [], []
    for _ in range(25):
        x = kick(n, theta, clamp, rng)   # same class of shock, within the rails
        steps, resel, a_stable = restabilize(
            x, a_stable, n, theta, clamp, g, hold, patience, max_trips, rng
        )
        follow_resel.append(resel)
        follow_steps.append(steps)

    print("Ultrastability check -- after a viable wiring is found, apply 25 more kicks:")
    print(f"  re-selections needed: mean {mean(follow_resel):.2f}  max {max(follow_resel)}")
    print(f"  steps-to-settle     : mean {mean(follow_steps):.1f}  max {max(follow_steps)}")
    print()
    print("Interpretation: the machine has no model of the disturbances and no")
    print("designer in the loop. Knocked into an unstable regime it re-selects its")
    print("own wiring -- roughly 1/p trials -- until the dynamics are stable, then")
    print("absorbs further shocks of the same class with zero search. That second-")
    print("order stability -- stability of the conditions for stability -- is Ashby's")
    print("ultrastability: requisite variety supplied by generate-and-test, not design.")


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--seed", type=int, default=1, help="PRNG seed (default 1)")
    p.add_argument("--units", type=int, default=4, help="number of coupled units N (default 4)")
    p.add_argument("--trials", type=int, default=400,
                   help="cold-start disturbances to sample (default 400)")
    args = p.parse_args()
    run(seed=args.seed, n=args.units, trials=args.trials)


if __name__ == "__main__":
    main()
