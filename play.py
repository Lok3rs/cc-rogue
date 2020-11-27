from engine import Engine
from util import EventHandler
from ui import GameScreen

from components import maps


def play_game():

    event_handler = EventHandler()  # an instance of EventHandler class. Use it to receive events and process them
    engine = Engine(player=maps.player_map_B, entities=maps.entities_map_B, event_handler=event_handler, game_map=maps.map_B)
    game = GameScreen()
    game.run_window_screen(engine)
