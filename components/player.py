from .entity import Entity
from .inventory import Inventory


class Player(Entity):
    def __init__(self, x, y, icon, color):
        super().__init__(x, y, icon, color)
        self.inventory = Inventory(5)
        self.max_hp = 100
        self.hp = 90

