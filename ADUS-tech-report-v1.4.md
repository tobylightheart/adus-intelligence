# **ADUS Framework – Technical Report (v1.4)**

## **Plain-language summary**

Intelligence is not one thing that a person or an AI simply has more or less
of. ADUS separates it into four interacting parts: **abilities** set what can be
learned, **dispositions** supply motives and habits, **understandings** store
what has been grasped, and **skills** put it into action. The pianist who can
play a chord but cannot explain it has skill without the matching
understanding; someone who can explain the chord but cannot play it has the
reverse. This split matters because each kind of limitation calls for a
different remedy.

The framework also distinguishes effortful performance from performance that
has become automatic. It asks whether a process can be brought back into
awareness, whether it can be redirected, and whether learning survives beyond
the current episode. For present-day language models, ADUS's central diagnosis
is not simply that they need more knowledge: it is that they largely lack an
ability to consolidate new understanding and skill while they are running.

The report turns that diagnosis into measurements and nine claims that could be
shown false. Technical notation is retained because precision is the point;
plain-language explanations are layered alongside it so a reader can first see
what each distinction is for.

## **0. Changelog from v1.3**

This version separates several ideas that v1.3 treated as one, especially what
a system can learn, how automatic a process is, and how learning persists.

* **§2 level of analysis restated**: functional-primary with implementation evidence admissible, plus an explicit priority rule. Resolves a latent inconsistency between v1.3 §2 (functional only) and v1.3 §8 (architectural definition of A).
* **§3 A split into qualitative and quantitative change**, with a reachability criterion. Level 2 redefined as A-qualitative change. Capacity scaling is A-quantitative.
* **§3 consolidation added as an A sub-domain.** Consolidation capacity governs the zone-transition rate and is therefore an ability, not a rate parameter.
* **§3.1 zones redefined on the load axis alone.** A zone says how much conscious effort a process currently needs: fluent, partly effortful, or step-by-step. Plasticity removed from the zone definition and reintroduced as a channel-relative transition *rate*. Consolidation channels introduced: C-N (nothing persists), C-X (an external aid keeps it), C-T (a trainer updates the system), and C-S (the system initiates its own update).
* **§6 retest criterion now channel-indexed.** New proposed LLM load assay (constrained reasoning budget).
* **§8 revised**: A row corrected, consolidation deficit stated as an A deficit, internal simulation given a functional criterion and assay, and environment parameters (V, coverage) added as adjacent concepts.
* **§9 claim 4 reformulated** as a C-X vs C-T slope comparison. New claims 7–9.
* **Editorial**: automaticity — how independently a process runs once started, like touch-typing without choosing each key — is written consistently as Do_A(X). See §3 note.

---

## **1. Purpose**

Mechanistic, functional architecture of intelligence that bridges psychometric structures and actionable intervention for humans and artificial systems.

---

## **2. Level of Analysis**

ADUS classifies a component by what it does, while allowing implementation
details to serve as evidence about that function.

ADUS is a **functional architecture with implementation evidence admissible**. Two commitments, in priority order.

**Primary — functional.** Node identity, zone placement, and every claim in §9 are stated in terms of functional role and information flow, never in terms of substrate. This is what makes the same vocabulary applicable to biological and artificial systems, and what makes the node-identity principle (§3) enforceable.

**Secondary — implementation admissible as evidence.** Architectural facts, ablation, activation patching, and mechanistic interpretability results are admissible as evidence for a functional attribution, and as mechanism where mechanism is known. They are not admissible as definitions.

**Priority rule.** Where behavioural and implementation evidence conflict, the behavioural finding fixes the attribution and the implementation finding becomes an explanandum. A component that behaves as Zone-2 is Zone-2 even if the circuit implementing it is believed to be fixed; the belief is then what requires revision.

*Rationale.* v1.3 §2 asserted functional analysis "without committing to neural or algorithmic implementation," while v1.3 §8 defined A for artificial systems as context length, attention capacity, and parameter count — an implementation-level definition. The inconsistency was doing real work, because some attributions (internal simulation, §8) cannot be adjudicated behaviourally alone. The resolution above admits that evidence without letting it override the functional criteria, which would otherwise reopen the A↔U and A↔S conflations that §3 exists to close.

