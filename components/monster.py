from .entity import Entity
from components import Item
from typing import Optional


MONSTER_TYPES = {
    "orc":  {
        "icon": "O",
        "max_hp": 90,
        "color": (0, 255, 0),
        "attack": 10,
        'exp': 20,
    },
    "troll": {
        "icon": "T",
        "max_hp": 60,
        "color": (255, 255, 0),
        "attack": 7,
        'exp': 15,
    },
    "dragon": {
        "icon": "D",
        "max_hp": 400,
        "color": (120, 255, 70),
        "attack": 20,
        'exp': 70,
    }
}


class Monster(Entity):
    def __init__(self, type: str, x: int = 0, y: int = 0, max_hp: int = None, attack: int = None, item: Item = None, block_movement: bool = True, talk_to_player: Optional = ''):
        super().__init__(x, y, MONSTER_TYPES[type]["icon"], MONSTER_TYPES[type]["color"], block_movement)
        self.name = type
        self.max_hp = max_hp
        self.current_hp = max_hp if max_hp else MONSTER_TYPES[type]["max_hp"]
        self.attack = attack if attack else MONSTER_TYPES[type]["attack"]
        self.exp = MONSTER_TYPES[type]["exp"]
        self.item = item
        self.talk_to_player = talk_to_player
