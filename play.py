from engine import Engine
from game_map import GameMap
from util import EventHandler
from ui import GameScreen

from random import randint
from components import Entity, Player, Item, maps


def play_game():
    event_handler = EventHandler()  # an instance of EventHandler class. Use it to receive events and process them

    # map_A = GameMap(maps.MAP_A).generate_map

    player_map_B = Player(maps.START_MAP_B['START_X'], maps.START_MAP_B['START_Y'])
    npc_map_B = Entity(maps.NPC_MAP_B['START_X'], maps.NPC_MAP_B['START_Y'], maps.NPC_MAP_B['ICON'], maps.NPC_MAP_B['COLOR'])
    gate_map_B = Entity(maps.GATE_MAP_B['START_X'], maps.GATE_MAP_B['START_Y'], maps.GATE_MAP_A['ICON'], maps.GATE_MAP_B['COLOR'])
    key = Item(randint(25, 34), randint(1, 5), "key", "rusty key")  # room_3
    entities_map_B = {npc_map_B, player_map_B, gate_map_B, key}
    map_B = GameMap(maps.MAP_B).generate_map

    # player_map_C = Entity(maps.START_MAP_C['START_X'], maps.START_MAP_C['START_Y'], settings.PLAYER['ICON'], settings.PLAYER['COLOR'])
    # npc_map_C = Entity(maps.NPC_MAP_C['START_X'], maps.NPC_MAP_C['START_Y'], maps.NPC_MAP_C['ICON'], maps.NPC_MAP_C['COLOR'])
    # entities_map_C = {npc_map_C, player_map_C}
    #
    # map_C = GameMap(maps.MAP_C).generate_map

    engine = Engine(entities=entities_map_B, event_handler=event_handler, game_map=map_B, player=player_map_B)
    game = GameScreen()
    game.run_window_screen(engine)
