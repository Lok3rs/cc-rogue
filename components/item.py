from .entity import Entity
from random import randint

ITEM_TYPES = {
    "special": {"icon": "@", "color": (235, 97, 35)},
    "weapon": {"icon": "w", "color": (0, 106, 212)},
    "armor": {"icon": "a", "color": (0, 128, 0)},
    "food": {"icon": "f", "color": (150, 75, 0)}
}


class Item(Entity):
    def __init__(self, type, name, x=0, y=0, bonus=0):
        if type not in ITEM_TYPES:
            raise ValueError("Wrong type of item")
        super().__init__(x, y, ITEM_TYPES[type]["icon"], ITEM_TYPES[type]["color"])
        self.name = name
        self.type = type
        self.bonus = bonus

    def get_description(self):
        attribute = None
        if self.type == "food":
            attribute = "HP"
        elif self.type == "weapon":
            attribute = "ATK"
        elif self.type == "armor":
            attribute = "DEF"

        if attribute:
            return f"{self.name} (+{self.bonus} {attribute})"
        else:
            return self.name


apple = Item("food", "apple", bonus=randint(5, 15))
breed = Item("food", "breed", bonus=randint(15, 30))
meet = Item("food", "meet", bonus=randint(25, 40))
health_potion = Item("food", "health potion", bonus=randint(30, 100))

rusted_sabre = Item("weapon", "rusted sabre", bonus=randint(4, 6))
double_edged_axe = Item("weapon", "double-edged axe", bonus=randint(4, 8))
hatchet = Item("weapon", "hatchet", bonus=randint(8, 12))
magic_sword = Item("weapon", "magic sword", bonus=randint(10, 17))
blessed_axe = Item("weapon", "blessed axe", bonus=randint(20, 35))

silver_armor = Item("armor", "silver armor", bonus=(randint(10, 15)))
golden_armor = Item("armor", "golden_armor", bonus=randint(20, 35))

LIST_OF_ITEMS = [apple, breed, meet, rusted_sabre, double_edged_axe]
LIST_OF_ITEMS_B = [silver_armor, hatchet, magic_sword, health_potion, apple, breed]
LIST_OF_ITEMS_C = [silver_armor, magic_sword, golden_armor, blessed_axe, health_potion, meet, breed, hatchet]
