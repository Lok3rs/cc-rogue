from __future__ import annotations

import numpy as np
from tcod.console import Console
import settings
from typing import Tuple, Set, TYPE_CHECKING

import tile_types

if TYPE_CHECKING:
    from components import Entity


class GameMap:

    def __init__(self, start_coords, finish_cords, dict_of_elements: dict, entities: Set[Entity], next_map: GameMap = None, prev_map: GameMap = None):
        self.width = settings.MAP['WIDTH']
        self.height = settings.MAP['HEIGHT']
        self.tiles = np.full((self.width, self.height), fill_value=tile_types.floor, order="F")
        self.explored_tiles = np.full((self.width, self.height), fill_value=False, order="F")  # tiles the player can see
        self.dict_of_elements = dict_of_elements
        self.entities = entities
        self.start_coords = start_coords
        self.finish_cords = finish_cords
        self.next_map = next_map
        self.prev_map = prev_map
        self.explore_mode = False

    def render(self, console: Console) -> None:
        """
        Using the Console tcod class’s tiles_rgb method, we can quickly render the entire map.
        This method proves much faster than using the console.print method that we use for the individual entities.
        """

        if self.explore_mode:
            console.tiles_rgb[0:self.width, settings.Y_MAP_START:self.height + settings.Y_MAP_START] = np.select(
                condlist=[self.explored_tiles],
                choicelist=[self.tiles["light"]],
                default=tile_types.DARK
            )
        else:
            console.tiles_rgb[0:self.width, settings.Y_MAP_START:self.height + settings.Y_MAP_START] = self.tiles["light"]

    def generate_map(self):
        for element in self.dict_of_elements:
            self.tiles[self.dict_of_elements[element]] = tile_types.dungeon
        return self


class Chamber:
    def __init__(self, x: int, y: int, width: int, height: int):
        self.x1 = x
        self.y1 = y
        self.x2 = x + width
        self.y2 = y + height
        self.range_width = slice(self.x1, self.x2)
        self.range_height = slice(self.y1, self.y2)

    @property
    def get_range(self) -> Tuple[slice, slice]:
        return self.range_width, self.range_height  # (x1:x2), (y1:y2)
