import settings
from .entity import Entity
from typing import Tuple

class Monster(Entity):

    def __init__(self, x: int, y: int, icon: str, name: str, max_hp: int, loot: list, color: Tuple[int, int, int], block_movement: bool = True):
        self.x = x
        self.y = y
        self.icon = icon
        self.name = name
        self.color = color
        self.block_movement = block_movement
        super().__init__(x, y, icon, color, block_movement)
        self.loot = loot
        self.max_hp = max_hp
        self.current_hp = max_hp
        self.color = color

    

    