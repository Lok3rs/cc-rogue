<<<<<<< HEAD
from settings import PLAYER
=======
>>>>>>> 2911743886ae09d351aa459ead8b0a29403fc795
from .entity import Entity
from .inventory import Inventory


class Player(Entity):
<<<<<<< HEAD
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER['ICON'], PLAYER['COLOR'])
        self.inventory = Inventory(5)
        self.max_hp = 100
        self.hp = 90
=======
    def __init__(self, x, y, icon, color):
        super().__init__(x, y, icon, color)
        self.inventory = Inventory(5)
        self.max_hp = 100
        self.hp = 90

>>>>>>> 2911743886ae09d351aa459ead8b0a29403fc795
