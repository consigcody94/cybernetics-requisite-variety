# 07 · Research frontiers — where the theory went after Ashby

> Previous: [06 — Modern Extensions](06-modern-extensions.md) · Back to [README](../README.md)

The earlier documents build the classical machinery: variety and constraint
([01](01-foundations.md)), the Law of Requisite Variety and the good-regulator
theorem ([02](02-ashbys-law.md)), Beer's Viable System Model ([03](03-viable-system-model.md)),
metasystems ([04](04-metalanguage-metasystems.md)), the practical craft of
attenuators and amplifiers ([05](05-variety-engineering.md)), and an applied essay
on modern systems ([06](06-modern-extensions.md)). This document does something
different. It is a **guided tour of the research literature** that has, in the
seventy years since *An Introduction to Cybernetics*, taken Ashby's slogan and
turned pieces of it into sharp theorems, computable quantities, and working
engineering.

The organising question is: *which parts of "only variety can destroy variety"
have since been made precise, and how?* Six threads run through the answer, and
this document takes them in turn:

- **(a) Information-theoretic sharpenings** turn the entropy bound `H(E) ≥ H(D) − H(R)`
  into exact bit-accounting — control limits, communication data-rate theorems,
  and the thermodynamics of feedback, where each bit of information the regulator
  acquires is paid for and cashed out against the second law.
- **(b) The good regulator's descendants** carry Conant & Ashby's "must be a model"
  claim forward through the control-theoretic internal model principle and the
  free-energy / active-inference programme, and argue hard about what "model"
  really means.
- **(c) Variety as agent capability** — the *empowerment* line — recasts requisite
  variety as an intrinsic, computable drive that an embodied agent can actually
  maximise.
- **(d) Multi-scale requisite variety** replaces Ashby's single scalar inequality
  with a whole spectrum of scale-indexed constraints, and supplies measurable
  complexity profiles to go with them.
- **(e) Organisational and VSM applications** show Beer's recursive variety logic
  used as a live diagnostic and design method on real institutions.
- **(f) The AI era** brings requisite variety and the good-regulator theorem
  directly into loss-of-control, oversight, and agent-governance discourse.

Every paper below is a real, verifiable publication; each entry gives a citation
with a working link and then an original annotation — what the result proves, how
it sharpens or extends the classical law, and what it means for the framework this
repository builds. Where a result *genuinely generalises Ashby* (the multi-scale
law, the entropy-reduction limits, the data-rate theorems), the annotation says
precisely how. A closing section collects the open questions the frontier has
not yet settled.

A caveat carried over from [06](06-modern-extensions.md): several of these threads
reach conclusions "close to" or "in the spirit of" Ashby by very different
formal routes. Convergence from independent formalisms is real evidence that the
underlying constraint is not an artefact of one setup — but each theorem should
be read with its own hypotheses attached, and the annotations try to keep those
hypotheses visible.

---

## (a) Information-theoretic sharpenings of the law

Ashby always insisted his law was a sibling of Shannon's channel-capacity result,
not a rival (see [02 §5](02-ashbys-law.md)). This thread makes the family
resemblance exact. The recurring pattern: an unwanted flow of entropy into the
essential variables can be cancelled only by an equal-or-greater flow of
information into the regulator — and that information flow now comes with a
price tag denominated in bits, in channel capacity, and in joules.

### Touchette & Lloyd (2000) — Information-Theoretic Limits of Control

