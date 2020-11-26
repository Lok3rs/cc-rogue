import settings
from engine import Engine
from entity import Entity
from game_map import GameMap
from util import EventHandler
from ui import GameScreen
import maps


def play_game():

    event_handler = EventHandler() # an instance of EventHandler class. Use it to receive events and process them


    player = Entity(settings.PLAYER['START_X'], settings.PLAYER['START_Y'], settings.PLAYER['ICON'], settings.PLAYER['COLOR'])

    npc = Entity(settings.NPC['START_X'], settings.NPC['START_Y'], settings.NPC['ICON'], settings.NPC['COLOR'])

    gate = Entity(settings.GATE_MAP_A['START_X'], settings.GATE_MAP_A['START_Y'], settings.GATE_MAP_A['ICON'], settings.GATE_MAP_A['COLOR'])

    entities = {npc, player, gate}

    map_1 = GameMap(maps.MAP_A).generate_map
    engine = Engine(entities=entities, event_handler=event_handler, game_map=map_1, player=player)
    game = GameScreen()
    game.run_window_screen(engine)


