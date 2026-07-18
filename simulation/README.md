# `simulation/` — the theory, made executable

Four small, dependency-free Python programs that turn the claims of the guide
into experiments you can run, perturb, and check. Each one prints its setup, the
quantities it measures, and the theoretical bound it is testing — so the output
reads as a proof-by-example rather than a black box.

Everything here uses **only the Python standard library** (Python 3.10+). No
`pip install`, no virtual environment. Randomness is seeded for reproducibility,
and every script exposes `--seed` (and a few other knobs — pass `--help`).

```bash
# from this directory
python regulator_game.py     # Ashby's regulation game — counting form
python entropy_bound.py      # H(E) >= H(D) - H(R) by Monte Carlo
python homeostat.py          # Ashby's homeostat — ultrastability
python vsm_firm.py           # a toy Viable System Model firm
```

Each finishes in a few seconds (well under a minute). Typical wall-clock on a
laptop: `regulator_game` ~1s, `entropy_bound` ~2.5s, `homeostat` ~2s,
`vsm_firm` ~1s.

---

## What each script demonstrates

### `regulator_game.py` — the counting form of Requisite Variety

Builds Ashby's regulation game as a table mapping each `(disturbance, response)`
pair to an outcome, then finds the regulator's **optimal** strategy by exact
search (a minimum set-cover over outcome labels: the fewest distinct outcomes the
regulator can be forced down to). It sweeps the number of regulator moves `|R|`
and confirms, for random *full-variety* tables, the counting bound

```
minimum achievable outcome variety   >=   ceil( |D| / |R| )
```

— equivalently `H(O) >= H(D) - H(R)` after taking `log2`. It then shows a cyclic
Latin-square construction that meets the bound with **equality**, so the bound is
not just correct but tight.

Connects to: [`docs/01-foundations.md`](../docs/01-foundations.md) (variety and
constraint) and [`docs/02-ashbys-law.md`](../docs/02-ashbys-law.md) (the counting
form).

Sample output:

```
 |R| |  bound |  H(D)-H(R) |  random min | random mean |  cyclic | tight?
-------------------------------------------------------------------------
   1 |      8 |      3.000 |           8 |        8.00 |       8 |    yes
   2 |      4 |      2.000 |           4 |        4.80 |       4 |    yes
   4 |      2 |      1.000 |           2 |        2.91 |       2 |    yes
   8 |      1 |      0.000 |           1 |        1.97 |       1 |    yes

bound violations across all random tables: 0
```

The regulator needs `|R| >= |D|` — as many distinct responses as there are
distinct disturbances — before it can pin the outcome to a single acceptable
state. Starve it and residual outcome variety is forced back onto you.

---

### `entropy_bound.py` — the information form, `H(E) >= H(D) - H(R)`

A Monte-Carlo experiment. A disturbance `D` is drawn uniformly from `m` states; a
regulator of *capacity* `k` lumps the `m` disturbances into `k` groups and emits
one canceling response per group; the residual is `E = (D - response) mod m`. All
three entropies are estimated from samples with a plug-in estimator (no analytic
shortcuts for the achieved `H(E)`), and the script verifies the exact chain

```
H(E)  >=  H(E|R)  =  H(D|R)  =  H(D) - I(D;R)  >=  H(D) - H(R).
```

A first sweep uses a **deterministic** regulator, where `I(D;R) = H(R)` and the
bound is tight: `H(E)` tracks `H(D) - H(R)` almost exactly, and each doubling of
`k` removes one bit of residual. A second sweep adds a **noisy** regulator whose
responses carry noise uncorrelated with `D`, so `I(D;R) < H(R)`: the residual sits
at `H(D) - I(D;R)`, strictly above the now-slack `H(D) - H(R)`. Regulator variety
that is not correlated with the disturbance is simply wasted — a quantitative echo
of Conant & Ashby's "good regulator" theorem.

Connects to: [`docs/01-foundations.md`](../docs/01-foundations.md) (Shannon
entropy) and [`docs/02-ashbys-law.md`](../docs/02-ashbys-law.md) (the entropy
form).

Sample output (deterministic regulator):

```
  k |  H(D) |  H(R) | I(D;R) |  loose |  H(E) | H(E) vs loose bound (achieved=#, tight bound=|)
  1 | 3.585 | 0.000 |  0.000 |  3.585 | 3.585 | #############################|
  2 | 3.585 | 1.000 |  1.000 |  2.585 | 2.585 | ######################|-------
  4 | 3.585 | 2.000 |  2.000 |  1.585 | 1.585 | #############|----------------
 12 | 3.585 | 3.585 |  3.585 |  0.000 | 0.000 | |-----------------------------
```

---

### `homeostat.py` — Ashby's homeostat and ultrastability

A minimal model of the four-unit machine from *Design for a Brain*. The units are
a vector `x` with linear coupling `x(t+1) = A x(t)`, clamped to a finite physical
range. Each `|x_i|` is an essential variable that must stay inside a survival band;
when it leaves the band, a uniselector re-randomizes the wiring `A`. A random
wiring is dynamically stable (spectral radius `< 1`) with some fixed probability
`p`, so the number of re-selections needed after a disturbance is geometric with
mean `~ 1/p` — the system reliably restabilizes by generate-and-test, with no
model of the disturbance and no designer in the loop.

