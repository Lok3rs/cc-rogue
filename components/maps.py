from game_map import DungeonsAndChambers, GameMap
from components.entity import Entity
from components.item import Item
from components.monsters import Monster
from components.player import Player

from random import randint, choice


GATE = {
    'icon': 'GA',
    'icon_2': 'TE',
    'color': (255, 0, 0)
}

START_MAP_A = {
    'start_x': 0,
    'start_y': 5,
}



MAP_A = {
    'room_1': DungeonsAndChambers(x=10, y=5, width=10, height=10).get_size_of_element,
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
    'dungeon_22': DungeonsAndChambers(x=74, y=36, width=5, height=2).get_size_of_element,
    'dungeon_23': DungeonsAndChambers(x=68, y=9, width=5, height=1).get_size_of_element,
    'dungeon_24': DungeonsAndChambers(x=72, y=10, width=1, height=20).get_size_of_element,

}

START_MAP_B = {
    'start_x': 0,
    'start_y': 35,
}

GATE_MAP_B_1 = {
    'start_x': 78,
    'start_y': 36,
}

GATE_MAP_B_2 = {
    'start_x': 78,
    'start_y': 37,
}

NPC_MAP_B = {

    'icon': 'N',
    'start_x': 15,
    'start_y': 35,
    'color': (255, 0, 0)
}

MAP_B_CHAMBERS = {
    'room_1': DungeonsAndChambers(x=10, y=30, width=10, height=10).get_size_of_element,
    'room_2': DungeonsAndChambers(x=65, y=5, width=10, height=15).get_size_of_element,
    'room_3': DungeonsAndChambers(x=25, y=3, width=10, height=5).get_size_of_element,
    'room_4': DungeonsAndChambers(x=13, y=20, width=5, height=5).get_size_of_element,
    'room_5': DungeonsAndChambers(x=35, y=33, width=10, height=10).get_size_of_element,
    'room_6': DungeonsAndChambers(x=3, y=3, width=10, height=10).get_size_of_element,
    'room_7': DungeonsAndChambers(x=30, y=16, width=7, height=7).get_size_of_element,
    'room_8': DungeonsAndChambers(x=50, y=3, width=5, height=9).get_size_of_element,
    'room_9': DungeonsAndChambers(x=56, y=26, width=8, height=10).get_size_of_element,
    'room_10': DungeonsAndChambers(x=70, y=34, width=8, height=10).get_size_of_element,
    'room_11': DungeonsAndChambers(x=43, y=24, width=8, height=4).get_size_of_element,
    'dungeon_0': DungeonsAndChambers(x=0, y=35, width=10, height=1).get_size_of_element,
    'dungeon_1': DungeonsAndChambers(x=13, y=5, width=12, height=1).get_size_of_element,
    'dungeon_2': DungeonsAndChambers(x=20, y=35, width=15, height=1).get_size_of_element,
    'dungeon_4': DungeonsAndChambers(x=6, y=13, width=1, height=30).get_size_of_element,
    'dungeon_5': DungeonsAndChambers(x=15, y=25, width=1, height=5).get_size_of_element,
    'dungeon_6': DungeonsAndChambers(x=17, y=6, width=1, height=14).get_size_of_element,
    'dungeon_7': DungeonsAndChambers(x=17, y=9, width=33, height=1).get_size_of_element,
    'dungeon_8': DungeonsAndChambers(x=45, y=39, width=25, height=1).get_size_of_element,
    'dungeon_9': DungeonsAndChambers(x=33, y=26, width=10, height=1).get_size_of_element,
    'dungeon_10': DungeonsAndChambers(x=32, y=9, width=1, height=18).get_size_of_element,
    'dungeon_11': DungeonsAndChambers(x=49, y=32, width=8, height=1).get_size_of_element,
    'dungeon_12': DungeonsAndChambers(x=60, y=30, width=11, height=1).get_size_of_element,
    'dungeon_13': DungeonsAndChambers(x=48, y=27, width=1, height=6).get_size_of_element,
    'dungeon_14': DungeonsAndChambers(x=70, y=20, width=1, height=10).get_size_of_element,
    'dungeon_22': DungeonsAndChambers(x=74, y=36, width=5, height=2).get_size_of_element,
    'dungeon_23': DungeonsAndChambers(x=6, y=43, width=20, height=1).get_size_of_element,
    'dungeon_24': DungeonsAndChambers(x=25, y=36, width=1, height=7).get_size_of_element,

}

MAP_C = {
    'room_1': DungeonsAndChambers(x=44, y=10, width=30, height=30).get_size_of_element,
    'room_2': DungeonsAndChambers(x=5, y=3, width=10, height=8).get_size_of_element,
    'room_3': DungeonsAndChambers(x=5, y=30, width=10, height=8).get_size_of_element,
    'room_4': DungeonsAndChambers(x=30, y=20, width=5, height=5).get_size_of_element,
    'room_5': DungeonsAndChambers(x=23, y=33, width=10, height=10).get_size_of_element,
    'room_6': DungeonsAndChambers(x=23, y=12, width=8, height=5).get_size_of_element,
    'room_7': DungeonsAndChambers(x=8, y=20, width=5, height=5).get_size_of_element,
    'dungeon_0': DungeonsAndChambers(x=0, y=35, width=26, height=1).get_size_of_element,
    'dungeon_1': DungeonsAndChambers(x=13, y=5, width=40, height=1).get_size_of_element,
    'dungeon_4': DungeonsAndChambers(x=26, y=5, width=1, height=29).get_size_of_element,
    'dungeon_7': DungeonsAndChambers(x=12, y=22, width=20, height=1).get_size_of_element,
    'dungeon_11': DungeonsAndChambers(x=53, y=5, width=1, height=5).get_size_of_element,
    'dungeon_14': DungeonsAndChambers(x=10, y=11, width=1, height=10).get_size_of_element,
}

