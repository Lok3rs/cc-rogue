from __future__ import annotations

from typing import Tuple, Optional
from random import randint


class Entity:
    """
    A generic object to represent players, enemies, items, etc.
    """

    def __init__(self, x: int, y: int, icon: str, color: Tuple[int, int, int], block_movement: bool = False, talk_to_player: Optional[str] = '', is_gate: bool = False):
        self.x = x
        self.y = y
        self.character = icon
        self.color = color
        self.block_movement = block_movement
        self.talk_to_player = talk_to_player
        self.is_gate = is_gate

    def move(self, direction_x: int, direction_y: int) -> None:
        # Move the entity by a given amount
        self.x += direction_x
        self.y += direction_y

    def put_on_map(self, chamber_range: Tuple[slice, slice]):
        self.x = randint(chamber_range[0].start, chamber_range[0].stop - 1)
        self.y = randint(chamber_range[1].start, chamber_range[1].stop - 1)
        return self
