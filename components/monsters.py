from .entity import Entity
from typing import Tuple


class Monster(Entity):
    def __init__(self, x: int, y: int, icon: str, name: str, max_hp: int, color: Tuple[int, int, int], attack: int, block_movement: bool = True, index: int = 123):
        super().__init__(x, y, icon, color, block_movement)
        self.name = name
        self.max_hp = max_hp
        self.current_hp = max_hp
        self.attack = attack
        self.index = index