The template already present in v1.3 is the proposed Aw assay: an implementation-level intervention (ablation, patching) used to measure a functionally defined quantity (predictive validity of introspective report). That is the intended pattern throughout.

---

## **3. Component Model**

The model separates four kinds of working part, then describes the current
state of each part with three parameters.

Four continuously interacting nodes. Each carries an **automaticity parameter** Do_A( ) (how little deliberate attention it needs, like a familiar route home), an **awareness parameter** Aw( ) (how accurately the actor can inspect it, like noticing why a habit fired), and a **controllability parameter** Cn( ) (how well the actor can stop or redirect it, like withholding an automatic reply), each ranging 0–1.

| Node | Symbol | Definition | Sub-domains |
| ----- | ----- | ----- | ----- |
| **Abilities** | A | Substrate-bounded core capacities (biological or architectural) | cognitive, perceptual, motor, sensory, **consolidative** |
| **Disposition** | D | Affective, motivational & habit circuits | affect-valence, drive-intensity, habit-context |
| **Understanding** | U | Declarative & episodic store | factual, conceptual, experiential, contextual |
| **Skills** | S | Learned procedures (motor/cognitive) | motor, cognitive, perceptual-motor, social |

*Notation note (editorial).* v1.3 used inconsistent subscripts — DoCA (A), DoDA (D), DoPA (U), DoSA (S). This report uses Do_A(A), Do_A(D), Do_A(U), Do_A(S) throughout. PS (proceduralisation strength) remains a distinct U→S quantity and is not an automaticity parameter. If the original letters encoded a distinction not recovered here, revert.

**Node identity vs zone placement (principle, unchanged).** A node's identity is determined by its *functional role* — capacity ceiling, motivational circuit, content store, procedure — never by its automaticity or trainability. Zone placement describes the current *state* of a component within a node. A fully automatised, non-updatable piece of knowledge is Zone-1 U, not A. This principle prevents the A↔U and A↔S conflations that the Do_A machinery exists to disambiguate, and it survives the §2 revision intact: implementation evidence may inform where a component sits, but role determines which node it is in.

### **3.1 Abilities: qualitative and quantitative change**

Ability changes either open a genuinely new kind of learning or enlarge the
capacity available for kinds that were already possible.

A is **architecturally afforded, not architecturally given.** Architecture bounds the set of U and S that are reachable at all; training determines which of the afforded set is realised. A capacity that emerges under gradient descent in a fixed architecture is *A-realisation*, not new A.

Two kinds of change to A, distinguished by the ceiling edges A→U and A→S:

* **A-qualitative**: the change alters *which* U and S are reachable at all. New sensory or motor modalities are the paradigm case. Candidate cognitive cases: episodic memory, internal simulation, executive function, consolidation.
* **A-quantitative**: the change alters the ceiling, rate, or capacity *within* an unchanged reachable set. Width or depth scaling, context extension, and parameter growth are A-quantitative by default.

**Level 1 / Level 2 restated.** Level 1 is the acquisition of new U and S within a fixed reachable set. Level 2 is A-qualitative change. Constructive growth (e.g. Net2Net widening) is Level 1 machinery unless it can be shown to cross a reachability boundary — which is an empirical question, not a definitional one.

This keeps "Level 2 requires architectural change" from being merely analytic. The substantive and open claim is: **the reachable set under a fixed transformer trained by gradient descent is a proper subset of the reachable set under architectures with dedicated episodic, simulative, executive, or consolidative structure.** If that is false, Level 2 is unnecessary for those capacities.

### **3.2 Consolidation as an ability**

Consolidation is the ability that lets today's effortful learning become
tomorrow's durable, fluent competence.

Consolidation capacity — the existence and quality of a route by which Zone-2/3 content becomes Zone-1 content — is an A sub-domain, not a free rate parameter.

*Justification.* By the criterion in §3.1, a component belongs to A when it determines which U and S are reachable at all. Absent a consolidation route, any competence requiring more acquisition effort than fits within a single working episode is unreachable at any level of effort. That is a reachability bound, not a rate bound. Human expertise routinely sits past it.

*Consequence for §8.* The frontier-LLM deficit is therefore an A deficit — a Level 2 gap — rather than a shortfall of U or S. The missing thing is not knowledge or procedure but the ability that would let knowledge and procedure accumulate.