The script estimates `p`, runs many cold-start disturbances and reports the
distribution of uniselector trips (observed mean matches the predicted `1/p`), and
then demonstrates **ultrastability**: once a viable wiring is found, further shocks
of the same class are absorbed with *zero* re-selection. Stability of the
conditions for stability is the second-order property Ashby was after.

Connects to: [`docs/01-foundations.md`](../docs/01-foundations.md) (essential
variables and the regulator picture); background for the "search for a stable
configuration" theme that recurs in
[`docs/04-metalanguage-metasystems.md`](../docs/04-metalanguage-metasystems.md).

Sample output:

```
P(fresh wiring viable)  ~ 0.183
predicted re-selections per disturbance ~ 1/p = 5.45 (geometric search)

Cold-start restabilization over 400 disturbances (each starting in an unstable regime):
  re-selections : mean 5.34  median 4  max 37
  restabilized  : 400/400 (all disturbances absorbed)

Ultrastability check -- after a viable wiring is found, apply 25 more kicks:
  re-selections needed: mean 0.00  max 0
```

*Modelling note:* the real homeostat re-selects each out-of-band unit's weights
independently; here every trip redraws the whole matrix. That keeps the search
statistics a clean Bernoulli(`p`) trial per trip while preserving the phenomenon.

---

### `vsm_firm.py` — a toy Viable System Model firm

An agent-based firm of `N` operating units facing demand built from three kinds of
variety: persistent per-unit structure (trackable locally), a common seasonal
swing (forecastable if denoised), and idiosyncratic white shocks (absorbable only
by steering slack). A single knob, the variety level `nu`, scales all three. Three
control regimes run against the *same* demand stream:

- **CENTRAL** — sees only the aggregate of last step's demand and sets one uniform
  capacity for every unit (responding variety `~1`).
- **AUTONOMOUS** — Beer's System 1: each unit sets its own capacity from its own
  last demand (responding variety `N`), absorbing per-unit variety where it arises.
- **META** — S1 autonomy plus a metasystem: **S4** forecasts the common swing from
  the denoised aggregate and pre-positions for it; **S3** holds a reserve sized to
  recent volatility and steers it to whichever units fall short this step (idle
  reserve is charged as waste, so it earns its keep only when variety is real).

Sweeping `nu` reproduces the signature result: at zero variety all three are
near-perfect (central control is adequate — there is nothing to absorb), and as
`nu` rises CENTRAL degrades fastest, AUTONOMOUS holds better, and META holds best,
the gap widening with the very variety it exists to absorb.

Connects to: [`docs/03-viable-system-model.md`](../docs/03-viable-system-model.md)
(the five systems), [`docs/04-metalanguage-metasystems.md`](../docs/04-metalanguage-metasystems.md)
(why a metasystem is needed), and
[`docs/05-variety-engineering.md`](../docs/05-variety-engineering.md) (attenuation
and amplification).

Sample output (viability score, % of unit-steps within tolerance):

```
  nu |   CENTRAL |  AUTONOMOUS |  META (S1+S3+S4)
-------------------------------------------------
   0 |    100.0% |      100.0% |           100.0%
   2 |     70.7% |       80.0% |            93.5%
   8 |     56.6% |       59.6% |            84.2%
  18 |     58.4% |       61.6% |            81.9%
```

---

## How to read these as evidence, not decoration

The guide states two theorems (the counting and entropy forms of Requisite
Variety) and one engineering doctrine (absorb variety low, add a metasystem for
the residual). The first two scripts *test the theorems* — they would print a
bound violation if the inequality ever failed, and none appears. The last two
*illustrate the doctrine* on dynamical and organizational models: they are honest
simulations, not proofs, and the READMEs and docstrings say so where it matters
(e.g. the homeostat's whole-matrix re-selection, or the toy firm's deliberately
simple forecasting and reserve rules). Rerun any of them with a different `--seed`
to confirm the conclusions are not artifacts of one lucky draw.

---

## Primary sources

- Ashby, W. Ross. *An Introduction to Cybernetics.* Chapman & Hall, 1956. (Variety; the regulation game and the Law of Requisite Variety, Chapter 11.)
- Ashby, W. Ross. *Design for a Brain: The Origin of Adaptive Behaviour.* 2nd ed., Chapman & Hall, 1960. (The homeostat; ultrastability.)
- Shannon, Claude E. "A Mathematical Theory of Communication." *Bell System Technical Journal*, vol. 27, 1948, pp. 379–423 and 623–656. (Entropy `H`.)
- Conant, Roger C., and W. Ross Ashby. "Every Good Regulator of a System Must Be a Model of That System." *International Journal of Systems Science*, vol. 1, no. 2, 1970, pp. 89–97.
- Beer, Stafford. *Brain of the Firm.* Allen Lane / Herder and Herder, 1972 (2nd ed., Wiley, 1981).
- Beer, Stafford. *The Heart of Enterprise.* Wiley, 1979. (The Viable System Model; Systems 1–5.)
