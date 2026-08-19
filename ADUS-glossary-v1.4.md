# **ADUS v1.4 — Glossary**

Companion reference to *ADUS Framework – Technical Report (v1.4)*. Entries are alphabetical. Section §-references point to the technical report.

Entries marked **[gap]** are terms the report uses without defining; a proposed definition is given, but it is a proposal, not a restatement. These are collected again in the final section.

---

## **Reading order**

For a first pass, the framework decomposes into five layers:

1. **Nodes** — A, D, U, S. What kinds of working part exist.
2. **State parameters** — Do_A, Aw, Cn, PS. What state a component is in.
3. **Zones** — Zone-1/2/3. Position on the load axis.
4. **Dynamics** — plasticity, consolidation channels, matrix edges. How components move and interact.
5. **Boundary conditions** — V, coverage, reachable set. What the environment and the architecture must supply.

---

## **A**

**A** — see *Abilities*.

**A-qualitative change** (§3.1) — a change to A that alters *which* U and S are reachable at all. The criterion for Level 2. Paradigm case: a new sensory or motor modality.

**A-quantitative change** (§3.1) — a change to A that alters the ceiling, rate, or capacity *within* an unchanged reachable set. Width scaling, parameter growth, and context extension are A-quantitative by default.

**A-realisation** (§3.1) — the emergence under training of a capacity that the architecture already afforded. Not new A. Distinguishes "the model developed X during training" from "the model acquired the ability to develop X."

**Abilities (A)** (§3) — substrate-bounded core capacities, biological or architectural. The node that sets ceilings on what U and S can be acquired. Sub-domains: cognitive, perceptual, motor, sensory, consolidative. In artificial systems: context length, attention capacity, parameter count, inductive biases, presence of a consolidation route.

**Ablation** — removing or zeroing a model component to test whether behaviour depends on it. Used in the Aw assay (§8.1) as an implementation-level intervention measuring a functional quantity.

**Activation patching** — replacing activations at a chosen site with those from a different input, to test causal contribution. Same role as ablation in §8.1.

**Architecturally afforded** (§3.1) — the framework's stance on A: architecture bounds the reachable set; training determines which of the afforded set is realised. Contrasts with "architecturally given," under which A would be fully fixed at design time.

**Automaticity** — see *Do_A*.

**Awareness** — see *Aw*.

**Aw( )** (§3.4) — awareness parameter, or "re-conscious-isation gain," 0–1 per node. 1 = the actor can voluntarily return a Zone-1 process to conscious working memory and report its content *veridically*. 0 = opaque under explicit probing. Veridicality, not fluency, is the criterion.

**Aw(U)** — awareness of the understanding store specifically. Central to the framework's LLM diagnosis: frontier models are hypothesised to have Aw(U) ≈ 0 for provenance, so metacognition (the U-row) runs off a store the system cannot veridically inspect.

---

## **C**

**C-N / C-X / C-T / C-S** (§3.3) — the consolidation channels, in ascending order of substrate involvement:

| | Route |
| --- | --- |
| **C-N** | No route. Gains do not outlast the episode. |
| **C-X** | External artifact. Gains persist outside the agent and are re-presented later. |
| **C-T** | Substrate, other-initiated. Gains reach the weights via a training process the agent does not initiate. |
| **C-S** | Substrate, self-initiated. The agent initiates the update to its own substrate. |

The ladder is a *substrate* ordering with an *initiation* qualifier on the substrate rung, not two independent axes.

**Ceiling edge** (§5) — the A→U and A→S cells of the interaction matrix. Where A constrains what U and S can be acquired. The reachability criterion (§3.1) is stated in terms of these edges.

**Cn( )** (§3.4) — control parameter, or "veto/redirect gain," 0–1 per node. 1 = complete on-line suppression or re-routing of an automatism; 0 = no detectable override. Assay: stop-signal with automatism pre-loaded, Cn = 1 − p_fail × (SSRT / median_go_RT). Deliberately *pure suppression*: amplification is modelled separately as D-driven potentiation.

**Confabulation** (§3.4) — the Aw = 0 failure mode with high verbal output. Confident, articulate self-report with no predictive relationship to the underlying process. The reason fluency cannot serve as an awareness measure.

**Consolidation** (§3.2, §3.3) — the process by which Zone-2/3 content becomes Zone-1 content; equivalently, movement along the load axis that persists beyond the episode.

**Consolidation route** (§3.2) — an available path for consolidation. Its existence, not merely its speed, determines reachability, which is why consolidation capacity is classified as A.

**Consolidative (A sub-domain)** (§3.2) — the ability sub-domain covering consolidation capacity. New in v1.4. Its absence in frontier LLMs is the framework's central AI diagnosis.

**Constrained reasoning budget** (§6.2) — proposed load assay for artificial systems. Vary permitted reasoning-token allocation; measure degradation. Zone-1 content survives severe constraint, Zone-3 procedures collapse. Degradation slope is the analogue of dual-task cost.