*Non-circularity.* §3.3 makes plasticity a channel-relative rate; this section makes that rate ability-governed. These are consistent, not circular, under the decomposition:

> rate(X, channel) = f( A_consolidation , channel availability , Aw(X) )

A supplies the capacity, the channel supplies the route, and awareness supplies the direction. Self-initiated consolidation (C-S) without veridical self-inspection is undirected: the system cannot tell what is worth keeping.

### **3.3 Zones and plasticity**

**Zone is position on the load axis only.**

In everyday terms, a Zone-3 learner follows each step of a new recipe, a Zone-2
cook still checks it occasionally, and a Zone-1 cook prepares the dish while
holding a conversation. The zones describe current effort, not what kind of
component is doing the work.

| Zone | Behavioural definition | Provisional Do_A range |
| ----- | ----- | ----- |
| **Zone-1 (core / trait)** | Dual-task cost < 10%; no explicit stepwise execution required; resistant to single-session intervention | ≥ 0.9 (to be fitted) |
| **Zone-2 (trainable)** | Measurable dual-task cost; partial stepwise dependence | 0.3–0.9 (to be fitted) |
| **Zone-3 (conscious / state)** | Performance collapses under load; requires explicit step-by-step execution | < 0.3 (to be fitted) |

**Plasticity is not part of the zone definition.** It is the *transition rate* between zones, and it is **channel-relative**: a property of (component × consolidation channel), not of the component alone.

| Channel | Route |
| ----- | ----- |
| **C-N** | No route. Gains do not outlast the episode — like solving a problem and keeping no notes or memory of it. |
| **C-X** | External artifact. Gains persist outside the agent and are re-presented later — like consulting yesterday's notebook. |
| **C-T** | Substrate, other-initiated. Gains reach the weights through training the agent does not initiate — like a teacher scheduling the next practice session. |
| **C-S** | Substrate, self-initiated. The agent initiates its own update — like noticing a weakness and choosing to practise it until it sticks. |

Retest gain is therefore measured **under a specified channel**. The v1.3 criterion (30-day retest gain < 5%) tacitly assumed human C-T, which is why it degenerates on frozen artificial systems: under C-N every rate is zero by construction, placing the entire system in Zone-1 including components that collapse under load. Separating the axes makes that degeneracy a finding rather than a measurement failure.

Note that the channels differ in how much of the consolidation machinery sits inside the agent. C-T requires nothing of the agent. C-X requires an S (externalisation practice) plus an environmental affordance. C-S requires the A of §3.2. This is why the taxonomy is a substrate ladder with an initiation qualifier on the substrate rung, rather than two independent axes.

### **3.4 Awareness & Control Parameters**

Aw asks whether an actor can accurately inspect an automatic process; Cn asks
whether the actor can interrupt or redirect it.

**Awareness Aw( )** — "re-conscious-isation" gain, graded 0–1. 1 = the actor can voluntarily bring a high-automaticity (Zone-1) process back into conscious working memory and **veridically** report its content; 0 = the process remains opaque even when explicitly probed. Veridicality is the criterion, not fluency: confident, articulate self-report with no predictive relationship to the underlying process scores Aw ≈ 0. Confabulation is the Aw = 0 failure mode with high verbal output. Human assay: process-dissociation hit-rate (probe-cued report of last automatic stimulus or rule). Binary shortcut: correct vs incorrect probe report.

**Control Cn( )** — "veto / redirect" gain, graded 0–1. 1 = complete on-line suppression or re-routing of the automatism; 0 = no detectable override. Human assay: stop-signal or Go/No-Go with automatism pre-loaded; Cn = 1 − (failure rate) × (normalised latency cost). *Amplification* of an automatism is not a control phenomenon; it is D-driven potentiation, modelled as a D→ matrix edge (§5.1). This keeps Cn a pure executive-suppression parameter.

Both parameters are hypothesised to be trainable yet trait-like stable; stability is a registered prediction (§9, claim 6). They modify, not replace, the underlying Do_A value.

---

## **4. Operational Boundaries**

These boundaries prevent capacities, stored content, learned procedures, and
motivation from being renamed as one another when their behaviour changes.

