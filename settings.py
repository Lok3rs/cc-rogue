import random

SCREEN = {'WIDTH': 80,
          'HEIGHT': 50
          }

MAP = {'WIDTH': 80,
       'HEIGHT': 45
       }

PLAYER = {'ICON': 'Q',
          'COLOR': (255, 255, 255)
          }

ORC ={
       "icon": "o",
       "name": "orc",
       "loot": ["gold", "sword"],
       "max_hp": 90,
       "color" : (0, 255, 0),
       "attack": 10
}

TROLL = {
       "icon": "t",
       "name": "troll",
       "loot": ["gold", "meet"],
       "max_hp": 60,
       "color" : (255, 255, 0),
       "attack": 7
}

DRAGON = {
       "icon": "D",
       "name": "dragon",
       "loot": ["gold", "armor", "axe", "map"],
       "max_hp": 400,
       "color": (120, 255, 70),
       "attack": 20
}

