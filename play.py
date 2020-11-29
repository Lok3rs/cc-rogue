from engine import Engine
from util import EventHandler
from ui import GameScreen

import maps


def play_game():
    event_handler = EventHandler()  # an instance of EventHandler class. Use it to receive events and process them
    engine = Engine(player=maps.MAP_B_PLAYER, event_handler=event_handler, game_map=maps.MAP_B)
    game = GameScreen()
    game.run_window_screen(engine)
