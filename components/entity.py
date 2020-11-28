from typing import Tuple, Optional


class Entity:
    """
    A generic object to represent players, enemies, items, etc.
    """

    def __init__(self, x: int, y: int, icon: str, color: Tuple[int, int, int], block_movement: bool = False, talk_to_player: Optional[str] = ''):
        self.x = x
        self.y = y
        self.character = icon
        self.color = color
        self.block_movement = block_movement
        self.talk_to_player = talk_to_player

    def move(self, direction_x: int, direction_y: int) -> None:
        # Move the entity by a given amount
        self.x += direction_x
        self.y += direction_y
