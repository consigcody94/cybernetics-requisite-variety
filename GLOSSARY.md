# Glossary

Precise working definitions for the terms used throughout this repository. Entries are
alphabetical and cross-referenced. Where a term is contested or used loosely in the
literature, the entry says so.

A note on sources: most Ashby terms are defined operationally in *An Introduction to
Cybernetics* (1956); most Beer terms are defined in *The Heart of Enterprise* (1979) and
*Diagnosing the System for Organizations* (1985). Full citations at the end.

---

### Algedonic signal

In Beer's Viable System Model, an alarm that bypasses the normal management hierarchy and
travels directly to the top ([System 5](#system-5-policy)) when an operational unit is in
serious trouble — from the Greek *algos* (pain) and *hedos* (pleasure). Algedonic channels
exist because routine reporting chains [attenuate](#attenuator) variety and can filter out
exactly the news that most needs to arrive quickly. *See also:* [Viable System
Model](#viable-system-model-vsm), [Metasystem](#metasystem).

### Amplifier

Any device or arrangement that increases the [variety](#variety) a
[regulator](#regulator) can deploy against its environment: delegation, standardization,
training, automation, published rules that let one decision govern many cases. Amplifiers
and [attenuators](#attenuator) are the two levers of [variety
engineering](#variety-engineering); Beer's design injunction is that they should be
designed deliberately rather than left to emerge by accident.

### Attenuator

Any device or arrangement that reduces the variety reaching a low-variety receiver from a
high-variety source: aggregation, sampling, exception reporting, categories, dashboards,
delegation of decisions downward. Attenuation is unavoidable — a manager cannot absorb the
full state of an operation — so the design question is *which* variety gets filtered out,
not whether filtering happens. *See also:* [Amplifier](#amplifier), [Variety
engineering](#variety-engineering), [Transducer](#transducer).

### Autonomy

In the VSM, the freedom of an operational unit ([System 1](#system-1-operations)) to
absorb its own environmental variety locally, constrained only as much as systemic
cohesion strictly requires. Beer treats autonomy not as a political concession but as a
computational necessity: the [metasystem](#metasystem) lacks the
[requisite variety](#law-of-requisite-variety) to run the operations itself. *See also:*
[Recursion](#recursion).

### Black box

A system investigated solely through the relation between its inputs and outputs, with no
access to (or no use made of) its internal mechanism. Ashby made black-box study a
methodological centerpiece of cybernetics: many useful regulators, and all everyday
dealings with complex systems, work this way. *See also:* [Model](#model),
[POSIWID](#posiwid).

### Channel capacity

The maximum rate at which a communication channel can transmit distinguishable states,
in the sense of Shannon's information theory. It matters for regulation because a
regulator's effective variety is capped by the capacity of the channels connecting it to
what it regulates — a perfect controller behind a narrow channel is not a perfect
controller. *See also:* [Law of requisite variety](#law-of-requisite-variety),
[Transducer](#transducer).

### Constraint

A relation between two sets whereby the variety that actually occurs is less than the
variety that could conceivably occur. For Ashby, constraint is what makes prediction,
science, and regulation possible at all: an unconstrained world would admit no learning.
Exploiting constraint in the disturbances is the regulator's cheapest source of leverage.
*See also:* [Variety](#variety), [Model](#model).

### Cybernetics

The study of communication, control, and regulation in animals, machines, and
organizations — Wiener's 1948 coinage, from the Greek *kybernetes* (steersman). Its
distinguishing move is to abstract away from what a system is made of and attend to how
it is organized: feedback, information flow, and stability. *See also:* [Second-order
cybernetics](#second-order-cybernetics), [Feedback](#feedback).

### Disturbance

Anything that would drive a system's [essential variables](#essential-variables) outside
their acceptable limits if left uncorrected. In Ashby's regulation schema, disturbances
D act on the system through a table of outcomes, and the regulator R chooses responses so
that the outcome stays in the goal set. *See also:* [Regulator](#regulator), [Law of
requisite variety](#law-of-requisite-variety).

### Entropy

In the information-theoretic sense used here: a measure of the uncertainty of a source,
maximal when all states are equally likely. When [variety](#variety) is measured
logarithmically over a probability distribution, it *is* Shannon entropy, and the Law of
Requisite Variety can be stated as an inequality among entropies. *See also:*
[Negentropy](#negentropy).

### Environment

For a given system, everything outside its boundary that it interacts with — the
proximate source of most [disturbances](#disturbance) and the ultimate object of most
regulation. In the VSM each operational unit faces its own local environment, which is
embedded in the larger environment faced by the whole; the environment's variety always
vastly exceeds the organization's. *See also:* [Variety engineering](#variety-engineering).

### Essential variables

The variables that must be kept within physiological (or organizational) limits for a
system to survive: blood pH and body temperature for an animal, cash flow and legal
standing for a firm. Ashby defines adaptation itself in terms of keeping essential
variables within limits, which makes them the anchor of every regulation problem.
*See also:* [Homeostasis](#homeostasis), [Ultrastability](#ultrastability),
[Viability](#viability).

### Feedback

The return of information about a system's output to influence its subsequent input.
Negative feedback opposes deviation from a reference and is the basic mechanism of
stability; positive feedback reinforces deviation and produces growth or runaway. The
term is often used loosely; in cybernetics it names a closed causal loop, not merely
"a response."

### Good regulator theorem

Conant and Ashby's 1970 result, usually summarized as: every good regulator of a system
must be a model of that system. Formally, under their assumptions (an optimal, maximally
simple regulator minimizing outcome entropy), the regulator's behavior must be a mapping
(a homomorphic image) of the behavior of the system regulated. Honest caveat: the theorem
is proved for a specific formal setup, and how far its slogan generalizes — especially to
[error-controlled feedback](#feedback) regulators that react after the fact — is debated
in the literature. *See also:* [Model](#model), [Regulator](#regulator).

### Homeostasis

The maintenance of [essential variables](#essential-variables) within survivable limits
despite disturbance — Walter Cannon's physiological term, generalized by cybernetics to
any system. Homeostasis is the *goal* of regulation; the Law of Requisite Variety states
the price of achieving it. *See also:* [Homeostat](#homeostat).

### Homeostat

Ashby's 1948 electromechanical device: four interacting units whose configuration was
randomly re-selected (via stepping switches) whenever an essential variable left its
limits, continuing until a stable configuration was found. It demonstrated
[ultrastability](#ultrastability) — adaptation by second-order change of the system's own
parameters — in hardware, and is the centerpiece of *Design for a Brain*.

### Law of requisite variety

Ashby's central theorem: the variety in outcomes cannot be forced below the variety in
disturbances minus the variety available to the regulator (measured logarithmically:
H(O) ≥ H(D) − H(R), ignoring channel noise). Equivalently, a regulator can hold outcomes
within a goal set only if it can deploy at least as much variety as the disturbances it
must counter — in Ashby's words, "only variety can destroy variety." The law is a
counting/information-theoretic constraint, not an empirical generalization; it bounds
what any regulator *could* do, saying nothing about how to build one. *See also:*
[Variety](#variety), [Regulator](#regulator), [Variety
engineering](#variety-engineering).

### Metasystem

In Beer's usage, the ensemble of Systems [3](#system-3-integration),
[4](#system-4-intelligence), and [5](#system-5-policy) considered as the management that
is logically *over and above* the operational units — not because it is more powerful,
but because it handles a class of problems (cohesion, adaptation, identity) that the
operational level cannot even formulate. A metasystem speaks a metalanguage: it resolves
questions that are undecidable in the language of the level below. *See also:*
[Recursion](#recursion), [Viable System Model](#viable-system-model-vsm).

### Model

A system whose states and transitions map, at some chosen level of abstraction, onto
those of another system (technically a homomorphism — a many-to-one, structure-preserving
mapping). Per the [good regulator theorem](#good-regulator-theorem), effective regulation
implies possession of such a mapping, explicit or implicit; per the black-box method, the
model need capture only input–output structure, not mechanism. *See also:* [Black
box](#black-box), [Constraint](#constraint).

### Negentropy

"Negative entropy": order or improbability of state, the quantity an organism imports
(Schrödinger's phrase) to stave off thermodynamic decay, linked to information by
Brillouin. Caveat: the term is used informally and sometimes sloppily in the cybernetics
literature; the rigorous content is carried by [entropy](#entropy) and information
proper, and thermodynamic and informational entropy should not be casually equated.

### POSIWID

Beer's acronym for his dictum "the purpose of a system is what it does" — a diagnostic
stance, not a metaphysical claim. It instructs the analyst to infer purpose from
observed, repeated behavior rather than from stated intentions, mission statements, or
design documents; if a system reliably produces an outcome, treat that outcome as its
de facto purpose when diagnosing it. *See also:* [Black box](#black-box).

### Recursion

The structural principle of the VSM: every viable system contains viable systems and is
contained in one, and the *same* five-system organization recurs at every level (team,
plant, division, corporation, industry). Recursion is Beer's answer to overwhelming
variety — each level absorbs the variety it can, so no level needs a model of everything.
*See also:* [Autonomy](#autonomy), [Viable System Model](#viable-system-model-vsm).

### Redundancy of potential command

Warren McCulloch's principle, adopted by Beer: in a well-organized network, command
passes to wherever the relevant information is, rather than residing permanently at a
fixed apex. It underwrites the VSM's insistence that authority follows information, and
its skepticism of rigid org-chart hierarchy.

### Regulator

Any subsystem whose activity keeps another system's [essential
variables](#essential-variables) within limits despite [disturbance](#disturbance) — a
thermostat, an immune system, a management team. Ashby distinguishes cause-controlled
regulation (acting on the disturbance before it lands) from error-controlled regulation
(acting on the deviation after it appears), the latter being necessarily imperfect since
it works only after some error has occurred. *See also:* [Law of requisite
variety](#law-of-requisite-variety), [Good regulator theorem](#good-regulator-theorem).

### Second-order cybernetics

The cybernetics of observing systems, associated with Heinz von Foerster and others from
the late 1960s onward: it includes the observer — with their purposes and distinctions —
inside the system being studied, rather than assuming a detached spectator. It matters
here because [variety](#variety) is observer-relative: what counts as a distinguishable
state depends on who is distinguishing and why. Caveat: "second-order" is a research
orientation more than a formal theory, and its claims range from the rigorous to the
frankly philosophical.

### Self-organization

The emergence of ordered, coordinated behavior in a system without an external designer
imposing it, as when the [homeostat](#homeostat) finds stability by internal
re-configuration. Ashby noted a sharpened caveat that is often forgotten: strictly, a
system cannot change its own organization without some part standing outside the part
being changed, so claims of self-organization always deserve scrutiny about where the
selecting is actually done.

### State-determined system

Ashby's idealization: a system whose next state is fixed by its present state (a
deterministic dynamical system, in modern terms). *Design for a Brain* builds its whole
account of adaptation on such systems, then adds stochastic step-mechanisms on top; the
idealization is what makes the analysis tractable, and real systems fit it only
approximately.

### System 1 (Operations)

In the VSM, the collection of operational units that do what the organization exists to
do — make the product, treat the patients, teach the students. Each System 1 unit is
itself a viable system at the next [recursion](#recursion) down, with its own management
and its own local environment. *See also:* [Autonomy](#autonomy).

### System 2 (Coordination)

The anti-oscillation function: shared standards, schedules, protocols, and conventions
that damp conflicts between System 1 units without invoking managerial authority — the
timetable rather than the boss. Its absence shows up as units fighting over shared
resources and as chronic firefighting escalated upward unnecessarily.

### System 3 (Integration)

The "inside and now" management function: it allocates resources among the System 1
units, holds them accountable, and optimizes the synergy of the whole operational
complex. System 3 works mainly through the resource bargain — negotiated autonomy in
exchange for accountability — rather than through detailed command. *See also:* [System
3* (Audit)](#system-3-audit), [Metasystem](#metasystem).

### System 3* (Audit)

A sporadic, direct channel by which System 3 samples the state of operations without
going through System 1 management: audits, spot inspections, walking the floor,
climate surveys. It exists to correct for the variety lost in routine reporting — a
deliberate check on the [attenuators](#attenuator) built into the hierarchy.

### System 4 (Intelligence)

The "outside and then" function: scanning the environment, modeling the future, and
proposing adaptation — R&D, strategy, market intelligence. Beer insisted System 4 must be
in continuous, structured conversation with System 3, since adaptation proposals are
worthless if disconnected from what operations can actually absorb.

### System 5 (Policy)

The identity and closure function: it defines what the organization *is*, sets the ethos
within which 3 and 4 debate, and arbitrates when they deadlock. In Beer's diagnosis,
pathology arises when System 5 collapses into System 3 (management by looking inward
only) or floats free of the 3–4 conversation entirely. *See also:* [Algedonic
signal](#algedonic-signal).

### Team Syntegrity

Beer's later (1990s) protocol for non-hierarchical group deliberation, arranging thirty
participants as the edges of an icosahedron so that discussion topics interlock and
influence reverberates symmetrically through the group. It applies variety-engineering
ideas to meetings; it is best regarded as a designed protocol with practitioner support
rather than a theorem-backed method.

### Transducer

Anything that carries information across a boundary while changing its form: a sensor, a
report, a translation, a survey instrument. Every channel in the VSM needs transducers at
both ends, and Beer's rule is that a transducer must itself have the
[variety](#variety) of the channel it serves — a clumsy form or an untrained interviewer
destroys variety that the channel was built to carry.

### Ultrastability

Ashby's term for a two-level architecture of adaptation: ordinary feedback keeps the
system stable against expected disturbances, and when that fails — when [essential
variables](#essential-variables) breach their limits — a second mechanism changes the
system's own parameters (by selection, often random) until stability is regained. It is
his core model of how a system can adapt to disturbances its designer never foresaw.
*See also:* [Homeostat](#homeostat).

### Variety

The number of distinguishable states of a system, or of distinguishable elements of a
set — often taken logarithmically, in bits, so that varieties of independent parts add.
Crucially, variety is relative to an observer's purpose and powers of discrimination:
a box of resistors has one variety for the accountant and another for the engineer.
*See also:* [Constraint](#constraint), [Entropy](#entropy), [Law of requisite
variety](#law-of-requisite-variety).

### Variety engineering

Beer's name for the design discipline that follows from Ashby's law: since environmental
variety always exceeds managerial variety, the residual variety must be handled by
deliberately designed [attenuators](#attenuator) and [amplifiers](#amplifier) on every
channel, balanced so that each pair of connected systems can match varieties at their
interface. Left undesigned, attenuation and amplification still happen — but
accidentally, and usually badly.

### Viability

The capacity of a system to maintain a separate existence — to survive, adapt, and keep
its identity in a changing environment — over a timescale long relative to its
transactions. Viability is the criterion the VSM is built to satisfy: Beer's claim is
that the five-system architecture is *necessary and sufficient* for it, a strong claim
that should be read as a well-argued engineering thesis rather than a proven theorem.
*See also:* [Essential variables](#essential-variables).

### Viable System Model (VSM)

Beer's model of any organization capable of independent existence: five interlocking
functions ([Systems 1–5](#system-1-operations)) plus [algedonic](#algedonic-signal)
alarms, embedded in a [recursive](#recursion) structure and connected by channels sized
according to [variety engineering](#variety-engineering). Developed across *Brain of the
Firm* (1972), *The Heart of Enterprise* (1979), and *Diagnosing the System* (1985), it is
offered both as a diagnostic lens for existing organizations and as a design template for
new ones. *See also:* [Metasystem](#metasystem), [Viability](#viability).

---

## Sources

- W. Ross Ashby, *Design for a Brain*, 1952 (2nd ed. 1960).
- W. Ross Ashby, *An Introduction to Cybernetics*, 1956.
- Roger C. Conant and W. Ross Ashby, "Every good regulator of a system must be a model of
  that system," *International Journal of Systems Science*, 1970.
- Norbert Wiener, *Cybernetics: or Control and Communication in the Animal and the
  Machine*, 1948.
- Claude E. Shannon and Warren Weaver, *The Mathematical Theory of Communication*, 1949.
- Walter B. Cannon, *The Wisdom of the Body*, 1932.
- Erwin Schrödinger, *What is Life?*, 1944.
- Stafford Beer, *Cybernetics and Management*, 1959.
- Stafford Beer, *Brain of the Firm*, 1972 (2nd ed. 1981).
- Stafford Beer, *Designing Freedom*, 1974.
- Stafford Beer, *The Heart of Enterprise*, 1979.
- Stafford Beer, *Diagnosing the System for Organizations*, 1985.
- Stafford Beer, *Beyond Dispute: The Invention of Team Syntegrity*, 1994.
- Heinz von Foerster, *Understanding Understanding: Essays on Cybernetics and Cognition*,
  2003.
