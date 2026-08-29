---
name: vt-fusion-retrofit
description: Diagnose an existing VT cycle deck for coordination work and propose a fusion slide for Katherine to accept or reject. Reads the deck, names the critical aspects it finds, judges whether those aspects can vary simultaneously and by what structure (stock-and-flow, compensatory pair, conflict case, or none), drafts one candidate slide, and stops. Never inserts a slide without approval. Also drafts the teacher note slide for the cycle. Use when adding a fusion device to an existing deck, when auditing whether a cycle reaches coordination, or when building the fusion table across the arc. This skill does not build new decks — that is vt-deck-authoring. It does not finish decks to shipping standard — that is vt-bio-skill. Triggers - "fusion retrofit", "does this cycle fuse", "add a fusion slide", "fusion table", "coordination audit".
---

# vt-fusion-retrofit

Run this after `vt-bio-skill` has brought a deck to standard. Run it one deck at
a time, with Katherine present. It is not a batch job, and section 6 says why.

`deck_lint.py` remains the last gate.

---

## 1. Words

**Separation.** The student discerns a critical aspect as a thing that can vary,
because it varied while everything else was held still. This is what the 5 core
questions already do.

**Fusion.** The student holds two or more critical aspects at once, because the
case cannot be resolved from either alone.

Marton's underlying construct is **simultaneity**, and it comes in two forms:

- **Synchronic** — the aspects are present in the same case, in the same moment.
  This is fusion in the strict sense.
- **Diachronic** — things met at different times are brought into awareness
  together, so relations between them become discernible. The Concept Bank does
  this, and it is not a lesser thing. It is harder to engineer and most curricula
  never attempt it.

Both terms appear in teacher-facing material with a one-line gloss. **Neither
appears in anything a student reads** — the standing rule forbids coding
vocabulary to students.

---

## 2. The coordination structures

These are **not the same kind of object**, and the difference decides what can be
retrofitted. A representation can be *added* to any cycle whose content
accumulates. A case structure has to be *found* in the content and cannot be
manufactured.

### 2a. One representation

**Stock-and-flow model.** A conditional slide type in `vt-bio-skill` §1; the form
comes from Moore-Anderson. The student reads or builds a model, and the
coordination is rate against amount — a stubborn confusion in its own right,
independent of biology content (Booth Sweeney and Sterman's bathtub studies found
graduate students failing it). Use only where the aspect turns on something that
accumulates.

### 2b. Two case structures

**Compensatory pair.** Two aspects vary inversely while the outcome is held
invariant, so neither aspect alone predicts the outcome. Use where the aspects
stand in an arithmetic relationship — a product or a sum.

*Worked example, ecology.* A sea turtle lays about a hundred eggs per clutch and
almost none reach breeding age. An elephant produces one calf every four or five
years and most survive. Both populations hold steady. Replacement rate is held
invariant; fecundity and per-offspring survival vary inversely. A student
reasoning from clutch size alone concludes the ocean should be solid turtles.
The error is not a knowledge gap — it is discerning one aspect and stopping.

*Worked example, physiology.* Cardiac output = heart rate × stroke volume.
Different combinations give the same output.

**Conflict case.** One case in which one aspect points toward one answer and a
second points toward another, so both must be coordinated to resolve it. Use
where no arithmetic relationship exists — most of Biology, nearly all of
Forensics.

*Worked example.* Legless snakes. Limbs aid locomotion points one way;
fitness is context-dependent points the other. Neither alone settles it. This is
also a discriminating case for teleological reasoning, which is arguably
biology's central conceptual obstacle.

**None.** A legitimate outcome. Some aspects do not co-vary. Say so and record
the reason.

### 2c. The what-if question — evidence, not occasion

A counterfactual asks the student to hold the case, change one aspect, and
generate the consequence. She cannot do that without already holding the relation
between aspects. So it does not create coordination; it reveals whether
coordination happened.

The compensatory pair and the conflict case are **occasions** for coordination.
The what-if is **evidence** of it, and it is visible in what she writes rather
than inferable from a score.

Two constraints:

- **Specify what changes and what is held.** "What if there were no decomposers?"
  leaves the student not knowing how far to go or at what scale. Moore-Anderson's
  forms are constrained: how would X differ *in this other context*, or *if I
  changed it in this way*. An unconstrained counterfactual is the polar bear
  question again.