Hugo Touchette and Seth Lloyd. "Information-Theoretic Limits of Control."
*Physical Review Letters* **84**, 1156 (2000). arXiv:
[chao-dyn/9905039](https://arxiv.org/abs/chao-dyn/9905039).

Recasts controllability itself in information-theoretic terms. A generalised
second law — entropy *plus* information — sets an absolute floor on the
dissipation any open-loop controller must pay, and closed-loop feedback is shown
to behave like a zero-sum game in which **each bit the controller reads from the
system can lower the system's entropy by at most one bit** beyond what open-loop
already achieves. That "at most one bit of order per bit of information" is
exactly the exchange rate Ashby's inequality asserts, now derived as a physical
law rather than a combinatorial one. For this repository it is the direct
sharpening of `H(E) ≥ H(D) − H(R)`: the entropy (variety) a regulator can strip
out of the essential variables is bounded by the information it acquires about
them, and acquiring that information has a thermodynamic cost. It grounds the
entropy form of the law in [02 §4](02-ashbys-law.md) in physics and connects
requisite variety to the second law.

### Sagawa & Ueda (2008) — Second Law of Thermodynamics with Discrete Quantum Feedback Control

Takahiro Sagawa and Masahito Ueda. "Second Law of Thermodynamics with Discrete
Quantum Feedback Control." *Physical Review Letters* **100**, 080403 (2008). arXiv:
[0710.0956](https://arxiv.org/abs/0710.0956).

The canonical "information is a resource for control" theorem. Sagawa and Ueda
derive a generalised second law for feedback-controlled systems in which the
maximum extractable work exceeds the ordinary free-energy bound by an amount
equal to the **mutual information** the controller gains by measuring the system —
with overall consistency with the second law preserved once the thermodynamic cost
of the controller's own information processing is counted. Read against Ashby, this
is the thermodynamic counterpart of requisite variety: it quantifies exactly how
much regulatory leverage (work, order) a controller can buy per bit of acquired
information. The mutual-information term `I(D;R)` that appears in the sharp form of
the entropy law ([02 §4](02-ashbys-law.md)) reappears here as the currency of a
Maxwell's-demon accounting, making precise the sense in which *gathering variety
about a disturbance is what pays for suppressing it*.

### Sagawa & Ueda (2010) — Generalized Jarzynski Equality under Nonequilibrium Feedback Control

Takahiro Sagawa and Masahito Ueda. "Generalized Jarzynski Equality under
Nonequilibrium Feedback Control." *Physical Review Letters* **104**, 090602 (2010).
arXiv: [0907.4914](https://arxiv.org/abs/0907.4914).

Extends the Jarzynski nonequilibrium work relation to systems under
measurement-based feedback, adding terms for the mutual information obtained and
for the *feedback efficacy*, and exhibits an explicit "information ratchet" that
transports a Brownian particle and extracts positive work purely from measured
information. Where the 2008 paper states the bound, this one gives a
fluctuation-level, experimentally testable model of an **information engine** — the
concrete physical device in which information about a system's state is literally
converted into directed control action. For the repository it is the
microphysical existence proof behind variety attenuation and amplification: it
shows the variety-balance idea operating at the scale of a single molecular
regulator, where every claim can be checked against measurable work and heat.

### Tatikonda & Mitter (2004) — Control Under Communication Constraints

Sekhar Tatikonda and Sanjoy Mitter. "Control Under Communication Constraints."
*IEEE Transactions on Automatic Control* **49**(7):1056–1068 (2004). DOI:
[10.1109/TAC.2004.831187](https://doi.org/10.1109/TAC.2004.831187).

A foundational **data-rate theorem**. Tatikonda and Mitter formulate feedback
control of a linear system across a finite-rate digital channel connecting sensor
to controller, and establish matching upper and lower bounds on the minimum
communication rate needed to meet control objectives such as stabilisation, tying
the required bit rate to the system's unstable dynamics. This is a
communication-constrained restatement of requisite variety with teeth: keeping an
unstable plant under control provably requires a channel carrying *at least a
definite number of bits per unit time*. It also supplies something Ashby's static
count does not — a **rate** form of the law. The regulator must not merely possess
enough variety; it must *receive* information-bearing capacity fast enough to
match the rate at which the plant generates fresh uncertainty. That temporal
dimension is exactly the gap flagged in the [06 open problems](06-modern-extensions.md#open-problems).

### Nair & Evans (2004) — Stabilizability of Stochastic Linear Systems with Finite Feedback Data Rates

Girish N. Nair and Robin J. Evans. "Stabilizability of Stochastic Linear Systems
with Finite Feedback Data Rates." *SIAM Journal on Control and Optimization*
**43**(2):413–436 (2004). DOI:
[10.1137/S0363012902402116](https://doi.org/10.1137/S0363012902402116).

The rigorous stochastic form of the data-rate theorem, and one of the load-bearing
classics of the field. Nair and Evans prove that the infimum feedback data rate
required for mean-square stabilisation of a noisy linear system equals the **sum of
the logarithms of the magnitudes of the unstable open-loop eigenvalues**, and that
no coding-plus-control scheme can stabilise below this threshold. This is arguably
the sharpest quantitative generalisation of Ashby in the entire literature, and it
is worth stating precisely how it generalises: the quantity `Σ log|λᵢ|` is the
*rate* (bits per unit time) at which the unstable dynamics manufacture new
variety, and the theorem says the regulator must import at least that many bits per
unit time or lose control. Ashby's static inequality `V(R) ≥ V(D)` becomes a
conservation of variety *flux* — inbound information rate must match the plant's
variety-production rate. Everything in [02](02-ashbys-law.md) about "only variety
can destroy variety" survives, now indexed by time and pinned to a computable
number.

### Ranade & Sahai (2017) — Control Capacity

Gireeja Ranade and Anant Sahai. "Control Capacity." arXiv:
[1701.04187](https://arxiv.org/abs/1701.04187) (2017; cs.IT / eess.SY).

Where the data-rate theorems constrain the *sensing* side, control capacity builds
a Shannon-style theory for the *actuation* side. Ranade and Sahai define control
capacity as the maximum rate, in bits, at which a controller acting through an
uncertain (noisy multiplicative) actuation channel can dissipate uncertainty from
a system; give a computable single-letter formula for scalar memoryless channels;
and prove that a system is stabilisable exactly when its control capacity exceeds
the log of the unstable open-loop eigenvalue. This completes the picture: Ashby's
demand to "match the disturbance's variety" is made quantitative not just for the
regulator's *knowledge* of the disturbance but for its *authority to act* when that
authority is itself limited or unreliable. Mirroring channel capacity, the result
comes with a strong converse and a bit-valued measure of side-information — turning
the intuitive "how much can this actuator actually move the system?" into a number.

### Kostina & Hassibi (2019) — Rate-Cost Tradeoffs in Control

Victoria Kostina and Babak Hassibi. "Rate-Cost Tradeoffs in Control." *IEEE
Transactions on Automatic Control* (2019). arXiv:
[1612.02126](https://arxiv.org/abs/1612.02126) (2016).

Advances the data-rate theorem from the binary question "can we stabilise?" to the
graded question "how well, per bit?" Kostina and Hassibi derive an explicit lower
bound on the *directed* mutual information between channel input and output needed
to achieve a target LQR (quadratic) control cost, valid for vector, non-Gaussian,
and partially observed systems, and show that a simple scheme quantising only the
innovation nearly attains it. This is the rate-distortion-style sharpening of the
variety-balance equation: instead of a cliff between "regulable" and "not," it
gives a smooth exchange curve trading communication rate against control quality.
For a repository that repeatedly stresses requisite variety is a *balance*
condition rather than a threshold, this is the theorem that makes the marginal
value of each additional bit of regulatory information explicit.

---

## (b) The good regulator's descendants

Conant & Ashby's 1970 theorem — every good regulator must be a model of the system
it regulates (see [02 §6](02-ashbys-law.md)) — has two distinct lineages. One runs
through control engineering as the *internal model principle*; the other runs
through theoretical neuroscience as the *free energy principle* and active
inference. Recent work has begun to prove that the two lineages are the same result
in different clothes — while a parallel critical strand asks whether "contains a
model" is a fact about the mechanism or a choice made by whoever is looking.

### Francis & Wonham (1976) — The Internal Model Principle of Control Theory

Bruce A. Francis and W. Murray Wonham. "The Internal Model Principle of Control
Theory." *Automatica* **12**(5):457–465 (1976). DOI:
[10.1016/0005-1098(76)90006-6](https://doi.org/10.1016/0005-1098%2876%2990006-6).

Using the geometric approach to linear time-invariant control, Francis and Wonham
prove that any compensator achieving output regulation that remains stable under
small parameter variations must contain a *reduplicated internal model* of the
dynamics generating the disturbance and reference signals — regulation without such
an embedded model cannot be structurally stable. This is the control-theoretic
origin of the internal model principle and the hardest engineering statement of
"a good regulator must model the system." It gives the repository a genuine
theorem with an exact necessity claim to stand beside Conant & Ashby: where
Conant & Ashby argue from information and optimality, Francis & Wonham argue from
the algebra of robust pole placement, and reach the same destination. It is the
classic that every modern Bayesian or free-energy re-derivation cites as its
target, so it anchors this whole section.

### Buckley, Kim, McGregor & Seth (2017) — The Free Energy Principle for Action and Perception: A Mathematical Review

Christopher L. Buckley, Chang Sub Kim, Simon McGregor and Anil K. Seth. "The Free
Energy Principle for Action and Perception: A Mathematical Review." arXiv:
[1705.09156](https://arxiv.org/abs/1705.09156) (2017; later *Journal of
Mathematical Psychology*).

Collects the full mathematical machinery of Friston's free-energy-principle
implementation for perception and action into a single treatment, derives the
equations of a complete worked agent-based model, and — crucially for an honest
guide — makes explicit the assumption structure the derivation quietly depends on.
The free-energy principle recasts Ashby-style regulation as *variational
inference*: an agent that keeps its essential variables in bounds is reinterpreted
as one that minimises a bound on surprise, i.e. maintains and updates a generative
model of its world. This paper is the rigorous reference point for that whole
lineage. Its value here is exactly its separation of what the formalism *derives*
from the broader unifying rhetoric that surrounds it — the same "state the theorem,
mark the heuristic" discipline this repository tries to keep.

### Millidge, Seth & Buckley (2021) — A Mathematical Walkthrough and Discussion of the Free Energy Principle

Beren Millidge, Anil Seth and Christopher L. Buckley. "A Mathematical Walkthrough
and Discussion of the Free Energy Principle." arXiv:
[2108.13343](https://arxiv.org/abs/2108.13343) (2021).

Walks step by step through the FEP's central claim — that any system statistically
separable from its environment and holding itself at a non-equilibrium steady state
can be *read as* minimising variational free energy, and therefore as performing
approximate Bayesian inference — and appends a detailed catalogue of the
assumptions and internal controversies. This is the modern, generalised form of
the "a persisting system must model its world" intuition, extending Conant & Ashby
well beyond their restricted deterministic setup to any system that maintains a
boundary against its environment. For the repository it is doubly useful: it states
the strongest available version of the good-regulator idea, and its explicit
accounting of live disputes gives honest material for marking where the
FEP-as-regulation analogy is solid versus where it overreaches.

### Baltieri, Buckley & Bruineberg (2020) — Predictions in the Eye of the Beholder: an Active Inference Account of Watt Governors

Manuel Baltieri, Christopher L. Buckley and Jelle Bruineberg. "Predictions in the
Eye of the Beholder: an Active Inference Account of Watt Governors." *Artificial
Life Conference (ALIFE 2020)*. arXiv:
[2006.11495](https://arxiv.org/abs/2006.11495).

The necessary counterweight to the two FEP papers above. Baltieri and colleagues
build an active-inference generative model for the Watt centrifugal governor — the
textbook *anti-representational* device, long used to argue that some controllers
plainly contain no model — and show it can indeed be redescribed as prediction-error
minimisation. Their point is deflationary: because *almost any* system admits such
a redescription, the move carries little genuine explanatory weight on its own.
This bears directly on how literally the good-regulator theorem should be read
([02 §6](02-ashbys-law.md) already flags that "model" is a weak, precise notion,
not a claim about internal simulations). The paper sharpens the caveat: finding a
model "inside" a regulator can be an interpretive choice made by an outside
observer rather than a discovered fact about the mechanism. The repository should
cite it wherever it invokes Conant & Ashby, as the standing warning against
over-reading.

### Virgo, Biehl, Baltieri & Capucci (2025) — A "Good Regulator Theorem" for Embodied Agents

Nathaniel Virgo, Martin Biehl, Manuel Baltieri and Matteo Capucci. "A 'Good
Regulator Theorem' for Embodied Agents." *Artificial Life Conference (ALIFE 2025)*.
arXiv: [2508.06326](https://arxiv.org/abs/2508.06326).

A direct modern re-derivation and repair of the good-regulator theorem. Virgo and
colleagues reframe the Conant-Ashby result so that any agent capable of performing
a regulation task can be *interpreted by an external observer* as holding beliefs
about its environment that it updates in response to sensory input — a
belief-updating notion of "model" broader than Conant & Ashby's homomorphism, and
one that dissolves the Artificial-Life counterexamples (the Watt governor among
them) where no explicit model is visible. Two clarifications matter for this
repository: first, the model is *imposed by an interpreter* rather than intrinsic
to the mechanism (making peace with the Watt-governor critique above); and second,
the result holds whether an agent regulates its *environment* or its own *internal
state*. That second point is exactly the sharpening the good-regulator material in
[02](02-ashbys-law.md) and [06](06-modern-extensions.md) needs when the "system"
being regulated is partly the agent itself.

### Baltieri, Biehl, Capucci & Virgo (2025) — A Bayesian Interpretation of the Internal Model Principle

Manuel Baltieri, Martin Biehl, Matteo Capucci and Nathaniel Virgo. "A Bayesian
Interpretation of the Internal Model Principle." arXiv:
[2503.00511](https://arxiv.org/abs/2503.00511) (2025).

This is the paper that formally welds the two lineages of the good-regulator idea
together. Baltieri and colleagues restate the control-theoretic internal model
principle (Francis & Wonham, above) in the language of categorical systems theory,
extract a general definition of "model" from it, and *prove* that this notion is a
special case of possibilistic Bayesian filtering — connecting the internal models
of control engineering to the Bayesian internal models of cognitive science with an
actual theorem rather than an analogy. For the repository this supplies a formal
spine: it ties Ashby's cybernetics, classical robust regulation, and the
free-energy / predictive-processing tradition into a single chain, so the
convergence noted in [02 §6](02-ashbys-law.md) is upgraded from "genuine evidence"
to a demonstrated special-case relationship.

### Weinstein, Alshammari, Timperi, Bennis & LaValle (2024) — An Internal Model Principle for Robots

Vadim K. Weinstein, Tamara Alshammari, Kalle G. Timperi, Mehdi Bennis and Steven
M. LaValle. "An Internal Model Principle for Robots." arXiv:
[2406.11237](https://arxiv.org/abs/2406.11237) (2024).

Reaches the good-regulator / internal-model conclusion by a discrete,
non-probabilistic, constructive route. Weinstein and colleagues prove that a robot
relying only on internally available sensor information comes to have an internal
structure *isomorphic* — or bisimulation-equivalent — to its environment once it
satisfies an internally verifiable "sufficiency" condition, and show that
sufficiency is a discrete, non-probabilistic limiting case of surprise
minimisation. This gives the repository an engineering-flavoured counterpart to the
probabilistic FEP derivations: the same destination (the regulator ends up
mirroring the regulated system) reached with combinatorial state machinery instead
of variational calculus, and with a *sufficiency condition the agent can check for
itself*. It is a cleaner statement of what "having a model" can concretely mean,
and it pairs naturally with the Bayesian bridge above.

---

## (c) Variety as agent capability — empowerment

Ashby's variety is a count of distinguishable states. The *empowerment* programme
turns that count into an agent-centric, task-independent utility an embodied
controller can compute and maximise: how many distinguishable futures can I bring
about and then perceive? That is requisite variety read as *capability* rather than
as a bound — the regulator's own controllable-and-observable capacity, measured in
bits.

### Klyubin, Polani & Nehaniv (2005) — All Else Being Equal Be Empowered

Alexander S. Klyubin, Daniel Polani and Chrystopher L. Nehaniv. "All Else Being
Equal Be Empowered." *ECAL 2005 (Advances in Artificial Life)*, LNCS 3630,
pp. 744–753, Springer. DOI:
[10.1007/11553090_75](https://doi.org/10.1007/11553090_75).

The origin of empowerment. Klyubin and colleagues define it as a universal,
task-independent, agent-centric utility equal to the information-theoretic
*capacity of the agent's own perception-action channel* — the channel that runs
from the agent's actions, through the world, back to the agent's sensors. An agent
that simply maximises this quantity is driven toward states from which it has the
most potential control over its own future sensory input, with no hand-crafted
reward. This is the cleanest bridge from Ashby's law to embodied agents: it takes
the very quantity the Law of Requisite Variety cares about — how many
distinguishable situations a controller can act on *and* observe — and turns it
into an intrinsic drive. Requisite variety stops being only a constraint the
designer checks and becomes an objective the agent itself pursues.

### Salge, Glackin & Polani (2014) — Empowerment: An Introduction

Christoph Salge, Cornelius Glackin and Daniel Polani. "Empowerment — an
Introduction." In *Guided Self-Organization: Inception* (Springer). arXiv:
[1310.1863](https://arxiv.org/abs/1310.1863) (2014).

The canonical entry point and review for the whole empowerment programme. It
defines empowerment as the channel capacity between an agent's action sequence and
its subsequent sensor readings, walks through how the same formalism yields
strikingly different behaviours across different sensor-motor embodiments,
catalogues prior applications, and supplies a fast approximation usable in
continuous domains. For this repository it is the paper that most directly
operationalises Ashby's "variety" as an agent's jointly controllable-and-observable
capacity in bits, consolidating a scattered conference literature into one citable
source. It is the natural reading to hand someone who has absorbed
[01](01-foundations.md)–[02](02-ashbys-law.md) and wants to see requisite variety
turned into something a real controller computes.

### Mohamed & Rezende (2015) — Variational Information Maximisation for Intrinsically Motivated Reinforcement Learning

Shakir Mohamed and Danilo Jimenez Rezende. "Variational Information Maximisation
for Intrinsically Motivated Reinforcement Learning." *Advances in Neural
Information Processing Systems (NeurIPS 2015)*. arXiv:
[1509.08731](https://arxiv.org/abs/1509.08731).

The paper that made empowerment tractable at scale. Mohamed and Rezende derive a
scalable *variational lower bound* on the mutual information that defines
empowerment, sidestepping the exponential-cost Blahut-Arimoto computation, and
couple it with deep and convolutional networks so that empowerment can be estimated
and maximised directly from high-dimensional (pixel) observations to actions. This
moves variety-as-capability from a small tabular quantity into a practical
intrinsic objective for modern deep reinforcement learning. It substantiates the
claim, made informally in [06](06-modern-extensions.md), that a learning agent's
tools and action repertoire function as *variety amplifiers* — and it shows the
requisite-variety accounting surviving intact into contemporary machine learning,
not merely as metaphor but as an optimised loss.

### Rosas, Mediano, Biehl, Chandaria & Polani (2020) — Causal Blankets: Theory and Algorithmic Framework

Fernando E. Rosas, Pedro A. M. Mediano, Martin Biehl, Shamil Chandaria and Daniel
Polani. "Causal Blankets: Theory and Algorithmic Framework." arXiv:
[2008.12568](https://arxiv.org/abs/2008.12568) (2020).

Addresses a question Ashby's block diagram simply assumes away: *where is the
boundary between regulator and disturbance, and where do the channels run?* Rosas
and colleagues present a computational-mechanics framework that identifies
perception-action loops directly from data via "causal blankets" — sensory and
active variables defined as *dynamical sufficient statistics*, the differences that
make a difference — and show that every bipartite stochastic process admits such a
blanket, though how well the split yields a genuine perception-action loop depends
on the integrated information across it, with no requirement of steady-state or
Markovian dynamics. This gives a principled, data-driven way to draw the
regulator/disturbance cut and locate the information channels of the loop, which
the diagrams in [01](01-foundations.md) and [02](02-ashbys-law.md) take as given.
It sharpens what counts as "the regulator" and its channels when analysing real
coupled systems.

### Chen & Prokopenko (2025) — Why Collective Behaviours Self-Organise to Criticality

Qianyang Chen and Mikhail Prokopenko. "Why Collective Behaviours Self-Organise to
Criticality: A Primer on Information-Theoretic and Thermodynamic Utility Measures."
*Royal Society Open Science* **12**(6):241655 (2025). arXiv:
[2409.15668](https://arxiv.org/abs/2409.15668).

Situates empowerment within a family of intrinsic utility functions and ties the
whole family back to self-organisation. Chen and Prokopenko interpret the Ising
model as a perception-action loop and compare competing drives — predictive
information, empowerment, active inference, and a thermodynamic-efficiency measure
— showing that thermodynamic efficiency (predictability gained per unit energy
cost) peaks in the *critical* regime, and propose a "super-efficiency" principle
for why collective systems self-organise toward criticality. For this repository it
does two things: it places the agent-level empowerment measure alongside its rivals
so none is mistaken for the only variety-based objective, and it reconnects that
agent-level thread to the whole-system, self-organising view that motivates Beer's
cybernetics ([03](03-viable-system-model.md)) and the multi-scale work in the next
section.

---

## (d) Multi-scale requisite variety and measured complexity

This is the thread that most literally *generalises Ashby's theorem*. Ashby's law
is a single scalar inequality: total response variety must match total disturbance
variety. But a system can command enough variety in aggregate and still be
mismatched at the particular *scale* where disturbances actually strike. The
Bar-Yam programme replaces the scalar with a whole function — complexity as a
function of scale — and proves a scale-indexed law, backed by complexity measures
you can actually compute.

### Siegenfeld & Bar-Yam (2022) — A Formal Definition of Scale-Dependent Complexity and the Multi-Scale Law of Requisite Variety

Alexander F. Siegenfeld and Yaneer Bar-Yam. "A Formal Definition of Scale-dependent
Complexity and the Multi-scale Law of Requisite Variety." arXiv:
[2206.04896](https://arxiv.org/abs/2206.04896) (2022; physics.soc-ph).

The centrepiece of this section. Siegenfeld and Bar-Yam define a class of
complexity-versus-scale functions — *complexity profiles* — that obey a multi-scale
generalisation of Ashby's law: **at each scale, a system must carry at least as much
complexity as the environmental behaviours demanding distinct responses at that
scale**. The profiles satisfy a *sum rule* encoding a tradeoff between fine-scale
and coarse-scale degrees of freedom, and the construction extends to subdivided
systems and to a continuum of components. Here is precisely how it generalises
[02](02-ashbys-law.md): Ashby's `V(R) ≥ V(D)` is recovered as the total (integrated)
statement, but it is now split into a *spectrum* of constraints `C_R(scale) ≥
C_D(scale)` holding at every scale independently, tied together by conservation of
total degrees of freedom. The organisational payoff is immediate and is exactly the
failure mode [06](06-modern-extensions.md) keeps circling: a firm can possess ample
total variety yet be catastrophically under-varied at the one scale where the
disturbance lands (all generalists and no specialists, or vice versa). This is the
rigorous multi-scale sharpening of "only variety can destroy variety."

### Bar-Yam, Harmon & Bar-Yam (2013) — Computationally Tractable Pairwise Complexity Profile

Yavni Bar-Yam, Dion Harmon and Yaneer Bar-Yam. "Computationally Tractable Pairwise
Complexity Profile." *Complexity* **18**(5):20–27 (2013). arXiv:
[1208.0823](https://arxiv.org/abs/1208.0823).

The operational machinery underneath the multi-scale law. This paper reformulates
the complexity profile using only *pairwise* dependencies between components, making
it computable for high-dimensional real systems, and proves the reformulation
coincides with the original profile in identifiable cases, is monotonically
non-increasing in scale, obeys linear superposition for unrelated systems, and
satisfies a conservation-of-degrees-of-freedom sum rule. It is the load-bearing
older result showing that multiscale variety is not merely definable but *tractable
to compute* on real interacting systems. For a repository that insists on turning
slogans into things you can calculate — the whole point of the [simulations](../README.md)
— this is what keeps the 2022 multi-scale law from being purely conceptual: it is
the measurement recipe that lets "how much variety does this regulator have, at each
scale?" be answered with numbers rather than asserted.

### Allen, Stacey & Bar-Yam (2014) — An Information-Theoretic Formalism for Multiscale Structure in Complex Systems

Benjamin Allen, Blake C. Stacey and Yaneer Bar-Yam. "An Information-Theoretic
Formalism for Multiscale Structure in Complex Systems." arXiv:
[1409.4708](https://arxiv.org/abs/1409.4708) (2014; cond-mat.stat-mech).

Provides the deep information-theoretic foundation connecting Shannon-style variety
accounting to multi-scale structure. Allen and colleagues build an axiomatic
framework in which a system's *structure* is the information assigned to
dependencies among its components, giving a formal grounding for the complexity
profile, introducing a "marginal utility of information" index, and explaining why
multivariate mutual information can go negative. The formalism admits any
information measure satisfying its axioms, from Shannon entropy to Kolmogorov
complexity. For this repository it is the conceptual bridge between the entropy
inequality of [02 §4](02-ashbys-law.md) — the `H(E) ≥ H(D) − H(R)` accounting — and
the modern complexity-profile apparatus: it shows that the same information measures
Ashby leaned on, pushed through a multi-scale axiomatisation, yield the scale-indexed
picture, and it explicitly points toward a multiscale cybernetic thermodynamics.

### Siegenfeld & Bar-Yam (2020) — An Introduction to Complex Systems Science and Its Applications

Alexander F. Siegenfeld and Yaneer Bar-Yam. "An Introduction to Complex Systems
Science and its Applications." *Complexity* **2020**:6105872 (2020). arXiv:
[1912.05088](https://arxiv.org/abs/1912.05088).

A largely non-technical review that organises complex-systems science around
complexity profiles, the efficiency-versus-adaptability tradeoff, multi-scale
analysis, evolutionary process, and — centrally — the necessity that a system's
complexity *match* that of its environment. It is written to be readable with only
a high-school mathematics background. This is the complex-systems restatement of
requisite variety for a general audience, and the ideal accessible lead-in to the
formal 2206.04896 above. As a peer-reviewed, pedagogical companion piece it is the
natural "read this first" recommendation for the multi-scale thread in an
educational repository aimed at technically literate generalists — the counterpart,
for this thread, of what *Designing Freedom* is for Beer in [READING.md](../READING.md).

### Gershenson (2015) — Requisite Variety, Autopoiesis, and Self-Organization

Carlos Gershenson. "Requisite Variety, Autopoiesis, and Self-organization."
*Kybernetes* **44**(6–7):866–873 (2015). arXiv:
[1409.7475](https://arxiv.org/abs/1409.7475).

Reframes requisite variety from a regulation *bound* into an active *design
objective*. Gershenson links Ashby's law to Maturana and Varela's autopoiesis by
defining a system's degree of "living-ness" as the ratio between its own complexity
and its environment's complexity, and argues that self-organisation is a design
principle for driving that ratio upward toward requisite variety — yielding more
adaptive and robust technology. For this repository the move is significant: it
carries Ashby toward *viability*, sitting directly adjacent to Beer's concerns in
[03](03-viable-system-model.md), and it turns the law from something you check into
something you *engineer toward*. Published as a *Kybernetes* keynote paper, it is a
well-placed refereed anchor for the guide's transition from Ashby's inequality to
the viable-systems view — the conceptual hinge between [02](02-ashbys-law.md) and
[03](03-viable-system-model.md).

### Gershenson & Fernández (2012) — Complexity and Information: Measuring Emergence, Self-Organization, and Homeostasis at Multiple Scales

Carlos Gershenson and Nelson Fernández. "Complexity and Information: Measuring
Emergence, Self-organization, and Homeostasis at Multiple Scales." *Complexity*
**18**(2):29–44 (2012). arXiv:
[1205.2026](https://arxiv.org/abs/1205.2026).

Proposes concrete information-theoretic measures for exactly the notions Ashby and
Beer treat qualitatively: *emergence* as the information a system produces,
*self-organisation* as its complement, *complexity* as the balance between the two,
and *homeostasis* as a measure of stability — all computable at multiple scales and
demonstrated on random Boolean networks and elementary cellular automata. This lets
"how much variety/complexity does this regulator actually have?" be measured rather
than merely asserted, and its multi-scale framing connects it to the Bar-Yam line
above. The *homeostasis* measure speaks straight to the essential-variable /
regulation picture the repository is built on ([01](01-foundations.md)): it offers
a quantitative handle on whether a system is in fact holding its essential variables
steady, the very thing the block diagram asks but the classical theory leaves
unmeasured.

---

## (e) Organisational and VSM applications

Beer's Viable System Model ([03](03-viable-system-model.md)) claims that any viable
organisation must, at every level of recursion, absorb variety through five
specific functions, and that a missing variety-absorbing channel resurfaces as loss
of control. These two refereed studies put that claim to work as a live diagnostic
and as a design method — the empirical counterpart to the theory in
[03](03-viable-system-model.md)–[05](05-variety-engineering.md).

### Akmal, Podgorodnichenko, Gauld & Stokes (2023) — New Zealand Pae Ora Healthcare Reforms 2022: Viable by Design?

Adeel Akmal, Nataliya Podgorodnichenko, Robin Gauld and Tim Stokes. "New Zealand
Pae Ora Healthcare Reforms 2022: Viable by Design? A Qualitative Study Using the
Viable System Model." *International Journal of Health Policy and Management* (2023).
DOI: [10.34172/ijhpm.2023.7906](https://doi.org/10.34172/ijhpm.2023.7906).

Uses the VSM as a diagnostic lens on New Zealand's 2022 Pae Ora health reforms,
drawing on 28 manager interviews and over 300 documents. Despite a strong
structural and governance design, the study finds gaps in **System 2** coordination,
in resource planning, and in the performance-measurement channels — gaps it argues
threaten the reforms' long-term viability and their equity objectives. This is a
recent, refereed, large-scale application demonstrating the VSM as an *evaluative
instrument* on real institutional reform, not a toy example. It concretely
illustrates the repository's core structural claim ([03](03-viable-system-model.md),
[06](06-modern-extensions.md)): missing variety-absorbing channels do not disappear;
they reappear as loss of control, and the VSM is precise enough to say *which*
channel is under-provisioned before the failure is obvious.

### Arghand, Alborzi & Ghatari (2022) — A Methodology for IT Governance by Viable System Modeling

Ali Akbar Arghand, Mahmood Alborzi and Ali Rajabzadeh Ghatari. "A Methodology for
IT Governance by Viable System Modeling (VSM): an Action Research in Designing a
Data Center." *Systemic Practice and Action Research* **35**(2):131–152 (2022).
DOI: [10.1007/s11213-021-09559-8](https://doi.org/10.1007/s11213-021-09559-8).

Develops a VSM-based methodology — customised from Espejo's VIPLAN method — for
diagnosing and *designing* IT governance so that business strategy stays
dynamically aligned with IT-delivered value, and validates it through action
research implementing a real data centre in an Iranian private-sector organisation.
This is the closest paper in the set to the repository's software / SRE /
enterprise-architecture framing ([06 §2](06-modern-extensions.md)): a modern,
refereed application of the VSM and its recursive variety logic to designing and
governing a technology organisation and its infrastructure. It shows Beer's model
operationalised as an actual design methodology rather than only an analytic frame —
the practical bookend to the variety-engineering craft laid out in
[05](05-variety-engineering.md).

---

## (f) The AI era

The most recent thread brings Ashby's law and the good-regulator theorem out of
the systems-theory seminar and into the active debate about AI oversight, agent
governance, and loss of control. What these papers share is a refusal to treat
"requisite variety" as a slogan: each tries to make it a load-bearing, sometimes
checkable, part of how we reason about regulating capable AI systems — and several
speak directly to the open problems left dangling in [06](06-modern-extensions.md).

### Chin, Chiodo, Müller & Snell (2026) — Reframing AI Loss of Control

Ze Shen Chin, Maurice Chiodo, Dennis Müller and Coleman Snell. "Reframing AI Loss
of Control: What It Is, How to Have It, How to Lose It." arXiv:
[2606.12442](https://arxiv.org/abs/2606.12442) (2026).

The clearest recent attempt to make requisite variety a structural part of the
AI-safety vocabulary. Chin and colleagues argue that public debate about AI "loss
of control" rests on an undefined notion of control, and rebuild the concept from
cybernetics, management control, and control theory: control means the *setting and
getting of goals*, and it requires a working control loop, sufficient goal
alignment, and — named explicitly as a precondition — **requisite variety in the
regulator**. They show that loss of control can occur well below superintelligence
and already happens today. For the repository this is the rigorous bridge from the
classical regulation picture to contemporary loss-of-control discourse, and it
supplies a compact checklist (control loop + variety + alignment) that
operationalises "only variety can destroy variety" for AI systems and institutions —
the sharpest external validation of the [06 §1](06-modern-extensions.md) argument
that a fixed rulebook cannot regulate an open-ended optimiser.

### Cody, Shadab, Salado & Beling (2022) — Core and Periphery as Closed-System Precepts for Engineering General Intelligence

Tyler Cody, Niloofar Shadab, Alejandro Salado and Peter Beling. "Core and Periphery
as Closed-System Precepts for Engineering General Intelligence." *AGI-22 (15th
Conference on Artificial General Intelligence)*. arXiv:
[2208.02837](https://arxiv.org/abs/2208.02837) (2022).

Confronts head-on the wrinkle that makes naïve variety accounting fail for agents.
Cody and colleagues contend that AI systems break the classical engineering
assumption of independent, composable components because they act on their
environment and, through it, on themselves — so their inputs are *not* independent
of their outputs. Using abstract systems theory and the Law of Requisite Variety,
they propose "core" and "periphery" precepts for reasoning about how to regulate an
AI's outcomes toward stakeholder goals. This ports Ashby from a clean
regulator-versus-disturbance frame into the closed-loop, self-influencing character
of embodied and agentic AI — precisely the coupling that [06's open
problems](06-modern-extensions.md#open-problems) flag as breaking the tidy
disturbance-column / regulator-row table. It offers a principled way to talk about
*which part* of a system must carry the regulating variety when the system partly
creates its own inputs.

### Shadab, Cody, Salado, Topcu, Shadab & Beling (2025) — Exploring Core and Periphery Precepts in Biological and Artificial Intelligence

Niloofar Shadab, Tyler Cody, Alejandro Salado, Taylan G. Topcu, Mohammad Shadab and
Peter Beling. "Exploring Core and Periphery Precepts in Biological and Artificial
Intelligence: An Outcome-Based Perspective." arXiv:
[2507.04594](https://arxiv.org/abs/2507.04594) (2025).

The empirical follow-through on the 2022 core/periphery theory. This paper gives the
framework mathematical and empirical grounding, formally distinguishing
*core-dominant* from *periphery-dominant* systems and demonstrating the distinction
across both biological and artificial intelligence examples, arguing that these
Ashby-rooted abstractions have concrete, testable applicability rather than staying
purely conceptual. For an educational repository it pairs naturally with the 2022
paper: together they show how the Law of Requisite Variety can be turned into an
analytic *instrument* for classifying where a scaling intelligence concentrates its
regulating variety — a worked example of the "state the theorem, then make it
measurable" progression this repository favours.

### Janssen (2026) — From Runtime Records to Legal Findings

Jeroen Janssen. "From Runtime Records to Legal Findings: An Evidentiary-Adequacy
Criterion for Agentic AI Oversight." arXiv:
[2607.00941](https://arxiv.org/abs/2607.00941) (2026; technical report).

Brings Ashby's law and Conant & Ashby directly into AI governance and the human-
oversight obligations of regimes like the EU AI Act. Janssen defines a *necessity
criterion* for when an agentic AI system's runtime logs can actually support
legally operative oversight findings — did protected data cross a boundary, could a
human intervene, was delegated authority valid — namely that the record must carry
both a *typing* to the legal category and the *specific relation* the determination
depends on. Tamper-proof logs and generic provenance alone are shown to be
insufficient, and the argument is tied explicitly to requisite variety and the good
regulator theorem. The framing is that an auditor's or regulator's records need
requisite variety to distinguish the states that matter legally: **an under-varied
logging system cannot regulate an over-varied agent**. This is a concrete, current
application of the repository's good-regulator material ([02 §6](02-ashbys-law.md))
to real oversight infrastructure, and a direct instance of the
"model / distinguish the right states" reading of Conant & Ashby.

### Wu, Liu & Shu (2026) — CyberCorrect: A Cybernetic Framework for Closed-Loop Self-Correction in Large Language Models

Yuning Wu, Yingmin Liu and Yang Shu. "CyberCorrect: A Cybernetic Framework for
Closed-Loop Self-Correction in Large Language Models." arXiv:
[2605.17305](https://arxiv.org/abs/2605.17305) (2026; submitted to IEEE SMC 2026).

Reframes ad-hoc LLM self-correction as a genuine closed-loop control system in
cybernetic terms: the generator is the *plant*, a tri-modal error detector is the
*sensor*, a type-directed controller issues targeted repairs, and a convergence
judge decides when to stop — evaluated with control-theoretic metrics such as
convergence, overshoot, and oscillation. It reports higher final accuracy and
substantially less erroneous over-correction than prior prompting-based methods.
For this repository it is a working instantiation of cybernetic regulation applied
*inside a single model's reasoning loop*, making the sensor / controller / feedback
machinery of [01](01-foundations.md) concrete for LLMs. Its measured overshoot and
oscillation are the empirical face of a familiar warning: when the regulator is
mistuned relative to the plant it governs, a control loop does not just
under-correct, it rings — the dynamical failure mode that the static variety
inequality cannot see (another entry in the [06](06-modern-extensions.md) list of
where latency and dynamics escape Ashby's count).

### Wu & Or (2025) — Towards Open Complex Human-AI Agents Collaboration Systems

Ju Wu and Calvin K. L. Or. "Position Paper: Towards Open Complex Human-AI Agents
Collaboration Systems for Problem Solving and Knowledge Management." arXiv:
[2505.00018](https://arxiv.org/abs/2505.00018) (2025; position paper).

A substantive cybernetic treatment of human-AI teaming and multi-agent supervision.
Wu and Or propose a framework that synthesises a boundary-centric ontology of
agenthood with cybernetics (and Pask's Conversation Theory), using a Petri-net
formalism and a three-level meta / agent / execution orchestration to budget
initiative, gate which knowledge is promoted from provisional to validated, and
keep humans central to setting aims under audited governance. This is close in
spirit to the repository's mapping of supervisor / subagent stacks onto the VSM
([06 §1](06-modern-extensions.md)): it supplies vocabulary and structure for the
*metasystem* role ([04](04-metalanguage-metasystems.md)) that a human or
orchestrator must play to supply the regulating variety individual agents cannot
supply for themselves — coordination, resource control, planning, and identity in
Beer's terms, here recast for mixed human-AI teams.

---

## Open research questions

The frontier has sharpened a great deal of Ashby, but it has not closed it. The
gaps below are where the current literature is thinnest — and several are the same
gaps the [06 open problems](06-modern-extensions.md#open-problems) raise, now
located against the specific papers that bear on them.

1. **From rate theorems to open-ended agents.** The data-rate theorems
   (Tatikonda & Mitter; Nair & Evans) give an exact *rate* form of requisite
   variety — bits per unit time — but only for linear plants with well-defined
   unstable eigenvalues. There is no comparable rate theorem for open-ended
   optimisers or adversarial disturbance sources, which is exactly the regime the
   AI-era papers care about. What plays the role of `Σ log|λᵢ|` when the plant is a
   learning agent that reshapes its own dynamics?

2. **Is the good-regulator "model" intrinsic or observer-relative?** The Watt-governor
   critique (Baltieri et al.) and the embodied-agent re-derivation (Virgo et al.)
   agree that a model can be *read into* a regulator by an interpreter — and the
   Bayesian bridge (Baltieri et al. 2025) proves the internal model principle is a
   special case of Bayesian filtering. But if any successful regulator can be
   described as modelling, the theorem's *empirical* content thins. When does
   "contains a model" say something falsifiable about the mechanism rather than
   about the describer? This is the good-regulator paradox from [06](06-modern-extensions.md)
   in its precise, current form.

3. **Multi-scale variety as an operational audit.** Siegenfeld & Bar-Yam turn
   Ashby's scalar into a scale-indexed spectrum, and the pairwise profile
   (Bar-Yam et al.) makes it computable in principle — but no one has yet run a
   full complexity-profile audit of a real regulator (an SRE org, an agent stack, a
   moderation system) to locate the scale at which it is under-varied *before* the
   failure. Bridging the formal multi-scale law to a working diagnostic is open, and
   it is the natural next step for this repository's own simulations.

4. **A conservation law for variety?** Beer's intuition that suppressed variety
   reappears elsewhere ([06 open problems](06-modern-extensions.md#open-problems))
   has its closest formal cousin in the complexity-profile *sum rules* (the
   conservation of degrees of freedom in Bar-Yam et al. and Siegenfeld & Bar-Yam).
   Whether those sum rules are the genuine "conservation of variety" Beer gestured
   at — or a different quantity that merely rhymes with it — is unresolved.

5. **Empowerment versus its rivals as the "right" capability measure.** Empowerment
   (Klyubin et al.; Salge et al.) gives a computable, agent-centric reading of
   variety-as-capability, and Mohamed & Rezende scale it — but Chen & Prokopenko
   show it is one of several competing intrinsic utilities, and thermodynamic
   efficiency, not empowerment, is what peaks at criticality. Which measure, if any,
   is the correct generalisation of "the regulator's usable variety" for a given
   class of agents remains genuinely open.

6. **A theory of amplification with numbers.** Beer's "amplify the regulator,
   attenuate the disturbance" ([05](05-variety-engineering.md)) is still a design
   heuristic without a general account of *how much* a given mechanism buys. The
   control-capacity result (Ranade & Sahai) is the closest thing to a bit-valued
   theory of an actuator's amplification — but only for scalar memoryless channels.
   A general theory of amplification, including when an amplifier becomes a new
   disturbance source, is not yet in hand.

Read together, these papers show that requisite variety was not a dead end or a mere
slogan: over seventy years, piece after piece of it has been made exact — as a
thermodynamic limit, a communication rate, a Bayesian filter, a computable agent
drive, a scale-indexed spectrum, and a governance criterion. What remains open is
mostly the *unification* — a single account that holds when the regulator and the
regulated are coupled, adaptive, and multi-scale all at once. That is the frontier.

---

## Sources

The papers annotated above, grouped by thread. Each is also listed with its link in
the [Research papers](../READING.md#research-papers) section of the reading list.

**Information-theoretic sharpenings**

- Touchette, H., & Lloyd, S. "Information-Theoretic Limits of Control." *Phys. Rev. Lett.* 84, 1156 (2000). arXiv:chao-dyn/9905039.
- Sagawa, T., & Ueda, M. "Second Law of Thermodynamics with Discrete Quantum Feedback Control." *Phys. Rev. Lett.* 100, 080403 (2008). arXiv:0710.0956.
- Sagawa, T., & Ueda, M. "Generalized Jarzynski Equality under Nonequilibrium Feedback Control." *Phys. Rev. Lett.* 104, 090602 (2010). arXiv:0907.4914.
- Tatikonda, S., & Mitter, S. "Control Under Communication Constraints." *IEEE Trans. Automat. Contr.* 49(7):1056–1068 (2004). DOI:10.1109/TAC.2004.831187.
- Nair, G. N., & Evans, R. J. "Stabilizability of Stochastic Linear Systems with Finite Feedback Data Rates." *SIAM J. Control Optim.* 43(2):413–436 (2004). DOI:10.1137/S0363012902402116.
- Ranade, G., & Sahai, A. "Control Capacity." arXiv:1701.04187 (2017).
- Kostina, V., & Hassibi, B. "Rate-Cost Tradeoffs in Control." *IEEE Trans. Automat. Contr.* (2019). arXiv:1612.02126.

**The good regulator's descendants**

- Francis, B. A., & Wonham, W. M. "The Internal Model Principle of Control Theory." *Automatica* 12(5):457–465 (1976). DOI:10.1016/0005-1098(76)90006-6.
- Buckley, C. L., Kim, C. S., McGregor, S., & Seth, A. K. "The Free Energy Principle for Action and Perception: A Mathematical Review." arXiv:1705.09156 (2017).
- Millidge, B., Seth, A., & Buckley, C. L. "A Mathematical Walkthrough and Discussion of the Free Energy Principle." arXiv:2108.13343 (2021).
- Baltieri, M., Buckley, C. L., & Bruineberg, J. "Predictions in the Eye of the Beholder: an Active Inference Account of Watt Governors." ALIFE 2020. arXiv:2006.11495.
- Virgo, N., Biehl, M., Baltieri, M., & Capucci, M. "A 'Good Regulator Theorem' for Embodied Agents." ALIFE 2025. arXiv:2508.06326.
- Baltieri, M., Biehl, M., Capucci, M., & Virgo, N. "A Bayesian Interpretation of the Internal Model Principle." arXiv:2503.00511 (2025).
- Weinstein, V. K., Alshammari, T., Timperi, K. G., Bennis, M., & LaValle, S. M. "An Internal Model Principle for Robots." arXiv:2406.11237 (2024).

**Variety as agent capability — empowerment**

- Klyubin, A. S., Polani, D., & Nehaniv, C. L. "All Else Being Equal Be Empowered." ECAL 2005, LNCS 3630:744–753. DOI:10.1007/11553090_75.
- Salge, C., Glackin, C., & Polani, D. "Empowerment — an Introduction." In *Guided Self-Organization: Inception* (Springer, 2014). arXiv:1310.1863.
- Mohamed, S., & Rezende, D. J. "Variational Information Maximisation for Intrinsically Motivated Reinforcement Learning." NeurIPS 2015. arXiv:1509.08731.
- Rosas, F. E., Mediano, P. A. M., Biehl, M., Chandaria, S., & Polani, D. "Causal Blankets: Theory and Algorithmic Framework." arXiv:2008.12568 (2020).
- Chen, Q., & Prokopenko, M. "Why Collective Behaviours Self-Organise to Criticality." *R. Soc. Open Sci.* 12(6):241655 (2025). arXiv:2409.15668.

**Multi-scale requisite variety and measured complexity**

- Siegenfeld, A. F., & Bar-Yam, Y. "A Formal Definition of Scale-dependent Complexity and the Multi-scale Law of Requisite Variety." arXiv:2206.04896 (2022).
- Bar-Yam, Y., Harmon, D., & Bar-Yam, Y. "Computationally Tractable Pairwise Complexity Profile." *Complexity* 18(5):20–27 (2013). arXiv:1208.0823.
- Allen, B., Stacey, B. C., & Bar-Yam, Y. "An Information-Theoretic Formalism for Multiscale Structure in Complex Systems." arXiv:1409.4708 (2014).
- Siegenfeld, A. F., & Bar-Yam, Y. "An Introduction to Complex Systems Science and its Applications." *Complexity* 2020:6105872 (2020). arXiv:1912.05088.
- Gershenson, C. "Requisite Variety, Autopoiesis, and Self-organization." *Kybernetes* 44(6–7):866–873 (2015). arXiv:1409.7475.
- Gershenson, C., & Fernández, N. "Complexity and Information: Measuring Emergence, Self-organization, and Homeostasis at Multiple Scales." *Complexity* 18(2):29–44 (2012). arXiv:1205.2026.

**Organisational and VSM applications**

- Akmal, A., Podgorodnichenko, N., Gauld, R., & Stokes, T. "New Zealand Pae Ora Healthcare Reforms 2022: Viable by Design? A Qualitative Study Using the Viable System Model." *Int. J. Health Policy Manag.* (2023). DOI:10.34172/ijhpm.2023.7906.
- Arghand, A. A., Alborzi, M., & Ghatari, A. R. "A Methodology for IT Governance by Viable System Modeling (VSM): an Action Research in Designing a Data Center." *Syst. Pract. Action Res.* 35(2):131–152 (2022). DOI:10.1007/s11213-021-09559-8.

**The AI era**

- Chin, Z. S., Chiodo, M., Müller, D., & Snell, C. "Reframing AI Loss of Control: What It Is, How to Have It, How to Lose It." arXiv:2606.12442 (2026).
- Cody, T., Shadab, N., Salado, A., & Beling, P. "Core and Periphery as Closed-System Precepts for Engineering General Intelligence." AGI-22. arXiv:2208.02837 (2022).
- Shadab, N., Cody, T., Salado, A., Topcu, T. G., Shadab, M., & Beling, P. "Exploring Core and Periphery Precepts in Biological and Artificial Intelligence: An Outcome-Based Perspective." arXiv:2507.04594 (2025).
- Janssen, J. "From Runtime Records to Legal Findings: An Evidentiary-Adequacy Criterion for Agentic AI Oversight." arXiv:2607.00941 (2026).
- Wu, Y., Liu, Y., & Shu, Y. "CyberCorrect: A Cybernetic Framework for Closed-Loop Self-Correction in Large Language Models." arXiv:2605.17305 (2026).
- Wu, J., & Or, C. K. L. "Position Paper: Towards Open Complex Human-AI Agents Collaboration Systems for Problem Solving and Knowledge Management." arXiv:2505.00018 (2025).

---

> Previous: [06 — Modern Extensions](06-modern-extensions.md) · Back to [README](../README.md)
