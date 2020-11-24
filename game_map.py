import numpy as np
from tcod.console import Console

import tile_types


class GameMap:
    def __init__(self, width: int, height: int):
        self.width, self.height = width, height
        self.tiles = np.full((width, height), fill_value=tile_types.floor, order="F")
        self.tiles[0:33, 10] = tile_types.wall # creates a small, three tile wide wall at the specified location.


    def in_bounds(self, x: int, y: int) -> bool:
        """Return True if x and y are inside of the bounds of this map. Ensure the player doesn’t move beyond the map"""
        return 0 <= x < self.width and 0 <= y < self.height


    def render(self, console: Console) -> None:
        """
        Using the Console tcod class’s tiles_rgb method, we can quickly render the entire map.
        This method proves much faster than using the console.print method that we use for the individual entities.

        """
        console.tiles_rgb[0:self.width, 0:self.height] = self.tiles["dark"]

