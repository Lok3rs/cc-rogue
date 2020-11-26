from engine import Engine
from game_map import GameMap
from util import EventHandler
from ui import GameScreen
from settings import ORC, TROLL, DRAGON

from random import randint
from components import Entity, Player, Item, maps
from components.monsters import Monster


def play_game():
    event_handler = EventHandler()  # an instance of EventHandler class. Use it to receive events and process them

    # map_A = GameMap(maps.MAP_A).generate_map

    player_map_B = Player(maps.START_MAP_B['START_X'], maps.START_MAP_B['START_Y'])
    npc_map_B = Entity(maps.NPC_MAP_B['START_X'], maps.NPC_MAP_B['START_Y'], maps.NPC_MAP_B['ICON'], maps.NPC_MAP_B['COLOR'])
    gate_map_B = Entity(maps.GATE_MAP_B['START_X'], maps.GATE_MAP_B['START_Y'], maps.GATE_MAP_A['ICON'], maps.GATE_MAP_B['COLOR'])
    key = Item(randint(25, 34), randint(1, 5), "key", "rusty key")  # room_3
    orcs_map_b = {
        Monster(randint(11, 20), randint(31, 39), ORC["icon"], ORC["name"], ORC["max_hp"], ORC["loot"], ORC["color"], ORC["attack"]),
        Monster(randint(4, 12), randint(4, 12), ORC["icon"], ORC["name"], ORC["max_hp"], ORC["loot"], ORC["color"], ORC["attack"]),
        Monster(randint(57, 63), randint(27, 35), ORC["icon"], ORC["name"], ORC["max_hp"], ORC["loot"], ORC["color"], ORC["attack"])
    }
    trolls_map_b = {
        Monster(randint(66, 74), randint(7, 18), TROLL["icon"], TROLL["name"], TROLL["max_hp"], TROLL["loot"], TROLL["color"], TROLL["attack"]),
        Monster(randint(31, 36), randint(18, 22), TROLL["icon"], TROLL["name"], TROLL["max_hp"], TROLL["loot"], TROLL["color"], TROLL["attack"])
        
    }
    dragon_map_b = Monster(69, 39, DRAGON["icon"], DRAGON["name"], DRAGON["max_hp"], DRAGON["loot"],DRAGON["color"], DRAGON["attack"])
    entities_map_B = {npc_map_B, player_map_B, gate_map_B, key, dragon_map_b}
    entities_map_B.update(orcs_map_b, trolls_map_b)
    
    
    map_B = GameMap(maps.MAP_B).generate_map


    # player_map_C = Entity(maps.START_MAP_C['START_X'], maps.START_MAP_C['START_Y'], settings.PLAYER['ICON'], settings.PLAYER['COLOR'])
    # npc_map_C = Entity(maps.NPC_MAP_C['START_X'], maps.NPC_MAP_C['START_Y'], maps.NPC_MAP_C['ICON'], maps.NPC_MAP_C['COLOR'])
    # entities_map_C = {npc_map_C, player_map_C}
    #
    # map_C = GameMap(maps.MAP_C).generate_map

    engine = Engine(entities=entities_map_B, event_handler=event_handler, game_map=map_B, player=player_map_B)
    game = GameScreen()
    game.run_window_screen(engine)
