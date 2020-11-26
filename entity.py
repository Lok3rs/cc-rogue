from typing import Tuple


class Entity:
    """
    A generic object to represent players, enemies, items, etc.
    """

    def __init__(self, x: int, y: int, character: str, color: Tuple[int, int, int]):
        self.x = x
        self.y = y
        self.character = character
        self.color = color

    def move(self, direction_x: int, direction_y: int) -> None:
        # Move the entity by a given amount
        self.x += direction_x
        self.y += direction_y
