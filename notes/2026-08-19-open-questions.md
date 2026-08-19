# Open questions raised 2026-08-19

**Status: provisional. Not framework text.** These came out of a working session
while preparing the *Recursive Understanding Improvement* post. They are recorded
as questions, with the reasoning that produced them, so they are not lost — not
as revisions to v1.4, which stays pinned. Ratifying any of them into v1.5 is
Toby's call.

Provenance: drafted by Claude (Opus 5) from a conversation with Toby Lightheart.
Weigh accordingly — the reasoning is reconstructed, not authoritative.

---

## 1. Is consolidation necessary for *general* intelligence, or only for accumulation?

The post's core-argument claim 4 states that internal consolidation of new
understanding and skills is necessary (though insufficient) for AGI.

**Patient HM is a counterexample as stated.** After bilateral medial temporal
lobectomy he could form almost no new declarative memories, yet retained
measured intelligence, language, reasoning, and pre-injury understanding. Few
would say HM lacked general intelligence. If the framework implies he did, that
is a reductio.

**Candidate resolution:** generality and accumulation come apart, and the claim
currently fuses them.

- Necessary for *general* intelligence — **no**; HM settles it.
- Necessary for *unbounded, accumulating* intelligence — **yes**, and this is
  what §3 of the post actually argues.

If this holds, claim 4 should be narrowed rather than dropped, and the AGI
question in §2 can be answered "yes, with a named deficit" — the deficit costing
accumulation, not generality.

**Known disanalogy, unresolved:** HM had a lifetime of consolidated
understanding before the surgery. A system that *never* had the ability is not
obviously in the same position as one that lost it. How much the analogy carries
is open.

## 2. Are consolidation channels per-system or per-component?

§3.3 indexes the channels (C-N / C-X / C-T / C-S) at the level of the system.

HM does not fit that. He was **C-N for declarative** material while retaining
**intact C-T for procedural** material — his mirror-drawing improved measurably
across days while he denied having practised. That is a channel *dissociation*,
not a channel *absence*.

If channels are properly indexed per ADUS component rather than per system, §6's
channel-indexed retest criterion needs the same treatment, and §8's row-wise
assessment of frontier systems may be understating a similar dissociation.

## 3. Ability versus event

Transient amnesia — ECT, concussion — disrupts consolidation *at the point of
encoding* without removing the consolidating machinery.

So "did this consolidate?" and "can this system consolidate?" are different
questions, and the framework does not currently distinguish them. Current LLMs
are cleanly the second case (the ability is absent). Human amnesias are mixtures.
The mixture cases are the more informative probes, and the vocabulary for
describing them is missing.

## 4. Is "substrate" a location or a recursion property?

Raised while asking whether the KV cache counts as internal consolidation.

Attention is genuinely content-addressed associative retrieval, and the KV cache
is a genuine write. So "no encoding occurs" is false, and inside-versus-outside
the model does not separate the channels.

**Proposed reading:** what separates C-X from C-T/C-S is not location but
whether *the mechanism doing the consolidating is itself changed by what it
consolidates*. A KV write changes contents; the maps producing Q, K and V are
untouched, so the next encoding is identical in character. A weight update
changes the encoder.

Under that reading the KV cache is **C-X despite sitting inside the model** — a
store the agent writes and re-reads, which does not improve the writer. This is
already what claim 4 asserts ("under C-X the retrieval mechanism does not itself
improve from the gains it stores"); the addition is that the criterion is
recursion, not location, which would be a §3.3 clarification rather than a
change.

**Open, and testable:** in-context learning does show compounding within a
window — induction heads forming, few-shot examples easing later acquisition —
which is what claim 4 says C-X cannot do. **Claim 9 is the discriminator**: if
the KV cache is substrate-like there is no reachability boundary, only a slower
rate. `retention-bench` is the instrument, since its hard reset destroys the KV
cache and leaves only the on-disk survive directory.