- **In biology, counterfactuals invite teleology back.** "What if snakes had kept
  their legs?" gives a student reaching for purpose an easy answer. Hold the
  mechanism fixed and vary the condition instead: what if the ancestral
  population had lived in open ground rather than in burrows. Same coordination
  demand, no invitation to purpose.
- **Written and individual.** Moves 8 and 9 may run as group work — the exposure
  is low and the coordination demand is high, which is a good pairing. A group
  product says nothing about who coordinated, so the what-if must be individual
  or the diagnosis is empty.

---

## 3. What the skill does, per deck

1. Read the deck. List the critical aspects, in order, as the deck itself
   states them.
2. For each aspect, and for the pair of aspects if the cycle has two, judge:
   can these vary at the same time in a real case?
3. If yes, name which of the three structures fits, and say why the other two do
   not.
4. If no, say so plainly and give the reason. Do not manufacture a device.
5. Draft **one** candidate slide, cloned from the matching template slide type,
   never built by hand. Design tokens per `vt-bio-skill` §13.
6. Draft the teacher note slide (section 5).
7. **Stop.** Present both to Katherine. Insert nothing.

---

## 4. The design requirement on a fusion slide

The case must be **unresolvable from one aspect**. A task that merely invites
relating leaves an ambiguity in the diagnosis.

[Why this matters downstream: a student who states both aspects and does not
relate them may have coordinated fine and not understood that relating was being
asked for. That is a task-comprehension failure wearing a fusion failure's
clothes. Only a case that cannot be answered one-aspect-at-a-time tells the two
apart. This is a requirement on the slide, not on the rubric.]

---

## 5. The teacher note slide

**One slide, not speaker notes.** Speaker notes are invisible to the audience
this is written for, and scattered notes cannot be removed as a unit. One slide
can be deleted in a single action and the deck still runs.

Carries a marker string in the title, so `deck_lint.py` can require it and a
teacher can find every instance.

Contents:

- The **critical aspect** this cycle teaches, in plain words.
- What is held **invariant** across the examples, and the sentence saying the
  examples differ in one dimension on purpose.
- **What breaks if you substitute an example.** The load-bearing line for
  adopting teachers.
- **Position in the sequence** — what this cycle assumes has already been
  discerned, and what later cycle depends on it.
- **The slide-type map** — which slide types appear here, and which conditional
  ones were deliberately left out.
- **Which simultaneity this cycle is working on** — synchronic, diachronic, or
  both.
- **Visibility** — what this cycle asks students to expose, and to whom. Written
  and private, to a partner, read aloud unattributed, owned aloud, or voted.

[Visibility and complexity are two scales on different clocks and should not be
locked together. A hands-up vote is *low* complexity — a forced binary — sitting
at the top of the visibility scale, which is why it fails in a room where a wrong
first answer is not yet safe. The two-tier response slide solves the commitment
half of the problem and routes around the exposure half, which is why it works
where a vote would freeze the room. If visibility rises monotonically across the
arc, the highest-exposure moves land on the highest-complexity content, which is
the worst pairing. Better: raise visibility across the year, reset it low within
each cycle.]

[The slide-type map makes the deck self-documenting. `deck_lint.py` reads the
declared map, then checks the deck contains what it declared.]

---

## 6. Why this is not a batch job

Two reasons, and the second is the more important.

**It cannot decide.** Existing decks already made coherent choices. A skill that
picks a fusion device by rule will insert compensatory pairs into cycles with no
compensatory relationship, and the undoing costs more than the building.

**The case file is the byproduct.** Every accept and reject Katherine makes while
running this across 26 decks is a documented decision, in her words, with the
content in view. The case file is not a separate writing task. It is the record
of this run. Capture the reason at the moment of the decision, not afterward.

---

## 7. Output per deck, for the fusion table

One row: cycle, critical aspects, synchronic device or none, reason for none,
diachronic device present, NGSS codes.

The table across all 20 cycles is what makes a coverage hole visible, and it is
what a teacher needs to plan across weeks. A teacher cannot engineer diachronic
simultaneity without seeing the weeks at once — the same argument made for
students, applied to the person planning the year.

[An absence in the table is not automatically a hole. A standard addressed
without a fusion device, because the content carries no compensatory relationship
and no genuine conflict case, is a design decision. The table distinguishes the
two; it does not resolve them for you.]
