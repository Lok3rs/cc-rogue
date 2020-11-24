import settings
from engine import Engine
from entity import Entity
from game_map import GameMap
from util import EventHandler
from ui import GameScreen


def play_game():

    event_handler = EventHandler() # an instance of EventHandler class. Use it to receive events and process them

    # initialize player         x                   y                       color
    player = Entity(settings.PLAYER_START_X, settings.PLAYER_START_Y, settings.PLAYER_ICON, (0, 155, 155))

    npc = Entity(20, 20, "N", (255, 255, 0))

    entities = {npc, player}

    game_map = GameMap(settings.MAP_WIDTH, settings.MAP_HEIGHT)

    engine = Engine(entities=entities, event_handler=event_handler, game_map=game_map, player=player)

    GameScreen(engine).run_window_screen()


