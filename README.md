# rubik-cube-model

A 3x3 Rubik's cube modeled piece-by-piece (corners, edges, centers) with
integer rotation matrices, and an interactive 3D viewer in the browser
via [vpython](https://vpython.org/).

## Demo

<!-- video goes here -->

## Model

Each piece stores:

- `position` — integer vector in `{-1, 0, 1}^3`
- `orientation` — 3x3 integer rotation matrix (identity when solved)
- `colors` — mapping from _local_ face normal to color name

Because all face turns are 90° multiples, rotation matrices stay in
`{-1, 0, 1}` — no floating-point drift across any sequence of moves.

A face turn picks the 9 pieces in that layer and left-multiplies both
their position and orientation by the turn's rotation matrix.

## Usage

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python main.py
```

A browser tab opens with the cube. Drag to orbit. Buttons below rotate
faces in standard notation (`U`, `U'`, `R`, `R'`, ...). `Reset` returns
to solved.

Programmatic API:

```python
from rubik import Cube

cube = Cube()
cube.rotate_face("U", clockwise=True)
cube.apply("R U R' U'")
```

## Files

- `rubik/piece.py` — `Piece` dataclass
- `rubik/cube.py` — `Cube`: build, `rotate_face`, `apply` (move notation)
- `rubik/visualize.py` — `CubeView` vpython renderer
- `main.py` — demo entrypoint with UI buttons
