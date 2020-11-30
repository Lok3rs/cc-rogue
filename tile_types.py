from typing import Tuple

import numpy as np  # type: ignore

# Tile graphics structured type compatible with Console.tiles_rgb
"""
ch: The character, represented in integer format. Translate it from the integer into Unicode.
fg: The foreground color. “3B” means 3 unsigned bytes, used for RGB color codes.
bg: The background color. Similar to fg.
"""

graphic_dt = np.dtype(  # Create a data type object
    [
        ("ch", np.int32),  # Object Unicode codepoint
        ("fg", "3B"),  # 3 unsigned bytes, for RGB colors
        ("bg", "3B"),
    ]
)

# Tile struct used for statically defined tile data
tile_dt = np.dtype(
    [
        ("walkable", np.bool),  # True if this tile can be walked over
        ("transparent", np.bool),  # True if this tile doesn't block field of view
        ("light", graphic_dt),  # Graphics for when the tile was explored
    ])


def new_tile(*, walkable: int, transparent: int, light: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]]) -> np.ndarray:
    """Helper function for defining invidual tile types.  Creates a Numpy array of just the one tile_dt element, and returns it. """
    # * Enforce the use of keywords, so that parameter order doesn't matter.

    return np.array((walkable, transparent, light), dtype=tile_dt)


# represents unexplored, unseen tiles
DARK = np.array((ord(" "), (255, 255, 255), (0, 0, 0)), dtype=graphic_dt)

floor = new_tile(walkable=False, transparent=True, light=(ord("."), (24, 24, 24), (5, 5, 5)))
dungeon = new_tile(walkable=True, transparent=True, light=(ord(" "), (0, 0, 0), (153, 153, 0)))
