import settings
from .entity import Entity
from .inventory import Inventory


class Player(Entity):
    def __init__(self, x, y):
        super().__init__(x, y, settings.PLAYER['ICON'], settings.PLAYER['COLOR'])
        self.inventory = Inventory(5)