START_MAP_C = {
    'start_x': 0,
    'start_y': 35,
}

GATE_MAP_C = {
    'start_x': 77,
    'start_y': 35,
}

NPC_MAP_C = {
    'icon': 'N',
    'start_x': 15,
    'start_y': 35,
    'color': (255, 0, 0)
}


talk = {
    'npc': ['Save us from Dragon!', 'Dragon has the...key!'],
    'orc': ['Orc: Grrrrrrrrrr..!', 'Orc: You will die!', "Orc: Let's Fight!", 'Orc: You have no chance!'],
    'troll': ['Troll: Ha Ha Ha Ha', 'Troll: I will eat your flesh!', 'Troll: Tou choose wrong place...'],
    'dragon': ['Dragon: Hrrrrr.....'],
    'gate': ['You need key!']
}


player_map_B = Player(START_MAP_B['start_x'], START_MAP_B['start_y'])
entities_map_B = {
    player_map_B,
    Entity(NPC_MAP_B['start_x'], NPC_MAP_B['start_y'], NPC_MAP_B['icon'], NPC_MAP_B['color'], block_movement=True, talk_to_player=choice(talk['npc'])),
    Entity(GATE_MAP_B_1['start_x'], GATE_MAP_B_1['start_y'], GATE['icon'], GATE['color'], block_movement=True, talk_to_player=choice(talk['gate'])),
    Entity(GATE_MAP_B_2['start_x'], GATE_MAP_B_2['start_y'], GATE['icon_2'], GATE['color'], block_movement=True, talk_to_player=choice(talk['gate'])),
    Monster(randint(11, 19), randint(31, 39), "orc", item=Item(8, 1, "food", "meet", 30, index=1),talk_to_player=choice(talk['orc'])),
    Monster(randint(4, 12), randint(4, 12), "orc", item=Item(8, 1, "food", "meet", 30, index=1),talk_to_player=choice(talk['orc'])),
    Monster(randint(4, 12), randint(4, 12), "orc", item=Item(0, 0, "weapon", "rusted sabre", 5), talk_to_player=choice(talk['orc'])),
    Monster(randint(57, 63), randint(27, 35), "orc", item=Item(0, 0, "food", "meet", 30), talk_to_player=choice(talk['orc'])),
    Monster(randint(13, 17), randint(20, 24), "orc", item=Item(0, 0, "food", "meet", 30), talk_to_player=choice(talk['orc'])),
    Monster(randint(45, 68), 39, "orc", item=Item(0, 0, "food", "meet", 30), talk_to_player=choice(talk['orc'])),
    Monster(randint(71, 74), randint(35, 41), "troll", item=Item(0, 0, "food", "apple", 10), talk_to_player=choice(talk['troll'])),
    Monster(randint(51, 53), randint(3, 10), "troll", item=Item(0, 0, "food", "apple", 10), talk_to_player=choice(talk['troll'])),
    Monster(randint(51, 53), randint(3,7), "orc", item=Item(0, 0, "food", "meet", 30), talk_to_player=choice(talk['orc'])),
    Monster(randint(71, 74), randint(35, 41), "troll", item=Item(0, 0, "food", "apple", 10), talk_to_player=choice(talk['troll'])),
    Monster(randint(34, 36), randint(18, 22), "troll",item=Item(0, 0, "food", "apple", 10),  talk_to_player=choice(talk['troll'])),
    Monster(randint(34, 49), randint(24, 27), "troll",item=Item(0, 0, "food", "apple", 5), talk_to_player=choice(talk['troll'])),
    Monster(randint(34, 44), randint(30, 35), "orc", item=Item(0, 0, "food", "meet", 30), talk_to_player=choice(talk['orc'])),
    Monster(randint(35, 44), randint(32, 35), "troll", item=Item(0, 0, "food", "apple", 5),  talk_to_player=choice(talk['troll'])),
    Monster(randint(35, 44), randint(32, 35), "orc", item=Item(0, 0, "food", "meet", 30), talk_to_player=choice(talk['orc'])),
    Monster(randint(66, 74), randint(6, 17), "dragon", item=Item(0, 0, "armor", "plate armor", 25, index=6), talk_to_player=choice(talk['dragon'])),
    Item(randint(25, 34), randint(4, 6), "special", "rusty key"),
    Item(randint(30, 36), randint(16, 22), "weapon", "double-edged axe", 5),
    Item(randint(3, 12), randint(3, 12), "food", "apple", 20),
    Item(randint(13, 17), randint(20, 24), "food", "bread", 50)
}

map_B = GameMap(MAP_B_CHAMBERS).generate_map

player_map_C = Player(START_MAP_C['start_x'], START_MAP_C['start_y'])

entities_map_C = {
    player_map_C,
    Entity(NPC_MAP_C['start_x'], NPC_MAP_C['start_y'], NPC_MAP_C['icon'], NPC_MAP_C['color'])
}

map_C = GameMap(MAP_C).generate_map
