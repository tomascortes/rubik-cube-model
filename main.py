from vpython import button, rate, scene

from rubik import Cube
from rubik.visualize import CubeView


MOVE_ROWS = [
    ["U", "U'", "D", "D'"],
    ["R", "R'", "L", "L'"],
    ["F", "F'", "B", "B'"],
]


def build_controls(cube: Cube, view: CubeView) -> None:
    def on_move(move: str):
        def handler(_evt):
            cube.apply(move)
            view.redraw()
        return handler

    def on_reset(_evt):
        fresh = Cube()
        cube.pieces = fresh.pieces
        view.cube = cube
        view.redraw()

    scene.append_to_caption("\n\n")
    for row in MOVE_ROWS:
        for move in row:
            button(text=f" {move} ", bind=on_move(move))
            scene.append_to_caption("  ")
        scene.append_to_caption("\n")
    scene.append_to_caption("\n")
    button(text=" Reset ", bind=on_reset)


if __name__ == "__main__":
    cube = Cube()
    view = CubeView(cube)
    build_controls(cube, view)

    while True:
        rate(30)
