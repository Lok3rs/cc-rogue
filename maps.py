from components import Entity, Item, Monster, GameMap, Chamber
from random import choice


GATE = {
    'icon': 'GA',
    'icon_2': 'TE',
    'color': (255, 0, 0)
}

TALK = {
    'npc': ['Save us from Dragon!', 'Dragon has the...key!'],
    'orc': ['Orc: Grrrrrrrrrr..!', 'Orc: You will die!', "Orc: Let's Fight!", 'Orc: You have no chance!'],
    'troll': ['Troll: Ha Ha Ha Ha', 'Troll: I will eat your flesh!', 'Troll: Tou choose wrong place...'],
    'dragon': ['Dragon: Hrrrrr.....'],
    'gate': ['You need key!']
}

MAP_A_START_COORDS = (0, 35)

GATE_MAP_A_1 = {
    'start_x': 78,
    'start_y': 36,
}

GATE_MAP_A_2 = {
    'start_x': 78,
    'start_y': 37,
}

NPC_MAP_A = {

    'icon': 'N',
    'start_x': 15,
    'start_y': 35,
    'color': (255, 0, 0)
}

MAP_A_CHAMBERS = {
    'room_1': Chamber(x=10, y=30, width=10, height=10).get_range,
    'room_2': Chamber(x=65, y=5, width=10, height=15).get_range,
    'room_3': Chamber(x=25, y=3, width=10, height=5).get_range,
    'room_4': Chamber(x=13, y=20, width=5, height=5).get_range,
    'room_5': Chamber(x=35, y=33, width=10, height=10).get_range,
    'room_6': Chamber(x=3, y=3, width=10, height=10).get_range,
    'room_7': Chamber(x=30, y=16, width=7, height=7).get_range,
    'room_8': Chamber(x=50, y=3, width=5, height=9).get_range,
    'room_9': Chamber(x=56, y=26, width=8, height=10).get_range,
    'room_10': Chamber(x=70, y=34, width=8, height=10).get_range,
    'room_11': Chamber(x=43, y=24, width=8, height=4).get_range,
    'dungeon_0': Chamber(x=0, y=35, width=10, height=1).get_range,
    'dungeon_1': Chamber(x=13, y=5, width=12, height=1).get_range,
    'dungeon_2': Chamber(x=20, y=35, width=15, height=1).get_range,
    'dungeon_4': Chamber(x=6, y=13, width=1, height=30).get_range,
    'dungeon_5': Chamber(x=15, y=25, width=1, height=5).get_range,
    'dungeon_6': Chamber(x=17, y=6, width=1, height=14).get_range,
    'dungeon_7': Chamber(x=17, y=9, width=33, height=1).get_range,
    'dungeon_8': Chamber(x=45, y=39, width=25, height=1).get_range,
    'dungeon_9': Chamber(x=33, y=26, width=10, height=1).get_range,
    'dungeon_10': Chamber(x=32, y=9, width=1, height=18).get_range,
    'dungeon_11': Chamber(x=49, y=32, width=8, height=1).get_range,
    'dungeon_12': Chamber(x=60, y=30, width=11, height=1).get_range,
    'dungeon_13': Chamber(x=48, y=27, width=1, height=6).get_range,
    'dungeon_14': Chamber(x=70, y=20, width=1, height=10).get_range,
    'dungeon_22': Chamber(x=74, y=36, width=5, height=2).get_range,
    'dungeon_23': Chamber(x=6, y=43, width=20, height=1).get_range,
    'dungeon_24': Chamber(x=25, y=36, width=1, height=7).get_range,

}