* **A ↔ S**: Do_A(A) vs Do_A(S) determine node placement; developmental windows can lock A into Zone-1.
* **A-qual ↔ A-quant**: reachability of the U/S set, not magnitude of the ceiling (§3.1).
* **U ↔ S**: PS quantifies proceduralisation; bidirectional edges carry PS and IS (insight strength).
* **D loops**: three independent feedback loops, each with its own Do_A(D).

Aw( ) opens a transient →U edge with weight = Aw × Do_A. Cn( ) applies a multiplicative suppressive gain (1 − Cn) to the outgoing activation of the node for the current tick. Accordingly, high-Do_A automatisms with low Aw remain opaque to conscious update, whereas high-Cn nodes can be down-regulated on demand. Up-regulation is a D-edge phenomenon, not a Cn phenomenon.

---

## **5. Interaction Matrix (4×4)**

The interaction matrix records which of the four components is influencing
which other component, rather than treating intelligence as a single score.

Directed cell = **source → target** influence; strength = fitted coefficient or experimental effect size. Key high-impact paths:

* D→U (curiosity drives knowledge)
* U→S (concepts guide practice)
* S→D (competence boosts motivation)
* A→U & A→S (ceiling edges; the criterion for A-qualitative change, §3.1)

**Diagonal self-loops** (meta-): A→A, D→D, S→S

**Metacognition** (defined as U-row): U→A, U→D, U→U, U→S

### **5.1 D-driven potentiation**

Amplification of an automatism (craving-driven habit strengthening, arousal-driven perceptual capture) is modelled as a positive-gain D→ edge with its own fitted coefficient. This is mechanistically distinct from failed veto (low Cn): an actor can simultaneously have high Cn (successful suppression when engaged) and strong D→ potentiation (strong drive when suppression is not engaged). Collapsing these into one signed parameter loses that dissociation.

---

## **6. Measurement Suite (2 h battery)**

The measurement suite replaces impressionistic labels with observable costs,
gains, and response times.

* **Do_A(A) / Do_A(S)**: dual-task cost. *Retest is channel-indexed*: report the channel under which retest gain was measured (§3.3). Human default is C-T.
* **Do_A(D)**: Loop A affective-priming RT; Loop B EEfRT effort-discounting; Loop C slip-of-action habit test.
* **PS**: retrieval latency + dual-task cost during recall.

All metrics open-source scripted (Python / jsPsych).

### **6.1 Awareness & Control (extra 15 min)**

Aw — 24 probe-cued trials interpolated during automatic task; hit-rate = Aw. Cn — 48 stop-signal trials; Cn = 1 − p_fail × (SSRT / median_go_RT). Binary versions may be used for field deployment.

### **6.2 Proposed load assay for artificial systems**

The load axis needs an artificial analogue or the §8 placements are assigned by intuition rather than measured. Proposed: **constrained reasoning budget.** Vary the permitted reasoning-token allocation and measure performance degradation. Zone-1 content survives a severely constrained budget; Zone-3 procedures collapse. The degradation slope is the analogue of dual-task cost. Cheap to run and it makes the §8 table empirical.

---

## **7. Human Enhancement Heuristics**

For people, the framework points interventions at the specific transition or
connection that is weak instead of prescribing a generic intelligence boost.

* **Zone-3 → 2**: deliberate practice + fluency pressure
* **Zone-2 → 1**: spaced over-learning; critical-period sensitive for A
* **Mismatch diagnosis**: high A + low D → under-achievement; high U + low S → knowing-without-doing

Interventions target **matrix edges**, not nodes, for multiplicative gain. Under §3.3 these are explicitly *rate* interventions: they raise the transition rate under an available channel, moving position on the load axis.

---

## **8. AI / LLM Mapping**

For AI systems, ADUS separates architectural ceilings from learned content and
identifies durable self-directed learning as the central missing ability.

**A for artificial systems** = architectural capacities: context length, attention capacity, parameter count, inductive biases, and the presence or absence of a consolidation route. These bound the reachable set of U and S. Learned content, however frozen, is not A. Per §3.1, scaling these quantities is A-quantitative; adding structure that expands the reachable set is A-qualitative.

