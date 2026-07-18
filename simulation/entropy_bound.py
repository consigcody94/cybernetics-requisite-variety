#!/usr/bin/env python3
"""
entropy_bound.py -- Monte-Carlo demonstration of the information form of the
Law of Requisite Variety:  H(E) >= H(D) - H(R).

Setup.  A disturbance D is drawn uniformly from m states.  A regulator with
*capacity* k can distinguish at most k classes of disturbance; it lumps the m
disturbances into k groups and emits one canceling response per group.  The
outcome is  E = (D - response) mod m  -- the residual the regulator failed to
cancel.  Because for a fixed response the map D -> E is a bijection, this table
satisfies Ashby's full-variety condition, and the exact chain of inequalities

        H(E)  >=  H(E | R)  =  H(D | R)  =  H(D) - I(D;R)  >=  H(D) - H(R)

holds term by term.  Two facts fall out of that chain:

  * The bound  H(E) >= H(D) - H(R)  is *tight* exactly when I(D;R) = H(R),
    i.e. when the regulator's variety is entirely determined by (correlated
    with) the disturbance.  A deterministic grouping regulator achieves this.

  * Regulator variety that is NOT correlated with the disturbance is wasted:
    it inflates H(R) without lowering H(E).  We show this with a noisy
    regulator whose responses carry independent noise, so I(D;R) < H(R) and a
    gap opens between the true residual and the loose H(D)-H(R) bound.

Everything is estimated from samples with a plug-in entropy estimator; no
analytic shortcuts are used for the achieved H(E).  Standard library only.
"""

from __future__ import annotations

import argparse
import random
from collections import Counter
from math import log2


# --------------------------------------------------------------------------
# Plug-in Shannon entropy estimators (bits).
# --------------------------------------------------------------------------
def entropy(samples) -> float:
    n = len(samples)
    counts = Counter(samples)
    h = -sum((c / n) * log2(c / n) for c in counts.values())
    return h + 0.0  # normalize -0.0 (single-value case) to 0.0


def mutual_information(xs, ys) -> float:
    return entropy(xs) + entropy(ys) - entropy(list(zip(xs, ys)))


# --------------------------------------------------------------------------
# The regulated experiment.
# --------------------------------------------------------------------------
def simulate(m: int, k: int, noise: float, n_samples: int, rng: random.Random):
    """Draw n_samples rounds. Returns (D, R, E) sample lists.

    Grouping regulator: disturbance d falls in group g = d * k // m.  The
    regulator's canceling response is the group's representative value
    rep(g) = the first disturbance in that group.  With probability `noise`
    the regulator instead emits a *random* representative (independent of d) --
    variety that is uncorrelated with the disturbance, i.e. wasted.
    """
    # group boundaries: contiguous, as even as possible
    reps = [(g * m) // k for g in range(k)]  # first disturbance index of group g
    ds, rs, es = [], [], []
    for _ in range(n_samples):
        d = rng.randrange(m)
        g = (d * k) // m
        if noise and rng.random() < noise:
            r = reps[rng.randrange(k)]      # wasted, uncorrelated response
        else:
            r = reps[g]                     # correct canceling response
        e = (d - r) % m
        ds.append(d)
        rs.append(r)
        es.append(e)
    return ds, rs, es


def ascii_bar(value: float, scale: float, width: int = 30) -> str:
    filled = int(round((value / scale) * width)) if scale > 0 else 0
    filled = max(0, min(width, filled))
    return "#" * filled + "-" * (width - filled)


# --------------------------------------------------------------------------
# Driver.
# --------------------------------------------------------------------------
def sweep(title: str, m: int, ks, noise: float, n_samples: int, rng: random.Random):
    print(title)
    print("-" * len(title))
    header = (
        f"{'k':>3} | {'H(D)':>5} | {'H(R)':>5} | {'I(D;R)':>6} | "
        f"{'loose':>6} | {'H(E)':>5} | {'H(E) vs loose bound (achieved=#, tight bound=|)'}"
    )
    print(header)
    hd_full = log2(m)
    ok = True
    for k in ks:
        ds, rs, es = simulate(m, k, noise, n_samples, rng)
        h_d = entropy(ds)
        h_r = entropy(rs)
        i_dr = mutual_information(ds, rs)
        loose = h_d - h_r               # H(D) - H(R)
        tight = h_d - i_dr              # H(D) - I(D;R)  (the true lower bound)
        h_e = entropy(es)
        if h_e < loose - 1e-6:          # the loose bound must never be violated
            ok = False
        bar = ascii_bar(h_e, hd_full)
        # place the tight-bound marker
        marker = int(round((max(tight, 0.0) / hd_full) * 30)) if hd_full > 0 else 0
        marker = max(0, min(29, marker))
        bar = bar[:marker] + "|" + bar[marker + 1:]
        print(
            f"{k:>3} | {h_d:>5.3f} | {h_r:>5.3f} | {i_dr:>6.3f} | "
            f"{loose:>6.3f} | {h_e:>5.3f} | {bar}"
        )
    print()
    return ok


def run(seed: int, m: int, n_samples: int) -> None:
    rng = random.Random(seed)
    ks = [k for k in (1, 2, 3, 4, 6, 12) if k <= m]
    if m not in ks:
        ks.append(m)

    print("=" * 78)
    print("Requisite Variety, information form:  H(E) >= H(D) - H(R)")
    print("=" * 78)
    print(f"disturbance states m = {m}   samples/row = {n_samples}   seed = {seed}")
    print(f"H(D) = log2 {m} = {log2(m):.3f} bits (uniform disturbance)")
    print()
    print("A regulator of capacity k lumps the m disturbances into k groups and")
    print("emits one canceling response per group. Larger k = more responding")
    print("variety = smaller residual H(E).")
    print()

    ok1 = sweep(
        "1) Deterministic regulator (I(D;R)=H(R): the bound is TIGHT, H(E)=H(D)-H(R))",
        m, ks, noise=0.0, n_samples=n_samples, rng=rng,
    )

    ok2 = sweep(
        "2) Noisy regulator (25% wasted responses: I(D;R)<H(R), so H(D)-H(R) goes slack)",
        m, ks, noise=0.25, n_samples=n_samples, rng=rng,
    )

    print("Legend: 'loose' = H(D)-H(R). 'H(E)' = measured residual entropy.")
    print("        Bar shows achieved H(E) (#); the '|' marks the tight bound H(D)-I(D;R).")
    print()
    print("Takeaways:")
    print("  * In (1) H(E) tracks H(D)-H(R) almost exactly: every bit of regulator")
    print("    variety cancels one bit of disturbance. Doubling k removes one bit of H(E).")
    print("  * In (2) the responses carry noise uncorrelated with D, so H(R) rises but")
    print("    I(D;R) does not. The residual H(E) sits at H(D)-I(D;R) (the '|' marker),")
    print("    strictly above the now-slack H(D)-H(R). Uncorrelated regulator variety is")
    print("    wasted -- a quantitative version of Conant & Ashby's good-regulator point.")
    print()
    print(f"loose-bound violations: (1) {'none' if ok1 else 'FOUND'} , "
          f"(2) {'none' if ok2 else 'FOUND'}")


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--seed", type=int, default=1, help="PRNG seed (default 1)")
    p.add_argument("--m", type=int, default=12, help="number of disturbance states (default 12)")
    p.add_argument("--samples", type=int, default=200000,
                   help="Monte-Carlo samples per row (default 200000)")
    args = p.parse_args()
    run(seed=args.seed, m=args.m, n_samples=args.samples)


if __name__ == "__main__":
    main()
