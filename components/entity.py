from typing import Tuple


class Entity:
    """
    A generic object to represent players, enemies, items, etc.
    """

<<<<<<< HEAD
    def __init__(self, x: int, y: int, character: str, color: Tuple[int, int, int], block_movement: bool = False):
=======
    def __init__(self, x: int, y: int, icon: str, color: Tuple[int, int, int], block_movement: bool = False):
>>>>>>> 2911743886ae09d351aa459ead8b0a29403fc795
        self.x = x
        self.y = y
        self.character = icon
        self.color = color
        self.block_movement = block_movement

    def move(self, direction_x: int, direction_y: int) -> None:
        # Move the entity by a given amount
        self.x += direction_x
        self.y += direction_y