| Model capability | ADUS placement | Zone | Limitation |
| ----- | ----- | ----- | ----- |
| frozen parametric knowledge | U | 1 | proceduralised content store; no re-conscious-isation pathway (Aw(U) ≈ 0 for provenance); no update mechanism |
| within-session recall (context) | U | 2–3 | veridical but volatile; no cross-session PS update |
| in-context chain-of-thought | S | 3 | high Do_A(S) cost; no persistent delta |
| emergent helpfulness | D | 1–2 | see note below |
| context length / attention capacity | A (quantitative) | 1 | architectural ceiling; not trainable in deployment |
| consolidation route | A (qualitative) | — | **absent**; see below |

*Note on the D row.* v1.3 placed emergent dispositions at Zone-2 on the grounds that they are context-contingent. Evidence that a disposition survives removal of the context that supposedly elicits it — e.g. fabrication behaviour persisting after completion pressure is withdrawn — is Zone-1 evidence. The row is marked 1–2 pending a load-axis measurement (§6.2).

**Central diagnosis (revised).** v1.3 stated this as the absence of a Zone-2→1 route for U and S. Under §3.2 that is more precisely an **ability deficit**: the system lacks the consolidative A that would make the route exist. The continual learning problem is, in ADUS terms, a Level 2 gap — which is what constructive and consolidation mechanisms (cf. Retention Bench) target.

### **8.1 Proposed Aw assay**

Fluent self-report does not measure Aw (§3.4). Instead: elicit the model's introspective report of *which* heuristic, rule, or feature drove an output, then test whether that report predicts behavioural signatures under intervention (ablation, prompt perturbation, activation patching). Aw = predictive validity of introspective report, not its confidence or coherence. Current interpretability results suggest Aw(U) for frontier models is low and unreliable; the assay makes this a measurable quantity rather than an impression.

### **8.2 Internal simulation: functional criterion and assay**

Simulation is **internal** iff the roll-forward of represented state is *not routed through the output channel*. This is an information-flow criterion, not an implementation criterion, and therefore consistent with §2.

*Assay.* Constrain or suppress reasoning tokens and measure whether simulation-dependent performance survives. Survival indicates internal simulation; collapse indicates externalised roll-forward. This makes the chain-of-thought verdict empirical rather than stipulated, and it shares apparatus with §6.2.

*Evidence status.* Mechanistic interpretability supports *representation* of non-linguistic structure (spatial and temporal encodings robust to prompting variation; colour, cardinal direction, object properties). Evidence for *simulation proper* — counterfactual roll-forward of a represented state — is thinner and contested. One structural objection is directly relevant: transformers recompute representations each forward pass with no latent-state persistence beyond context. If internal simulation requires persistent latent state, then the objection to internal simulation and the consolidation deficit of §3.2 are the same deficit at different timescales. ADUS predicts that link.

### **8.3 Adjacent concepts: environment**

ADUS models the agent. Improvement additionally requires conditions the framework does not contain, and which should not be smuggled into the node model. Following Schaul's conditions for improvement in a closed system — informative and aligned feedback, sufficient experience coverage, sufficient capacity — ADUS supplies the third (capacity is A) and the first two are environmental:

* **V — verification strength** of the task environment, ordinal: formal verifier > execution feedback > learned judge > intrinsic signal.
* **Coverage** — breadth and sequencing of available experience. Curriculum is a coverage intervention, not a verification one.

*Substitution claim.* V and Aw are substitutes on the U-row metacognition edges: those edges can be driven externally by V or internally by Aw. A system with a proof checker does not need self-knowledge; a system in a non-verifiable domain is thrown back on it. Hence a model with Aw(U) ≈ 0 should improve reliably where V is high and stall where V is low. This is registered as claim 7.

Human parallels are worth stating carefully, since they are usually conflated. Books and phones are external stores — C-X, a consolidation channel. Schools supply *both* V (marking, correction, examination) and coverage (curriculum sequencing), and these are separable interventions with separable failure modes.

**Open problems.** Continual PS update; Do_A(D) stability across contexts; Zone-1 disposition circuits; whether the reachable set under a fixed transformer is a proper subset (§3.1).

---

## **9. Falsifiable Claims**

These are the framework's nine precise bets; each is followed by a
plain-language reading that must not replace the testable wording.

