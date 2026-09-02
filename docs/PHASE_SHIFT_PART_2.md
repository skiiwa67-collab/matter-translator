# Phase Shift Project \u2014 Part Two

Notes from the 2026-09-02 working session. Paper thought experiment.
Game use: this is the ship's fast-travel mode. Not a laboratory build.

This is NOT real physics. It is the working theory we agreed on so far.

## The job

Translate a volume (example: a carbon cube) from point A to point B in
under three femtoseconds. The object inside the volume is almost
irrelevant. We swap volumes, not things.

## Why machines cannot do it

Three femtoseconds is too short for any known computer, capacitor bank,
or copper wire.

Even a few atoms of difference in a wire can change whether a pulse
arrives on time. Z-pinch capacitor timing already struggles on much
longer scales. So the translation cannot be calculated or switched by
normal matter. It has to be inherent in the object and the field around
it, the way a key opens a lock without telling the lock what to do.

The teeth are in the key. The tumblers fall because of the shape, not
because a processor said so.

## The loop

1. Preload the object at A. Charge the volume so the swap is already
   sitting in the object, waiting for the moment.
2. Charge the field. Give A one polarity and B the opposite so
   space-time feels misplaced. A should have been B. B should have been
   A.
3. Wait for the moment of energy. Resonance climbs. When it crosses
   threshold, space-time corrects itself. The volumes swap because the
   setup made the swap inevitable, not because anything is intelligent.
4. If point B is not clear, resonance collapses. Nothing moves. No
   explosion. No overwrite. No voxel printer. Data-style copy is too
   slow and costs too much.

Point B does not need to know what is coming. A sends the "I am in the
wrong place" condition through the field. B only has to be empty.

## Rules we are treating as true

- Window: under three femtoseconds.
- Translation is inherent in the object, or in a resonance field
  surrounding the object. No external calculator in the loop.
- We translate a volume. The cube is cargo.
- Point B must be clear. Occupied B = collapse, not a merge.
- Distance does not matter for energy. Wrongness matters. Five feet or
  five light years is the same shrug if A feels catastrophically
  misplaced.
- Polarity is a cheat code we can actually use in a game model.
- String-theory picture, for flavor only: the cube is a chord. Retune
  it. The listener at B is a tuned vacuum. The string flips ends. No
  travel, just a different octave.

## What we do not know yet

- Exact charge levels.
- Exact resonance frequency.
- How clear "clear" has to be.
- Whether a half-occupied B always collapses, or only most of the time.
- The real math. We know it is missing pieces. Work with the tools we
  have.

## Game model

`sim/resonance_drive.py` is a toy that feels like the loop:

preload \u2192 polarity mismatch \u2192 resonance \u2192 swap
or
blocked B \u2192 resonance collapse

Drop that file into Grok and ask it to wire the class into the ship as
fast travel. Keep the tunables at the top.

## Session crumbs worth keeping

- Raspberry Pop-Tarts were involved.
- "Make it feel like it made a mistake" is the cleanest sentence we
  have for the polarity trick.
- Do not fold space. Swap it.
- Do not move matter. Relabel the volume.

Logged 2026-09-02. Source: Chris / Eve, Phase Shift Project Part Two.
