"""
resonance_drive.py
------------------
A toy simulation of the "resonance drive" concept from our project:
translate a volume (the cube) from point A to point B in under 3
femtoseconds by making the swap inherent in the object + field,
not in any calculation or machine.

This is NOT real physics. It's a game-engine-friendly model of the
*feel* of the system: preload -> polarity mismatch -> resonance ->
swap (or collapse if B is blocked).

Drop this into Grok and ask it to extend, balance, or visualize it
for the spaceship fast-travel mode.
"""

import random
from dataclasses import dataclass, field


# --- Tunables (the "parameters we don't actually know yet") ---
FEMTOSECOND = 1e-15          # seconds
TRANSLATION_WINDOW = 3 * FEMTOSECOND   # hard cap: under 3 fs
RESONANCE_THRESHOLD = 0.92   # how "convinced" space-time must be
POLARITY_MISMATCH_MIN = 0.5  # minimum wrongness to trigger a swap
COLLAPSE_CHANCE_IF_BLOCKED = 0.85  # if B isn't clear, resonance dies


@dataclass
class Volume:
    """A chunk of space-time that can hold matter (the cube)."""
    label: str
    x: float
    y: float
    z: float
    clear: bool = True          # is this slot empty / safe to receive?
    polarity: float = 0.0       # +1 or -1 once charged
    preloaded: bool = False     # has the object been "charged up"?
    resonance: float = 0.0      # 0..1, how close to the swap moment


@dataclass
class ResonanceDrive:
    """The field that surrounds the object and makes the swap happen."""
    a: Volume
    b: Volume
    charged: bool = False
    log: list = field(default_factory=list)

    def _tick(self, msg: str):
        self.log.append(msg)

    def preload(self, energy: float = 1.0):
        """Charge the object at A so the swap is inherent, not computed."""
        self.a.preloaded = True
        self.a.polarity = +1.0
        self._tick(f"Preloaded {self.a.label} with energy {energy:.2f}.")

    def charge_field(self):
        """Give B the opposite polarity so space-time feels 'wrong'."""
        self.b.polarity = -1.0
        self.charged = True
        self._tick(f"Field charged. {self.a.label} is +1, {self.b.label} is -1.")

    def _mismatch(self) -> float:
        return abs(self.a.polarity - self.b.polarity)

    def attempt_translation(self, dt: float = FEMTOSECOND) -> bool:
        """
        Try the swap. Must finish inside TRANSLATION_WINDOW.
        Returns True if the cube moved, False if resonance collapsed.
        """
        if not (self.a.preloaded and self.charged):
            self._tick("Not ready: preload and charge first.")
            return False

        # Build resonance: the more mismatched the polarity, the faster it climbs.
        mismatch = self._mismatch()
        if mismatch < POLARITY_MISMATCH_MIN:
            self._tick(f"Polarity mismatch too small ({mismatch:.2f}). No swap.")
            return False

        # Resonance climbs toward 1.0 within the femtosecond budget.
        # Full +1/-1 mismatch should clear the threshold in one pulse.
        self.a.resonance = min(1.0, self.a.resonance + mismatch * 0.5)
        self._tick(f"Resonance climbing: {self.a.resonance:.2f}")

        if self.a.resonance < RESONANCE_THRESHOLD:
            self._tick("Resonance below threshold. Waiting for the moment.")
            return False

        # The moment: space-time decides A "should" be at B.
        if not self.b.clear:
            if random.random() < COLLAPSE_CHANCE_IF_BLOCKED:
                self._tick("B blocked -> resonance COLLAPSED. Nothing moved.")
                self.a.resonance = 0.0
                return False

        # Swap: A and B exchange roles. The cube is now at B.
        self.a, self.b = self.b, self.a
        self.a.preloaded = False
        self.a.resonance = 0.0
        self.b.polarity = 0.0
        self.charged = False

        # Simulated duration only. Real wall-clock is irrelevant at femtoscale.
        elapsed = dt
        ok = elapsed <= TRANSLATION_WINDOW
        self._tick(
            f"SWAP. Cube now at {self.a.label}. "
            f"Took {elapsed / FEMTOSECOND:.2f} fs "
            f"({'within' if ok else 'OVER'} 3 fs budget)."
        )
        return True

    def status(self) -> str:
        return (
            f"A={self.a.label} (preloaded={self.a.preloaded}, pol={self.a.polarity:+.0f}) | "
            f"B={self.b.label} (clear={self.b.clear}, pol={self.b.polarity:+.0f}) | "
            f"charged={self.charged}"
        )


def demo():
    print("=== Resonance Drive Demo ===\n")

    # Scenario 1: clean B, successful swap
    a = Volume("PointA", 0, 0, 0)
    b = Volume("PointB", 100, 0, 0, clear=True)
    drive = ResonanceDrive(a, b)

    drive.preload(1.0)
    drive.charge_field()
    print(drive.status())
    moved = drive.attempt_translation()
    print("Moved:", moved)
    for line in drive.log:
        print(" -", line)
    print()

    # Scenario 2: B blocked -> collapse
    a2 = Volume("PointA", 0, 0, 0)
    b2 = Volume("PointB", 50, 50, 0, clear=False)  # concrete in the way
    drive2 = ResonanceDrive(a2, b2)
    drive2.preload(1.0)
    drive2.charge_field()
    moved2 = drive2.attempt_translation()
    print("Blocked scenario -> Moved:", moved2)
    for line in drive2.log:
        print(" -", line)


if __name__ == "__main__":
    demo()
