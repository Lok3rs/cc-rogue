from __future__ import annotations

import numpy as np
from tcod.console import Console
import settings
from typing import Tuple, Iterable, Optional, TYPE_CHECKING

import tile_types

if TYPE_CHECKING:
    from components.entity import Entity


class GameMap:

    def __init__(self, dict_of_elements: dict, entities: Iterable[Entity] = ()):
        self.width = settings.MAP['WIDTH']
        self.height = settings.MAP['HEIGHT']
        self.tiles = np.full((self.width, self.height), fill_value=tile_types.floor, order="F")
        self.dict_of_elements = dict_of_elements
        self.entities = entities

    def render(self, console: Console) -> None:
        """
        Using the Console tcod class’s tiles_rgb method, we can quickly render the entire map. 
        This method proves much faster than using the console.print method that we use for the individual entities.
        """
        console.tiles_rgb[0:self.width, 0:self.height] = self.tiles["dark"]

    @property
    def generate_map(self):
        map = GameMap(self.dict_of_elements)
        for element in self.dict_of_elements:
            map.tiles[self.dict_of_elements[element]] = tile_types.dungeon
        return map

    def get_blocking_entity(self, entities, x: int, y: int) -> Optional[Entity]:
        for entity in entities:
            if entity.block_movement and entity.x == x and entity.y == y:
                return entity
        return None


class DungeonsAndChambers:
    def __init__(self, x: int, y: int, width: int, height: int):
        self.x1 = x
        self.y1 = y
        self.x2 = x + width
        self.y2 = y + height
        self.range_width = slice(self.x1, self.x2)
        self.range_height = slice(self.y1, self.y2)

    @property
    def get_size_of_element(self) -> Tuple[slice, slice]:
        return self.range_width, self.range_height
        # (x1, x2), (y1, y2)
        # (0:33), (10:15)
        # width, height
