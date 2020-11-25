import numpy as np
from tcod.console import Console
import settings
from typing import Tuple

import tile_types


class GameMap:

    def __init__(self, dict_of_elements):
        self.width = settings.MAP['WIDTH']
        self.height = settings.MAP['HEIGHT']
        self.tiles = np.full((self.width, self.height), fill_value=tile_types.floor, order="F")
        self.dict_of_elements = dict_of_elements


    def render(self, console: Console) -> None:
        """
        Using the Console tcod class’s tiles_rgb method, we can quickly render the entire map. This method proves much faster than using the console.print method that we use for the individual entities.

        """
        console.tiles_rgb[0:self.width, 0:self.height] = self.tiles["dark"]


    @property
    def generate_map(self):
        map = GameMap(self.dict_of_elements)
        for element in self.dict_of_elements:
            map.tiles[self.dict_of_elements[element]] = tile_types.dungeon
        return map


class DungeonsAndChambers:
    def __init__(self, x: int, y: int, width: int, height: int):
        self.x1 = x
        self.y1 = y
        self.x2 = x + width
        self.y2 = y + height


    @property
    def get_size_of_element(self) -> Tuple[slice, slice]:
        self.range_width = slice(self.x1, self.x2)
        self.range_height = slice(self.y1, self.y2)
        return self.range_width, self.range_height
                        # (x1, x2), (y1, y2)
                        # (0:33), (10:15)
                        # width, height


