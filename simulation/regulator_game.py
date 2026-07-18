#!/usr/bin/env python3
"""
regulator_game.py -- Ashby's regulation game and the counting form of the
Law of Requisite Variety.

Ashby (1956) modelled regulation as a game on a table.  A disturbance D takes
one of |D| values; a regulator R, having seen D, chooses one of |R| responses;
a fixed table maps each (D, R) pair to an *outcome*.  The regulator's job is to
force the outcomes into as small a set as possible -- ideally a single
acceptable state.  The counting form of the law states:

        (minimum achievable outcome variety)  >=  |D| / |R|

provided the disturbance genuinely "gets through" the table -- i.e. for a fixed
response, distinct disturbances give distinct outcomes (every column of the
table is injective, the "full variety" condition).  Taking log2 of both sides
gives the information form  H(O) >= H(D) - H(R).

This script:
  * builds regulation tables,
  * finds the regulator's optimal strategy by exact search (minimum set cover
    over outcome labels -- the fewest distinct outcomes the regulator can be
    forced down to),
  * sweeps the regulator's move count |R| and prints the empirical bound
    |E| >= ceil(|D|/|R|) for random full-variety tables (bound HOLDS), and
  * shows a cyclic Latin-square construction that meets the bound with
    equality (bound is TIGHT).

Standard library only.  Reproducible via --seed.
"""

from __future__ import annotations

import argparse
import itertools
import random
from math import ceil, log2


# --------------------------------------------------------------------------
# Core: the regulator's best strategy.
# --------------------------------------------------------------------------
def min_outcome_variety(table: list[list[int]], n_d: int, n_r: int) -> int:
    """Return the minimum number of *distinct* outcomes the regulator can be
    driven down to.

    The regulator observes the disturbance d and picks a response r; the
    outcome is table[d][r].  The regulator wants the set of outcomes (over all
    disturbances) to be as small as possible.  The reachable outcome set for a
    disturbance d is {table[d][r] : r}.  The best strategy chooses, for every
    d, a response whose outcome lies in a common small "acceptable" set S.

    Finding the smallest such S is exactly a minimum set-cover / hitting-set
    problem: pick the fewest outcome labels S such that every disturbance can
    reach some label in S.  We solve it exactly by ascending-size search, which
    is fine for the small tables used here.
    """
    reach = [set(table[d][r] for r in range(n_r)) for d in range(n_d)]
    universe = sorted(set().union(*reach))
    for size in range(1, len(universe) + 1):
        for combo in itertools.combinations(universe, size):
            s = set(combo)
            if all(s & reach[d] for d in range(n_d)):
                return size
    return len(universe)


# --------------------------------------------------------------------------
# Table constructions.
# --------------------------------------------------------------------------
def random_full_variety_table(n_d: int, n_r: int, rng: random.Random) -> list[list[int]]:
    """A table whose every column is a permutation of the outcome labels
    0..n_d-1.  Column-injectivity is the "full variety" condition: for a fixed
    regulator response, distinct disturbances yield distinct outcomes, so the
    disturbance passes through undiminished and the counting bound applies."""
    columns = []
    for _ in range(n_r):
        perm = list(range(n_d))
        rng.shuffle(perm)
        columns.append(perm)
    return [[columns[r][d] for r in range(n_r)] for d in range(n_d)]


def cyclic_latin_table(n_d: int, n_r: int) -> list[list[int]]:
    """table[d][r] = (d + r) mod n_d, using the first n_r columns of the full
    n_d x n_d Latin square.  The reachable outcome set for disturbance d is the
    length-n_r cyclic window {d, d+1, ..., d+n_r-1} (mod n_d).  Covering every
    window needs points spaced at most n_r apart, i.e. exactly ceil(n_d/n_r)
    of them -- so this construction meets the bound with equality."""
    return [[(d + r) % n_d for r in range(n_r)] for d in range(n_d)]


# --------------------------------------------------------------------------
# Driver.
# --------------------------------------------------------------------------
def run(seed: int, n_d: int, trials: int) -> None:
    rng = random.Random(seed)

    print("=" * 74)
    print("Ashby's regulation game -- counting form of Requisite Variety")
    print("=" * 74)
    print(f"disturbances |D| = {n_d}   (H(D) = log2 {n_d} = {log2(n_d):.3f} bits)")
    print(f"random full-variety tables per |R|: {trials}   seed: {seed}")
    print()
    print("Claim:  min achievable outcome variety |E|  >=  ceil(|D|/|R|)")
    print("        (equivalently  H(E) >= H(D) - H(R)  in the entropy form)")
    print()

    header = (
        f"{'|R|':>4} | {'bound':>6} | {'H(D)-H(R)':>10} | "
        f"{'random min':>11} | {'random mean':>11} | {'cyclic':>7} | {'tight?':>6}"
    )
    print(header)
    print("-" * len(header))

    violations = 0
    for n_r in range(1, n_d + 1):
        bound = ceil(n_d / n_r)
        entropy_bound = log2(n_d) - log2(n_r)

        achieved = []
        for _ in range(trials):
            table = random_full_variety_table(n_d, n_r, rng)
            achieved.append(min_outcome_variety(table, n_d, n_r))
        rand_min = min(achieved)
        rand_mean = sum(achieved) / len(achieved)

        # every random full-variety table must respect the lower bound
        if rand_min < bound:
            violations += 1

        cyclic = min_outcome_variety(cyclic_latin_table(n_d, n_r), n_d, n_r)
        tight = "yes" if cyclic == bound else "NO"

        print(
            f"{n_r:>4} | {bound:>6} | {entropy_bound:>10.3f} | "
            f"{rand_min:>11} | {rand_mean:>11.2f} | {cyclic:>7} | {tight:>6}"
        )

    print("-" * len(header))
    print()
    print(f"bound violations across all random tables: {violations}")
    print("Reading the table:")
    print("  * 'bound'       = ceil(|D|/|R|), the counting-form lower bound.")
    print("  * 'H(D)-H(R)'   = the same bound in bits (log2 of the counting bound).")
    print("  * 'random min'  = best (smallest) outcome variety found over random")
    print("                    full-variety tables; it never drops below 'bound'.")
    print("  * 'cyclic'      = outcome variety for the cyclic Latin construction;")
    print("                    it equals the bound, so the bound is TIGHT.")
    print()
    print("Interpretation: to pin the outcome to a single acceptable state (|E|=1)")
    print("the regulator needs |R| >= |D| -- as many distinct responses as there")
    print("are distinct disturbances. Starve it of responses and residual outcome")
    print('variety is forced back onto you: "only variety can destroy variety."')


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--seed", type=int, default=1, help="PRNG seed (default 1)")
    p.add_argument("--nd", type=int, default=8, help="disturbance variety |D| (default 8)")
    p.add_argument("--trials", type=int, default=300,
                   help="random tables per |R| value (default 300)")
    args = p.parse_args()
    run(seed=args.seed, n_d=args.nd, trials=args.trials)


if __name__ == "__main__":
    main()