**Coverage** (§8.3) — environmental parameter: breadth and sequencing of available experience. Distinct from V. Curriculum is a coverage intervention, not a verification one.

---

## **D**

**D** — see *Disposition*.

**D-driven potentiation** (§5.1) — amplification of an automatism modelled as a positive-gain D→ matrix edge rather than as negative control. Preserves the dissociation between "can suppress when engaged" (high Cn) and "strong drive when not engaged" (strong potentiation).

**Disposition (D)** (§3) — affective, motivational, and habit circuits. Sub-domains: affect-valence, drive-intensity, habit-context. Assayed as three loops (see *Loop A/B/C*).

**Do_A( )** (§3) — automaticity parameter, 0–1 per node. Higher = more automatic, lower dual-task cost, less stepwise execution. Determines zone placement but *not* node identity (§3, node-identity principle). Notation normalised in v1.4; v1.3 used DoCA / DoDA / DoPA / DoSA.

**Dual-task cost** (§3.3) — performance decrement when a component is exercised under a competing demand. The primary operationalisation of the load axis in humans.

---

## **E**

**EEfRT** (§6) — Effort Expenditure for Rewards Task. Effort-discounting assay used for Loop B of D.

**Elastic / plastic** — *article vocabulary, not framework vocabulary.* Elastic adaptation reverts when the episode ends (C-N); plastic adaptation persists (C-T, C-S). Note the collision with Elastic Weight Consolidation, where "elastic" denotes a restoring force that aids retention — the opposite valence.

**Episodic memory (as an A candidate)** (§3.1) — listed as a candidate A-qualitative capacity. Note that in LLMs the context window arguably supplies the *store* functionally, and what is missing is the encoding step — making this partly a consolidation question rather than an ability question.

**Executive function (as an A candidate)** (§3.1) — listed as a candidate A-qualitative capacity. The framework's negative verdict for current LLMs runs through Aw rather than A: monitoring that is not veridical is not executive control.

---

## **F**

**Functional-primary** (§2) — the level-of-analysis commitment in v1.4. Node identity, zone placement, and all §9 claims are stated functionally; implementation evidence is admissible as evidence and mechanism, not as definition.

---

## **I**

**Implementation evidence** (§2) — architectural facts, ablation, patching, mechanistic interpretability. Admissible under the priority rule.

**Insight strength (IS)** (§4) — **[gap]** named as a quantity carried on the S→U edge, alongside PS on U→S, but not defined. *Proposed:* the strength with which procedural competence yields explicit conceptual content — the reverse of proceduralisation, i.e. articulating what one has learned to do.

**Interaction matrix** (§5) — the 4×4 directed source→target influence structure over nodes. Interventions are held to target edges rather than nodes (§7).

**Internal simulation** (§8.2) — roll-forward of represented state that is *not routed through the output channel*. An information-flow criterion, chosen so that internality remains functional rather than implementational. Assay: constrain reasoning tokens and test whether simulation-dependent performance survives.

---

## **L**

**Level 1** (§3.1) — acquisition of new U and S within a fixed reachable set.

**Level 2** (§3.1) — A-qualitative change: expansion of the reachable set.

**Load axis** (§3.3) — the dimension along which zones are defined in v1.4: sensitivity to competing demand and dependence on explicit stepwise execution. Separated in v1.4 from plasticity, which was previously bundled into the zone definition.

**Loop A / Loop B / Loop C** (§6) — **[gap]** the three D feedback loops, identified by assay (affective-priming RT; EEfRT effort-discounting; slip-of-action habit test) rather than by definition. *Proposed mapping:* Loop A ≈ affect-valence, Loop B ≈ drive-intensity, Loop C ≈ habit-context, matching the sub-domain list in §3.

---

## **M**

**Metacognition** (§5) — defined structurally as the U-row of the interaction matrix: U→A, U→D, U→U, U→S. Knowledge acting on the other nodes. Its reliability is bounded by Aw(U), or substituted for externally by V.

**Mismatch diagnosis** (§7) — a diagnostic pattern across nodes rather than within one: high A + low D → under-achievement; high U + low S → knowing-without-doing.

---

## **N**

**Node** (§3) — one of the four components: A, D, U, S.

**Node-identity principle** (§3) — a node's identity is set by *functional role* (capacity ceiling, motivational circuit, content store, procedure), never by automaticity or trainability. Frozen, non-updatable knowledge is Zone-1 U, not A. Exists to prevent A↔U and A↔S conflation.

---

## **P**

**Plasticity** (§3.3) — the transition *rate* between zones. In v1.4 it is not part of the zone definition and it is **channel-relative**: a property of (component × consolidation channel). Decomposed as rate = f(A_consolidation, channel availability, Aw).

