from vpython import box, vector, scene

from .cube import Cube


COLOR_RGB = {
    "red": vector(0.85, 0.1, 0.1),
    "orange": vector(1.0, 0.45, 0.0),
    "yellow": vector(1.0, 0.95, 0.1),
    "white": vector(0.95, 0.95, 0.95),
    "green": vector(0.1, 0.7, 0.25),
    "blue": vector(0.1, 0.3, 0.9),
}

CUBIE_SIZE = 0.95
STICKER_SIZE = 0.85
STICKER_THICKNESS = 0.02
CUBIE_BODY = vector(0.08, 0.08, 0.08)


class CubeView:
    def __init__(self, cube: Cube):
        self.cube = cube
        self._objects: list = []
        scene.background = vector(0.15, 0.15, 0.15)
        scene.title = "Rubik's Cube"
        self._draw()

    def _draw(self) -> None:
        for p in self.cube.pieces:
            pos = vector(int(p.position[0]), int(p.position[1]), int(p.position[2]))
            self._objects.append(
                box(
                    pos=pos,
                    size=vector(CUBIE_SIZE, CUBIE_SIZE, CUBIE_SIZE),
                    color=CUBIE_BODY,
                )
            )
            for normal, name in p.world_stickers():
                offset = vector(*normal) * 0.5
                size = vector(
                    STICKER_THICKNESS if normal[0] != 0 else STICKER_SIZE,
                    STICKER_THICKNESS if normal[1] != 0 else STICKER_SIZE,
                    STICKER_THICKNESS if normal[2] != 0 else STICKER_SIZE,
                )
                self._objects.append(
                    box(pos=pos + offset, size=size, color=COLOR_RGB[name])
                )

    def redraw(self) -> None:
        for o in self._objects:
            o.visible = False
        self._objects.clear()
        self._draw()
