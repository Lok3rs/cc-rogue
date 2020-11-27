from settings import PLAYER
from .entity import Entity
from .inventory import Inventory


class Player(Entity):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER['ICON'], PLAYER['COLOR'])
        self.inventory = Inventory(5)
        self.max_hp = 100
        self.hp = 90
        self.attack = 30
        self._hp = self.max_hp
