import numpy as np

from .piece import Piece


COLOR_BY_FACE_NORMAL = {
    (+1, 0, 0): "red",
    (-1, 0, 0): "orange",
    (0, +1, 0): "white",
    (0, -1, 0): "yellow",
    (0, 0, +1): "green",
    (0, 0, -1): "blue",
}

# 90-degree rotation matrices (integer entries).
# *_CW is the rotation to apply for a clockwise turn of the face whose outward
# normal lies along the positive axis direction (viewed from outside the cube).
RX_CW = np.array([[1, 0, 0], [0, 0, 1], [0, -1, 0]], dtype=int)
RY_CW = np.array([[0, 0, -1], [0, 1, 0], [1, 0, 0]], dtype=int)
RZ_CW = np.array([[0, 1, 0], [-1, 0, 0], [0, 0, 1]], dtype=int)

# axis index (x=0, y=1, z=2), layer value, CW rotation matrix (viewed from outside the face).
FACES = {
    "U": (1, +1, RY_CW),
    "D": (1, -1, RY_CW.T),
    "R": (0, +1, RX_CW),
    "L": (0, -1, RX_CW.T),
    "F": (2, +1, RZ_CW),
    "B": (2, -1, RZ_CW.T),
}


class Cube:
    def __init__(self):
        self.pieces: list[Piece] = []
        for x in (-1, 0, 1):
            for y in (-1, 0, 1):
                for z in (-1, 0, 1):
                    if x == 0 and y == 0 and z == 0:
                        continue
                    colors = {}
                    if x != 0:
                        colors[(x, 0, 0)] = COLOR_BY_FACE_NORMAL[(x, 0, 0)]
                    if y != 0:
                        colors[(0, y, 0)] = COLOR_BY_FACE_NORMAL[(0, y, 0)]
                    if z != 0:
                        colors[(0, 0, z)] = COLOR_BY_FACE_NORMAL[(0, 0, z)]
                    self.pieces.append(
                        Piece(position=np.array([x, y, z], dtype=int), colors=colors)
                    )

    def rotate_face(self, face: str, clockwise: bool = True) -> None:
        axis, layer, cw = FACES[face]
        R = cw if clockwise else cw.T
        for p in self.pieces:
            if p.position[axis] == layer:
                p.position = R @ p.position
                p.orientation = R @ p.orientation

    def apply(self, moves: str) -> None:
        for token in moves.split():
            face = token[0]
            if face not in FACES:
                raise ValueError(f"unknown face {face!r} in move {token!r}")
            suffix = token[1:]
            if suffix == "":
                self.rotate_face(face, clockwise=True)
            elif suffix == "'":
                self.rotate_face(face, clockwise=False)
            elif suffix == "2":
                self.rotate_face(face, clockwise=True)
                self.rotate_face(face, clockwise=True)
            else:
                raise ValueError(f"unknown move {token!r}")
