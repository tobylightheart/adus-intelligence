# The nine claims, in plain language

An explainer for [§9 of the technical report](ADUS-tech-report-v1.4.md). It sits
between the framework and its formal claims: the report states nine falsifiable
bets in the framework's own compressed notation, and this page says what each one
is betting, what the translation exposed, and what could be tested next.

It is dated, not maintained. Written 2026-09-08 against report v1.4. When the
claims change, this page is superseded rather than edited.

**It asks for nothing.** Disagreeing with a reading below is an edit, not a veto.

---

## 1. What was done

Each of the nine claims in §9 was given a plain-language reading, under one
constraint: **the reading never replaces the precise wording.** Both appear
together in the report, precise first.

That constraint is the whole method, and the reason for it is not politeness. The
precise wording is what makes a claim falsifiable. `β > 0.3` names a floor that a
result can fall below; "should predict" names no floor at all and cannot be
refuted by any positive number. A reading that drops a quantifier is not a
translation of the claim, it is a weaker claim wearing the same number.

Each reading was checked against the report's own definitions in §3 and the
glossary, rather than against ordinary usage of the words. `Understanding`,
`ability` and `skill` are all defined terms here, and all three have everyday
meanings that pull away from the definitions.

## 2. What was observed

Writing the readings exposed four things the compressed form hid.

### The nine claims are not one kind of thing

**Three or four are testable on systems we already run.**

- **Claim 9** (consolidation as reachability) describes tasks unreachable under
  `C-N` at any context budget that become reachable under `C-T`, and names
  parametric hard-resets on a continual-learning benchmark as the test. That is
  close to `retention-bench`'s existing design. It is not identical — the
  benchmark measures retention across a reset ladder rather than a reachability
  boundary — but the instrument exists and the gap is a variant, not a programme.
- **Claim 8** (internal simulation) predicts that simulation-dependent
  performance collapses when the output channel is constrained. `adus-harness`
  now runs an agent loop over both an API model and a local Qwen2.5-3B, so a
  subject exists. **Adjacent evidence already sits in the record**, though it is
  not a test: in the G-083 protocol measurement, 66 of 72 responses from the free
  API model opened with `Here's a thinking process:` — roll-forward being
  externalised through the output channel, observed incidentally while measuring
  something else.
- **Claim 4** (C-X flat-or-decaying, C-T flat-or-increasing per-session gain) is
  the accumulation question in different vocabulary. `constructive-retention` has
  produced exactly one construction event and its open question is what happens
  across many. The claim predicts the shape of that curve.
- **Claim 7** (V × Aw substitution) needs a system with near-zero `Aw(U)` under
  both a formal verifier and a learned judge. Buildable on the current harness;
  nothing has been built.

**Five are a human-subjects programme.** Claims 1, 2, 3, 5 and 6 need eight-week
protocols, six-month retest stability, stop-signal reliability anchors, and
dual-task cost measurement. These are ordinary experimental psychology and they
need participants, ethics approval, and time measured in seasons.

Publishing all nine as one list implies a single programme with a single
feasibility. It is two programmes with very different clocks.

### Some readings drop the quantifier that *is* the claim

This is the observation most worth disagreeing with.

- **Claim 1** states `β > 0.3`. The reading says *"should predict … even after
  accounting for their underlying ability."* A β of 0.05 satisfies the reading
  and refutes the claim.
- **Claim 2** states `≥ 50%` of the effect is mediated. The reading says *"at
  least half"* — this one survives, and shows the fix is cheap.
- **Claim 3** states `interaction p < 0.01`. The reading says *"measurably
  change"*. A significance threshold is not a magnitude, and "measurably" reads
  as though it were one.
- **Claim 6** states `r > 0.7` and `≥ 0.3 SD`. The reading says *"fairly
  stable"* and *"improve measurably"*.

Claims 5 and 8 keep their teeth (*"less than ten percent"*, *"prevented from
working it out through their output"*). Claim 9's reading is faithful and reads
well, which suggests the difficulty is not plain language as such.

### One claim is two claims

**Claim 7** asserts (a) that low-`Aw` systems improve where `V` is high and not
where `V` is low, and (b) that the effect of raising `Aw` is *larger* at low `V`
— a negative interaction term. The reading joins these with "and". They can come
apart: (a) could hold and (b) fail, and (b) is the harder and more interesting
bet. As one claim it is refuted by either half.

### The vocabulary that resists translation

`Do_A(D)`, `PS`, `C-X` / `C-T` / `C-N`, `Zone-1`, `Aw`, `Cn`, `V`. The glossary
covers all of these. The readings had to inline the sense of each one, which is
why several of them are long — and inlining a definition is where fidelity was
most often lost, because the short paraphrase of a defined term is usually a
near-synonym rather than the definition.

## 3. What this could mean

**The plain-language layer will be the version that gets quoted.** Precise
wording sits above each reading in the report, but a reader looking for something
to cite takes the sentence they understood. Where a reading has no effect-size
floor, the framework can be credited with a weaker claim than it made — or
refuted against one it never made. That cuts both ways and neither is good.

**The machine-testable subset overlaps almost exactly with the current work.**
Claims 4, 7, 8 and 9 map onto `constructive-retention`'s accumulation question,
`adus-harness`'s agent loop, and `retention-bench`'s reset ladder. The ADUS
programme map argued this from the theory side; §9 arrives at the same place from
the claims side, independently. That is mild evidence the framework and the code
are one programme rather than two things sharing an author.

**And the split is a publication decision, not just a housekeeping one.** Nine
claims presented as one list invites the reading that the framework is waiting on
a psychology lab. Four of them are waiting on us.

## 4. What we could develop or test next

Ranked by what can be done now rather than by what matters most.

1. **Restore the dropped quantifiers** in the readings for claims 1, 3 and 6.
   Claim 2 shows it costs one clause. This is the cheapest fidelity fix available
   and it removes the misquotation risk entirely.
2. **Split claim 7 into 7a and 7b.** The interaction term deserves its own number
   because it is the part that would be surprising if true.
3. **Test claim 8 on the harness.** Constrain the output channel on a
   roll-forward task and measure the collapse. A subject exists as of 2026-09-08;
   the assay in §8.2 is written; this is a small experiment, not a programme.
4. **Test claim 9 against the reset ladder.** Establish first whether
   `retention-bench` measures a reachability boundary or only a rate — the claim
   turns on exactly that distinction, and it is the one the report says
   discriminates the two readings of consolidation.
5. **State the human-subjects claims as a long-horizon set**, with what each
   would need. Marking them honestly is better than leaving nine claims looking
   uniformly imminent.

## Provenance and bounds

Source: `ADUS-tech-report-v1.4.md` §9, and the glossary for every defined term.
No claim wording was changed in writing this page. The observations about which
claims are machine-testable are readings of the current state of
`constructive-retention`, `adus-harness` and `retention-bench`, not measurements
made for this page; the G-083 figure is transcribed from that experiment's record.

Written 2026-09-08 · v1.4 · supersedable, not maintained.