MAP_A_ENTITIES = {
    Entity(NPC_MAP_A['start_x'], NPC_MAP_A['start_y'], NPC_MAP_A['icon'], NPC_MAP_A['color'], block_movement=True, talk_to_player=choice(TALK['npc'])),
    Entity(GATE_MAP_A_1['start_x'], GATE_MAP_A_1['start_y'], GATE['icon'], GATE['color'], is_gate=True, block_movement=True, talk_to_player=choice(TALK['gate'])),
    Entity(GATE_MAP_A_2['start_x'], GATE_MAP_A_2['start_y'], GATE['icon_2'], GATE['color'], is_gate=True, block_movement=True, talk_to_player=choice(TALK['gate'])),
    Monster("orc", item=Item("food", "meet", bonus=30), talk_to_player=choice(TALK['orc'])).put_on_map(MAP_A_CHAMBERS["room_1"]),
    Monster("orc", item=Item("food", "meet", bonus=30), talk_to_player=choice(TALK['orc'])).put_on_map(MAP_A_CHAMBERS["room_6"]),
    Monster("orc", item=Item("weapon", "rusted sabre", bonus=5), talk_to_player=choice(TALK['orc'])).put_on_map(MAP_A_CHAMBERS["room_6"]),
    Monster("orc", item=Item("food", "meet", bonus=30), talk_to_player=choice(TALK['orc'])).put_on_map(MAP_A_CHAMBERS["room_9"]),
    Monster("orc", item=Item("food", "meet", bonus=30), talk_to_player=choice(TALK['orc'])).put_on_map(MAP_A_CHAMBERS["room_4"]),
    Monster("orc", item=Item("food", "meet", bonus=30), talk_to_player=choice(TALK['orc'])).put_on_map(MAP_A_CHAMBERS["dungeon_10"]),
    Monster("troll", item=Item("food", "apple", bonus=10), talk_to_player=choice(TALK['troll'])).put_on_map(MAP_A_CHAMBERS["room_10"]),
    Monster("troll", item=Item("food", "apple", bonus=10), talk_to_player=choice(TALK['troll'])).put_on_map(MAP_A_CHAMBERS["room_8"]),
    Monster("orc", item=Item("food", "meet", bonus=30), talk_to_player=choice(TALK['orc'])).put_on_map(MAP_A_CHAMBERS["room_8"]),
    Monster("troll", item=Item("food", "apple", bonus=10), talk_to_player=choice(TALK['troll'])).put_on_map(MAP_A_CHAMBERS["room_10"]),
    Monster("troll",item=Item("food", "apple", bonus=10),  talk_to_player=choice(TALK['troll'])).put_on_map(MAP_A_CHAMBERS["room_7"]),
    Monster("troll",item=Item("food", "apple", bonus=5), talk_to_player=choice(TALK['troll'])).put_on_map(MAP_A_CHAMBERS["room_7"]),
    Monster("orc", item=Item("food", "meet", bonus=30), talk_to_player=choice(TALK['orc'])).put_on_map(MAP_A_CHAMBERS["room_3"]),
    Monster("troll", item=Item("food", "apple", bonus=5),  talk_to_player=choice(TALK['troll'])).put_on_map(MAP_A_CHAMBERS["room_5"]),
    Monster("orc", item=Item("food", "meet", bonus=30), talk_to_player=choice(TALK['orc'])).put_on_map(MAP_A_CHAMBERS["room_5"]),
    Monster("dragon", item=Item("special", "golden key", bonus=1), talk_to_player=choice(TALK['dragon'])).put_on_map(MAP_A_CHAMBERS["room_2"]),
    Item("armor", "bronze armor", bonus=5).put_on_map(MAP_A_CHAMBERS["room_3"]),
    Item("weapon", "double-edged axe", bonus=5).put_on_map(MAP_A_CHAMBERS["room_7"]),
    Item("food", "apple", bonus=20).put_on_map(MAP_A_CHAMBERS["room_6"]),
    Item("food", "bread", bonus=50).put_on_map(MAP_A_CHAMBERS["room_4"]),
    Item("special", "rusty key", bonus=1).put_on_map(MAP_A_CHAMBERS["room_1"]),
}

MAP_B_START_COORDS = (0, 35)

GATE_MAP_B = {
    'start_x': 77,
    'start_y': 35,
}

NPC_MAP_B = {
    'icon': 'N',
    'start_x': 15,
    'start_y': 35,
    'color': (255, 0, 0)
}

MAP_B_CHAMBERS = {
    'room_1': Chamber(x=44, y=10, width=30, height=30).get_range,
    'room_2': Chamber(x=5, y=3, width=10, height=8).get_range,
    'room_3': Chamber(x=5, y=30, width=10, height=8).get_range,
    'room_4': Chamber(x=30, y=20, width=5, height=5).get_range,
    'room_5': Chamber(x=23, y=33, width=10, height=10).get_range,
    'room_6': Chamber(x=23, y=12, width=8, height=5).get_range,
    'room_7': Chamber(x=8, y=20, width=5, height=5).get_range,
    'dungeon_0': Chamber(x=0, y=35, width=26, height=1).get_range,
    'dungeon_1': Chamber(x=13, y=5, width=40, height=1).get_range,
    'dungeon_4': Chamber(x=26, y=5, width=1, height=29).get_range,
    'dungeon_7': Chamber(x=12, y=22, width=20, height=1).get_range,
    'dungeon_11': Chamber(x=53, y=5, width=1, height=5).get_range,
    'dungeon_14': Chamber(x=10, y=11, width=1, height=10).get_range,
}

