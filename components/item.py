from .entity import Entity


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
