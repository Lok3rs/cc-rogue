from .entity import Entity
from components import Item


MONSTER_TYPES = {
    "orc":  {
        "icon": "O",
        "max_hp": 90,
        "color": (0, 255, 0),
        "attack": 10,
    },
    "troll": {
        "icon": "T",
        "max_hp": 60,
        "color": (255, 255, 0),
        "attack": 7,
    },
    "dragon": {
        "icon": "D",
        "max_hp": 400,
        "color": (120, 255, 70),
        "attack": 20
    }
}


class Monster(Entity):
    def __init__(self, x: int, y: int, type: str, max_hp: int = None, attack: int = None, item: Item = None, block_movement: bool = True):
        super().__init__(x, y, MONSTER_TYPES[type]["icon"], MONSTER_TYPES[type]["color"], block_movement)
        self.name = type
        self.max_hp = max_hp
        self.current_hp = max_hp if max_hp is not None else MONSTER_TYPES[type]["max_hp"]
        self.attack = attack if attack is not None else MONSTER_TYPES[type]["attack"]
        self.item = item
