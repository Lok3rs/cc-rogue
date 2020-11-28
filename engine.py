from typing import Set, Iterable, Any

from tcod.context import Context
from tcod.console import Console
import tcod
import settings

from game_map import GameMap
from util import EventHandler
from components import Entity, Player


class Engine:
    def __init__(self, entities: Set[Entity], event_handler: EventHandler, game_map: GameMap, player: Player, entity_x: int = 0, entity_y: int = 0):
        """
        Responsible of drawing the map and entities, as well as handling the player’s input.

        :param entities: is a set (of entities)
        :param event_handler: handle the events
        :param player:  is the player Entity. We have a separate reference to it outside of entities for ease of access.
        """
        self.entities = entities
        self.event_handler = event_handler
        self.game_map = game_map
        self.player = player
        self.logs = []
        self.is_inventory_shown = False
        self.talk_to = []
        self.x = entity_x
        self.y = entity_y

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

        # Draw the player's HP bar.
        # tcod.console_print_ex(console, 8, 1, tcod.BKGND_NONE, tcod.CENTER, '{0}: {1}/{2}'.format("HP", self.player.hp, self.player.max_hp))
        # tcod.console_print_ex(console, 25, 1, tcod.BKGND_NONE, tcod.CENTER,'{}: {}+{}'.format("ATK", self.player.attack, self.player.current_attack - self.player.attack))
        # tcod.console_print_ex(console, 40, 1, tcod.BKGND_NONE, tcod.CENTER, '{}: {}+{}'.format("DEF", self.player.defense, self.player.current_defense-self.player.defense))

        console.print(3, 1, f'HP:{self.player.hp}/{self.player.max_hp} ARM:{self.player.defense}+{self.player.current_defense - self.player.defense} '
                            f'ATT:{self.player.attack}+{self.player.current_attack - self.player.attack}', bg=(0, 0, 0), fg=(0, 255, 0))

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
