from game_map import DungeonsAndChambers

SCREEN = {'WIDTH': 80,
          'HEIGHT': 50
          }

MAP = {'WIDTH': 80,
       'HEIGHT': 45
       }

PLAYER = {'ICON': 'Q',
          'START_X': 0,
          'START_Y': 5,
          'COLOR': (255, 255, 255)
          }

NPC = {'ICON': 'N',
       'START_X': 15,
       'START_Y': 10,
       'COLOR': (255, 0, 0)
       }

GATE_MAP_A = {'ICON': """
GA
TE
""",
       'START_X': 75,
       'START_Y': 35,
       'COLOR': (255, 0, 0)
              }


MAP_A = {'room_1': DungeonsAndChambers(x=10, y=5, width=10, height=10).get_size_of_element,
         'room_2': DungeonsAndChambers(x=35, y=15, width=10, height=15).get_size_of_element,
         'room_3': DungeonsAndChambers(x=25, y=1, width=10, height=5).get_size_of_element,
         'room_4': DungeonsAndChambers(x=45, y=2, width=5, height=5).get_size_of_element,
         'room_5': DungeonsAndChambers(x=2, y=30, width=10, height=10).get_size_of_element,
         'room_6': DungeonsAndChambers(x=65, y=30, width=10, height=10).get_size_of_element,
         'room_7': DungeonsAndChambers(x=55, y=20, width=7, height=7).get_size_of_element,
         'room_8': DungeonsAndChambers(x=15, y=20, width=8, height=9).get_size_of_element,
         'room_9': DungeonsAndChambers(x=5, y=30, width=8, height=10).get_size_of_element,
         'room_10': DungeonsAndChambers(x=30, y=34, width=8, height=10).get_size_of_element,
         'room_11': DungeonsAndChambers(x=60, y=3, width=8, height=10).get_size_of_element,
         'room_12': DungeonsAndChambers(x=50, y=35, width=6, height=6).get_size_of_element,
         'dungeon_0': DungeonsAndChambers(x=0, y=5, width=5, height=1).get_size_of_element,
         'dungeon_1': DungeonsAndChambers(x=15, y=3, width=1, height=3).get_size_of_element,
         'dungeon_2': DungeonsAndChambers(x=16, y=3, width=10, height=1).get_size_of_element,
         'dungeon_4': DungeonsAndChambers(x=4, y=5, width=1, height=25).get_size_of_element,
         'dungeon_5': DungeonsAndChambers(x=12, y=37, width=6, height=1).get_size_of_element,
         'dungeon_6': DungeonsAndChambers(x=17, y=29, width=1, height=13).get_size_of_element,
         'dungeon_7': DungeonsAndChambers(x=13, y=9, width=12, height=1).get_size_of_element,
         'dungeon_8': DungeonsAndChambers(x=5, y=12, width=5, height=1).get_size_of_element,
         'dungeon_9': DungeonsAndChambers(x=23, y=22, width=3, height=1).get_size_of_element,
         'dungeon_10': DungeonsAndChambers(x=25, y=9, width=1, height=13).get_size_of_element,
         'dungeon_11': DungeonsAndChambers(x=26, y=12, width=35, height=1).get_size_of_element,
         'dungeon_12': DungeonsAndChambers(x=45, y=5, width=15, height=1).get_size_of_element,
         'dungeon_13': DungeonsAndChambers(x=17, y=42, width=13, height=1).get_size_of_element,
         'dungeon_14': DungeonsAndChambers(x=38, y=37, width=13, height=1).get_size_of_element,
         'dungeon_15': DungeonsAndChambers(x=52, y=24, width=1, height=11).get_size_of_element,
         'dungeon_17': DungeonsAndChambers(x=42, y=24, width=10, height=1).get_size_of_element,
         'dungeon_18': DungeonsAndChambers(x=42, y=17, width=16, height=1).get_size_of_element,
         'dungeon_19': DungeonsAndChambers(x=58, y=17, width=1, height=3).get_size_of_element,
         'dungeon_20': DungeonsAndChambers(x=58, y=27, width=1, height=7).get_size_of_element,
         'dungeon_21': DungeonsAndChambers(x=59, y=33, width=7, height=1).get_size_of_element,
         'dungeon_22': DungeonsAndChambers(x=75, y=36, width=5, height=2).get_size_of_element,
         'dungeon_23': DungeonsAndChambers(x=68, y=9, width=5, height=1).get_size_of_element,
         'dungeon_24': DungeonsAndChambers(x=72, y=10, width=1, height=20).get_size_of_element,

         }
