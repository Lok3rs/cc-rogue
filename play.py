import settings
from engine import Engine
from game_map import GameMap
from util import EventHandler
from ui import GameScreen

from random import randint
from components import Entity, Player, Item

def play_game():

    event_handler = EventHandler()  # an instance of EventHandler class. Use it to receive events and process them

    player = Player(settings.PLAYER['START_X'], settings.PLAYER['START_Y'])

    npc = Entity(settings.NPC['START_X'], settings.NPC['START_Y'], settings.NPC['ICON'], settings.NPC['COLOR'])

    gate = Entity(settings.GATE_MAP_A['START_X'], settings.GATE_MAP_A['START_Y'], settings.GATE_MAP_A['ICON'], settings.GATE_MAP_A['COLOR'])

    key = Item(randint(25, 34), randint(1, 5), "key")  # room_3

    entities = {npc, player, gate, key}

    map_1 = GameMap(settings.MAP_A).generate_map
    engine = Engine(entities=entities, event_handler=event_handler, game_map=map_1, player=player)
    game = GameScreen()
    game.run_window_screen(engine)
