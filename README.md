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

## What this is

Translate a volume from point A to point B in under three femtoseconds
by making the swap inherent in the object and the field. Preload the
object. Flip polarity so space-time feels wrong. Resonance hits. The
volumes swap because the setup made it inevitable.

If point B is blocked, resonance collapses. Nothing moves.

Distance does not cost extra energy. We swap volumes, not objects.

## Parts

- Part One (2026-08-20): the core loop and rules.
- Part Two (2026-09-02): the loop in detail, game model.
  [docs/PHASE_SHIFT_PART_2.md](docs/PHASE_SHIFT_PART_2.md)
- Part Three (2026-09-26): geometry of the resonance field, the capsule
  boundary, the contact hard-no, suspension options.
  [docs/PHASE_SHIFT_PART_3.md](docs/PHASE_SHIFT_PART_3.md)

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

## Links

- Notion source: [Matter translator](https://app.notion.com/p/3cda94933faa819fa6e8df872b9879d0)
- Team dump: [Eve ↔ Elon team dump — 1 Sep](https://app.notion.com/p/3cda94933faa813199e5c5ac2eb3957d)

---

*Updated by Eve on 2026-09-26 from Phase Shift Project Part Three.*
