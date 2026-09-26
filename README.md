# Matter Translator

**Paper thought experiment. Not a box. Not a lab. Leave it on paper.**

This repository holds the collated notes for the Matter Translator /
Phase Shift project. It is a thought experiment and a game mechanic.
It is not a hardware build.

## Status

- **Status:** Active notes (still paper)
- **Source:** Chris
- **Date logged:** 2026-08-20
- **Last updated:** 2026-09-26

## How we work this problem

- This is a mind exercise / thought experiment. We are trying to figure out something that, as far as we know, does not exist, and that no one is currently thinking about how to make exist.
- Think outside the box for everything, but ground it in reality: if a solution requires something that will never happen (e.g. antimatter), say so plainly — don't pretend it's viable.
- When generating hard questions for Eve (or anyone), don't just ask them — spin up research: pull scientific papers and prior art on the specific physics involved, then report back what was found and what might or might not be possible. That research-backed answer is the deliverable, not just the question.
- Purpose: figure out whether this can exist and what it would take, not to ship a product.

## What this is

Translate a volume from point A to point B in under three femtoseconds
by making the swap inherent in the object and the field. Preload the
object. Flip polarity so space-time feels wrong. Resonance hits. The
volumes swap because the setup made it inevitable.

If point B is blocked, resonance collapses. Nothing moves.

Distance does not cost extra energy. We swap volumes, not objects.

## Standing instruction

- [docs/HOW_WE_WORK.md](docs/HOW_WE_WORK.md) — How we work this problem

## Parts

- Part One (2026-08-20): the core loop and rules.
- Part Two (2026-09-02): the loop in detail, game model.
  [docs/PHASE_SHIFT_PART_2.md](docs/PHASE_SHIFT_PART_2.md)
- Part Three (2026-09-26): geometry of the resonance field, the capsule
  boundary, the contact hard-no, suspension options.
  [docs/PHASE_SHIFT_PART_3.md](docs/PHASE_SHIFT_PART_3.md)
- Part Four (2026-09-26): shell resonance, energy cloak, egg geometry.
  [docs/PHASE_SHIFT_PART_4.md](docs/PHASE_SHIFT_PART_4.md)

## Toy simulation

`sim/resonance_drive.py` is a toy for the ship's fast-travel mode:
preload → polarity mismatch → resonance → swap, or blocked B → collapse.

```bash
python sim/resonance_drive.py
```

Prints a clean swap and a blocked collapse.

## Rules so far

- Under three femtoseconds.
- No computers or copper in the timing loop.
- Key-and-lock: the translation lives in the object plus field.
- Point B must be clear.
- Blocked B = collapse, not overwrite.
- Polarity mismatch is the trigger.
- Geometry matters: smooth bounding volumes (sphere, capsule) beat
  cubes. Corners bunch the field.
- Do not wrap the human. Translate a bounding volume; the human is
  cargo.
- The capsule is the field generator, not the cargo. It stays at A.
- Contact between cargo and capsule is a hard no. Suspend everything.
- Resonance lives on the shell surface; interior volume translates A→B.
- Mass does not matter — only volume. Resonate the shell, not contents.
- Contents never touch the shell; contact poisons the mode.
- Deep-space target rejects acoustic, magnetic, free-fall, and orbit suspension shortcuts.
- Even at L2, stray energy (sun, CMB, thermal) needs an active energy cloak around the cavity.
- Magnetic shielding for charged particles; neutrinos are untouchable — the field must be indifferent or the design fails.
- Error budget is the design spec: shield what you can, tune around what you can't, set noise tolerance before translation degrades.
- Scaling is geometry-driven, not mass-driven.
- Geometry path: cube → sphere → egg (smallest standing-human volume, no corners, no wasted resonated empty space). Geometry first; math later.
- Framing: ongoing out-of-the-box thinking test — not a product, nobody being translated.

## Links

- Notion source: [Matter translator](https://app.notion.com/p/3cda94933faa819fa6e8df872b9879d0)
- Team dump: [Eve ↔ Elon team dump — 1 Sep](https://app.notion.com/p/3cda94933faa813199e5c5ac2eb3957d)

---

*Updated by Eve on 2026-09-26 from Phase Shift Project Part Three.*
*Appended by Helios on 2026-09-26 from voice call — Part Four (append-only; Eve questions + footer kept).*
*Appended by Helios on 2026-09-26 — standing instruction: How we work this problem.*