**Predictive validity** (§8.1) — the criterion in the Aw assay: does the introspective report predict behaviour under intervention. Replaces confidence and coherence as the measure.

**Priority rule** (§2) — where behavioural and implementation evidence conflict, the behavioural finding fixes the attribution and the implementation finding becomes the thing requiring explanation.

**Process-dissociation hit-rate** (§3.4) — human Aw assay. Probe-cued report of the last automatic stimulus or rule; hit-rate = Aw.

**Proceduralisation strength (PS)** (§3, §4, §6) — the quantity on the U→S edge measuring how far declarative content has become procedure. Assayed by retrieval latency plus dual-task cost during recall. Distinct from Do_A(U), though v1.3 presented them in the same cell.

---

## **R**

**Reachable set** (§3.1) — the set of U and S that a given architecture permits to be acquired at all. The central construct behind Level 1/Level 2: Level 1 moves within it, Level 2 expands it.

**Reachability criterion** (§3.1) — the test for A-qualitative change: does the change alter *which* U and S are reachable, rather than the ceiling, rate, or capacity within an unchanged set.

**Re-conscious-isation** (§3.4) — the process Aw measures: returning an automatised process to conscious working memory such that its content can be veridically reported.

**Retest gain, channel-indexed** (§6) — retest gain is now reported together with the consolidation channel under which it was measured, since under C-N every rate is zero by construction.

---

## **S**

**Skills (S)** (§3) — learned procedures, motor or cognitive. Sub-domains: motor, cognitive, perceptual-motor, social.

**Slip-of-action test** (§6) — habit assay used for Loop C of D: does a previously reinforced response persist after the contingency is devalued.

**SSRT** (§3.4, §6.1) — stop-signal reaction time. Component of the Cn assay.

---

## **T**

**Tick** (§4) — **[gap]** used in the Cn formulation ("for the current tick"), implying a discrete-time dynamical model that is not specified. *Proposed:* one update step of the interaction matrix; needs pinning down before the matrix can be simulated.

---

## **U**

**Understanding (U)** (§3) — the declarative and episodic content store. Sub-domains: factual, conceptual, experiential, contextual. Note that zone placement for a *store* is about retrieval automaticity rather than execution load; see the gaps section.

**U-row** — see *Metacognition*.

---

## **V**

**V (verification strength)** (§8.3) — environmental parameter: the quality of the feedback signal available in the task environment. Ordinal: formal verifier > execution feedback > learned judge > intrinsic signal. Not an ADUS node; an adjacent condition.

**V × Aw substitution** (§8.3, claim 7) — the claim that V and Aw are substitutes on the U-row edges: metacognitive correction can be driven externally by verification or internally by veridical self-inspection. Predicts reliable improvement at high V even where Aw ≈ 0, and stalling at low V.

**Veridicality** (§3.4) — the correspondence between a self-report and the process it reports on. The criterion for Aw, chosen specifically to exclude fluent confabulation.

---

## **Z**

**Zone-1 (core / trait)** (§3.3) — dual-task cost < 10%; no explicit stepwise execution; resistant to single-session intervention. Provisional Do_A ≥ 0.9.

**Zone-2 (trainable)** (§3.3) — measurable dual-task cost; partial stepwise dependence. Provisional Do_A 0.3–0.9.

**Zone-3 (conscious / state)** (§3.3) — performance collapses under load; requires explicit step-by-step execution. Provisional Do_A < 0.3.

**Zone placement** (§3) — the current *state* of a component within a node. Distinct from node identity, which is fixed by functional role.

---

## **Gaps: terms used but not defined in v1.4**

Collected for a v1.5 pass. Proposed definitions above are proposals only.

1. **Insight strength (IS)** — named in §4, never defined.
2. **Loop A / B / C** — identified by assay, not by construct. The mapping to D's sub-domains is inferable but unstated.
3. **Tick** — implies a discrete-time dynamical model that the report does not specify. Blocking for any simulation of the matrix.
4. **Zone semantics for a content store.** The load axis is defined by dual-task cost and stepwise execution, which are properties of *processes*. U is a *store*. In practice §6 measures U through retrieval (latency + dual-task cost during recall), so U's zone is retrieval automaticity — but this is never said, and as written the zone criteria do not straightforwardly apply to U at all. Worth an explicit sentence in §3.3.
5. **PS vs Do_A(U)** — v1.3 listed them in the same table cell; v1.4 asserts they are distinct without stating the relationship. Are they independent, or is PS a directional component of Do_A(U)?
6. **"Developmental windows"** (§4) — invoked as a mechanism locking A into Zone-1; not defined, and its artificial-system analogue is unstated.
7. **Sub-domain boundaries within U** — "experiential" and "contextual" are not distinguished from each other or from "factual."
8. **Channel availability** — appears in the plasticity decomposition (§3.2) as a term in f( ), but is not itself given a scale. Binary, or graded by bandwidth and latency?
