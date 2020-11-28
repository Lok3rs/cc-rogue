from .entity import Entity
from .inventory import Inventory


ICON = 'Q'
COLOR = (255, 255, 255)
MAX_HP = 100
ATTACK = 30
DEFENSE = 5
MAX_INVENTORY = 10


class Player(Entity):
    def __init__(self, x, y):
        super().__init__(x, y, ICON, COLOR)
        self.inventory = Inventory(MAX_INVENTORY)
        self.max_hp = MAX_HP
        self.attack = ATTACK
        self.defense = DEFENSE
        self.hp = self.max_hp
        self.current_attack = self.attack
        self.current_defense = self.defense
