from typing import Set, Iterable, Any

from tcod.context import Context
from tcod.console import Console
import tcod
import settings

from util import EventHandler
from components import Player, GameMap


class Engine:
    def __init__(self, event_handler: EventHandler, game_map: GameMap, entity_x: int = 0, entity_y: int = 0):
        """
        Responsible of drawing the map and entities, as well as handling the player’s input.

        :param entities: is a set (of entities)
        :param event_handler: handle the events
        :param player:  is the player Entity. We have a separate reference to it outside of entities for ease of access.
        """
        self.entities = game_map.entities
        self.event_handler = event_handler
        self.game_map = game_map
        self.player = Player(game_map.start_coords[0], game_map.start_coords[1])
        self.entities.add(self.player)
        self.logs = []
        self.is_inventory_shown = False
        self.talk_to = []
        self.x = entity_x
        self.y = entity_y
        self.current_round = 1

    def handle_events(self, events: Iterable[Any]) -> None:
        """
         Pass the events to it so it can iterate through them, and it uses self.event_handler to handle the events
        """

        for event in events:

            # Send the event to event_handler’s “dispatch” method, which sends the event to its proper place.
            # In this case, a keyboard event will be sent to the ev_keydown method.
            # The Action returned from that method is assigned to local action variable.

            action = self.event_handler.dispatch(event)

            if action is None:
                continue

            action.perform(self, self.player)

    def render(self, console: Console, context: Context) -> None:
        """
        This handles drawing our screen. Iterates through the self.entities and prints them to their proper locations,
        then present the context, and clears the console
        """
        self.game_map.render(console)

        for entity in self.entities:
            console.print(entity.x, entity.y+settings.Y_MAP_START, entity.character, fg=entity.color)

        console.print(1, 1, f'HP:{self.player.hp}/{self.player.max_hp} '
                            f'ARM:{self.player.defense}+{self.player.current_defense - self.player.defense} '
                            f'ATT:{self.player.attack}+{self.player.current_attack - self.player.attack}   '
                            f'LVL:{self.player.level} EXP:{self.player.current_exp}/{self.player.exp_to_level_up}',
                            bg=(0, 0, 0), fg=(0, 255, 0)
                      )

        console.print(61, 1, f'{"NEXT LEVEL ENABLED" if self.player.has_gate_key() else ""}', bg=(0, 0, 0), fg=(0, 255, 0))

        y = settings.SCREEN["HEIGHT"] - 1
        messages_count = 1
        for message in self.logs[::-1]:
            tcod.console_set_color_control(tcod.COLCTRL_1, tcod.yellow, tcod.black)
            x = 1
            for i in range(len(message)):
                if (message[i] in "1234567890" and message[i - 1] == "[" and message[i + 1] == "]"):
                    tcod.console_print(console, x, y - messages_count, f"%c{message[i]}%c" % (tcod.COLCTRL_1, tcod.COLCTRL_1))
                else:
                    tcod.console_print(console, x, y - messages_count, message[i])
                x += 1
            messages_count += 1
            if messages_count > 4:
                break

        for message in self.talk_to:
            console.print(self.x - 10, self.y+1, message, bg=(255, 255, 255), fg=(0, 0, 0))

        context.present(console)
        console.clear()
