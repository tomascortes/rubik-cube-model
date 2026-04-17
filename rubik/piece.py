from dataclasses import dataclass, field

import numpy as np


@dataclass
class Piece:
    position: np.ndarray
    colors: dict
    orientation: np.ndarray = field(default_factory=lambda: np.eye(3, dtype=int))

    @property
    def kind(self) -> str:
        n = int(np.count_nonzero(self.position))
        return {1: "center", 2: "edge", 3: "corner"}.get(n, "core")

    def world_stickers(self):
        for local, color in self.colors.items():
            world = self.orientation @ np.array(local, dtype=int)
            yield tuple(int(v) for v in world), color