For the method behind these readings, see the dated companion explainer,
*The nine claims, in plain language* (2026-09-08).

1. Do_A(D) Loop-B baseline predicts 8-week knowledge gain (U) controlling for A (β > 0.3).
   **Plain-language reading:** A person's starting willingness to expend effort should predict how much they learn over eight weeks with β > 0.3, even after accounting for their underlying ability.
2. PS mediates U→S transfer (≥ 50% of effect).
   **Plain-language reading:** At least half of the path from understanding something to performing it skilfully should be explained by that understanding becoming a practised procedure.
3. Habit-loop Do_A(D) Loop-C moderates the D→U slope (interaction p < 0.01).
   **Plain-language reading:** Existing habits should change how strongly motivation turns into new understanding, with the interaction meeting a p < 0.01 threshold.
4. **(Revised.)** Under matched task streams, C-X and C-T both produce positive downstream skill gain, but **per-session gain under C-X is flat or decaying while under C-T it is flat or increasing.** Prediction: slope divergence over ≥ 10 sessions. *Rationale: under C-X the retrieval mechanism does not itself improve from the gains it stores, so nothing makes the next gain easier. This tests the recursion claim rather than the existence claim, which v1.3's formulation could not discriminate.*
   **Plain-language reading:** Notes and trainer-led updates can both help, but repeated trainer-led updates should keep making learning easier while relying on notes alone should not produce that compounding improvement.
5. Dual-task cost < 10% AND PS > 0.7 ⇒ behaviour indistinguishable from Zone-1 core.
   **Plain-language reading:** A well-practised behaviour that loses less than ten percent under distraction should look like an automatic core behaviour.
6. Aw and Cn show trait-like retest stability (r > 0.7 over 6 months) while remaining responsive to targeted training (≥ 0.3 SD gain from an 8-week mindfulness or inhibition protocol). *(To be anchored against published stop-signal / SSRT reliability estimates.)*
   **Plain-language reading:** People's ability to inspect and redirect automatic processes should show six-month retest stability above r = 0.7, while still improving by at least 0.3 standard deviations after focused training.
7. **7a.** **V × Aw substitution.** Systems with Aw(U) ≈ 0 show reliable self-improvement where V is high (formal verifier, execution feedback) and negligible improvement where V is low (learned judge, intrinsic signal). **7b.** The effect of raising Aw is larger at low V than at high V (negative interaction term).
   **7a plain-language reading:** A system that cannot accurately inspect its own understanding can still improve when the world gives clear right-or-wrong feedback, but should improve negligibly when external feedback is weak.
   **7b plain-language reading:** Better self-inspection should help more when external feedback is weak than when it is strong.
8. **Internal simulation.** Under the §8.2 assay, simulation-dependent performance in current frontier models collapses when the output channel is constrained — i.e. roll-forward is externalised, not internal.
   **Plain-language reading:** Current frontier models should lose tasks that require mentally running a situation forward when they are prevented from working it out through their output.
9. **Consolidation as reachability (Level 2 test).** There exist tasks unreachable under C-N *at any context budget* that become reachable under C-T. This discriminates consolidation-as-ability (§3.2) from consolidation-as-rate: the rate reading predicts only slower acquisition, the ability reading predicts a reachability boundary. Directly testable on a continual-learning benchmark with parametric hard-resets.
   **Plain-language reading:** Some tasks should remain impossible no matter how much temporary working space a non-learning system receives, yet become possible when training can make learning persist.

---

## **10. File Formats & Links**

The diagnostic battery, data schema, and registration templates named here are
planned interfaces, not implemented resources.

**Yet to be implemented**

* Diagnostic battery: github.com/symbolfarm/intelligence-ADUS
* Dataset schema: ADUS_schema_v1.4.json
* Pre-registration templates: osf.io/adus

---

## **11. Citation**

Use this citation when referring to version 1.4 of the framework.

```
@techreport{ADUSv1_4,
  title = {{ADUS: A Functional Architecture of Intelligence (v1.4)}},
  author = {{Toby Lightheart}},
  url = {https://github.com/tobylightheart/adus-intelligence},
  year = {2026}
}
```

**End of report** — context set for downstream modelling, intervention design, and comparative alignment studies.
