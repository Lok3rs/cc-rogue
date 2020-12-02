from .entity import Entity
from components import Item, ITEM_TYPES
from typing import Optional

MONSTER_TYPES = {
    "orc": {
        "icon": "O",
        "max_hp": 90,
        "color": (0, 255, 0),
        "attack": 15,
        'exp': 20,
    },
    "troll": {
        "icon": "T",
        "max_hp": 70,
        "color": (255, 255, 0),
        "attack": 12,
        'exp': 15,
    },
    "dragon": {
        "icon": "D",
        "max_hp": 400,
        "color": (72, 61, 139),
        "attack": 30,
        'exp': 70,
    },

    'dragon_boss': {
        "icon":
'''
  _a' /(     ,>
~~_}\ \(    (
     \(,_(,)'
      _>, _>,''',

        "max_hp": 700,
        "color": (127, 0, 255),
        "attack": 40,
        'exp': 120,
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



troll = Monster(type='troll', x=0, y = 0, max_hp= 70, attack=12, block_movement=True)