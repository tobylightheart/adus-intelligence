# ADUS — a functional architecture of intelligence

Two people sit at a piano. One plays fluently and cannot explain why the chord
she just played resolves the way it does. The other can explain it precisely,
and cannot play it. Neither is more intelligent than the other. They differ in
*which part* of intelligence they have developed.

ADUS is a way of naming those parts. It describes intelligence as four things
that are always interacting:

- **Abilities** — what the body and brain can do before anything is learned.
  You have the ability to acquire language; reading and speaking are not
  abilities but things you then learn. For an AI, abilities are its inputs, its
  processing, its memory, and its outputs.
- **Dispositions** — what makes a system act: drives, habits, preferences,
  values, goals. Terence Tao is not merely very capable at mathematics; he had
  a drive to study and practise it from a young age. In a language model, this
  is close to what people call its persona — and it is where most AI safety
  concern actually lives.
- **Understandings** — the associations and operations that connect experiences
  and concepts. Understandings are not simply right or wrong; they have degrees
  of accuracy, precision and completeness. A misunderstanding has the wrong
  associations; an imprecise one is broadly right but vague.
- **Skills** — actions and sequences of actions, judged by quality and timing.
  Playing the instrument is a skill. So is solving an equation, which is mostly
  an application of understanding performed well and quickly.

That is the whole vocabulary. The pianist who cannot explain the chord has the
skill without the understanding; her companion has the understanding without
the skill. Ordinary language blurs them together as "knowing how to play", and
the blur is what makes conversations about intelligence — human or artificial —
go in circles.

## Why split intelligence four ways

Because it turns vague questions into answerable ones.

"Is this system intelligent?" has no useful answer. "Which of these four has it
got, and which is it missing?" does. Current language models have a great deal
of understanding and considerable skill at applying it. What they mostly lack
is the ability to *acquire and keep* new understanding while running — every
conversation starts from the same place. Naming that as a missing **ability**,
rather than a shortfall of intelligence in general, points at what would have to
be built.

The same split does work for people. If someone is not learning, it is worth
knowing whether the obstacle is an ability, a disposition, a missing
prerequisite understanding, or an unpractised skill, because the four call for
different responses.

ADUS is a *functional* architecture: components are identified by the role they
play and the way information moves between them, not by what they are made of.
That is what lets one vocabulary cover a person and a neural network without
claiming the two are alike underneath.

## Where to start

**If you want the argument**, read
[Recursive Understanding Improvement through Network Construction](https://tobylightheart.github.io/research/2026/09/04/recursive-understanding-improvement-through-network-construction.html).
It introduces ADUS in the course of making a case about AI takeoff and is
written to be read straight through.

**If you want the framework itself**, the [technical report](ADUS-tech-report-v1.4.md)
is a specification rather than an introduction. §1–§3 carry the component model
and the ways understanding is consolidated, which is the part most relevant to
current AI. §9 is a list of nine claims stated so that they can be shown false —
the shortest route to what the framework actually commits to.

**If a term is doing more work than it seems**, the
[glossary](ADUS-glossary-v1.4.md) is usually clearer than the report's first use
of it. Read it alongside the report, not after.

## Related work

- **[retention-bench](https://github.com/symbolfarm/retention-bench)** — a
  research instrument that measures whether what a system learned survives a
  discontinuity that wipes its working state. It is the measurement side of the
  claims made here about consolidation.
- **constructive-retention** — experiments in growing network components to
  consolidate memory. In progress, not yet public.
- **adus-harness** — an agent harness built explicitly around these four
  components. In early scoping, not yet public.

## Status

Independent research, actively revised, currently at v1.4 (2026-07-29). The
framework is a working instrument rather than a settled result: version numbers
move, and claims get reformulated when they turn out not to discriminate
between anything.

Feedback and criticism are welcome. The claims in §9 are stated to be
falsifiable, and finding one false is useful.

## Citation

```
@techreport{ADUSv1_4,
  title  = {{ADUS: A Functional Architecture of Intelligence (v1.4)}},
  author = {{Toby Lightheart}},
  url    = {https://github.com/tobylightheart/adus-intelligence},
  year   = {2026}
}
```
