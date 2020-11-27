from .entity import Entity
from settings import ITEMS


class Item(Entity):
    def __init__(self, x, y, type, name, bonus=0):
        if type not in ITEMS:
            raise ValueError

        super().__init__(x, y, ITEMS[type]["icon"], ITEMS[type]["color"])
        self.name = name
        self.type = type
        self.bonus = bonus