MAP_B_ENTITIES = {
    Entity(NPC_MAP_B['start_x'], NPC_MAP_B['start_y'], NPC_MAP_B['icon'], NPC_MAP_B['color']),
    Entity(GATE_MAP_B['start_x']-20, GATE_MAP_B['start_y'], GATE['icon'], GATE['color'], is_gate=True, block_movement=True, talk_to_player=choice(TALK['gate'])),
    Item("special", "silver key", bonus=1).put_on_map(MAP_B_CHAMBERS["room_1"])
}

MAP_C_START_COORDS = (0, 5)

MAP_C_CHAMBERS = {
    'room_1': Chamber(x=10, y=5, width=10, height=10).get_range,
    'room_2': Chamber(x=35, y=15, width=10, height=15).get_range,
    'room_3': Chamber(x=25, y=1, width=10, height=5).get_range,
    'room_4': Chamber(x=45, y=2, width=5, height=5).get_range,
    'room_5': Chamber(x=2, y=30, width=10, height=10).get_range,
    'room_6': Chamber(x=65, y=30, width=10, height=10).get_range,
    'room_7': Chamber(x=55, y=20, width=7, height=7).get_range,
    'room_8': Chamber(x=15, y=20, width=8, height=9).get_range,
    'room_9': Chamber(x=5, y=30, width=8, height=10).get_range,
    'room_10': Chamber(x=30, y=34, width=8, height=10).get_range,
    'room_11': Chamber(x=60, y=3, width=8, height=10).get_range,
    'room_12': Chamber(x=50, y=35, width=6, height=6).get_range,
    'dungeon_0': Chamber(x=0, y=5, width=5, height=1).get_range,
    'dungeon_1': Chamber(x=15, y=3, width=1, height=3).get_range,
    'dungeon_2': Chamber(x=16, y=3, width=10, height=1).get_range,
    'dungeon_4': Chamber(x=4, y=5, width=1, height=25).get_range,
    'dungeon_5': Chamber(x=12, y=37, width=6, height=1).get_range,
    'dungeon_6': Chamber(x=17, y=29, width=1, height=13).get_range,
    'dungeon_7': Chamber(x=13, y=9, width=12, height=1).get_range,
    'dungeon_8': Chamber(x=5, y=12, width=5, height=1).get_range,
    'dungeon_9': Chamber(x=23, y=22, width=3, height=1).get_range,
    'dungeon_10': Chamber(x=25, y=9, width=1, height=13).get_range,
    'dungeon_11': Chamber(x=26, y=12, width=35, height=1).get_range,
    'dungeon_12': Chamber(x=45, y=5, width=15, height=1).get_range,
    'dungeon_13': Chamber(x=17, y=42, width=13, height=1).get_range,
    'dungeon_14': Chamber(x=38, y=37, width=13, height=1).get_range,
    'dungeon_15': Chamber(x=52, y=24, width=1, height=11).get_range,
    'dungeon_17': Chamber(x=42, y=24, width=10, height=1).get_range,
    'dungeon_18': Chamber(x=42, y=17, width=16, height=1).get_range,
    'dungeon_19': Chamber(x=58, y=17, width=1, height=3).get_range,
    'dungeon_20': Chamber(x=58, y=27, width=1, height=7).get_range,
    'dungeon_21': Chamber(x=59, y=33, width=7, height=1).get_range,
    'dungeon_22': Chamber(x=74, y=36, width=5, height=2).get_range,
    'dungeon_23': Chamber(x=68, y=9, width=5, height=1).get_range,
    'dungeon_24': Chamber(x=72, y=10, width=1, height=20).get_range,
}

MAP_C_ENTITIES = set()

MAP_C = GameMap(MAP_C_START_COORDS, MAP_C_CHAMBERS, MAP_C_ENTITIES).generate_map()
MAP_B = GameMap(MAP_B_START_COORDS, MAP_B_CHAMBERS, MAP_B_ENTITIES, next_map=MAP_C).generate_map()
MAP_A = GameMap(MAP_A_START_COORDS, MAP_A_CHAMBERS, MAP_A_ENTITIES, next_map=MAP_B).generate_map()
