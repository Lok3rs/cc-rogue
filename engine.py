from typing import Set, Iterable, Any

from tcod.context import Context
from tcod.console import Console
import tcod
import settings

from game_map import GameMap
from util import EventHandler
from components import Entity


class Engine:
    def __init__(self, entities: Set[Entity], event_handler: EventHandler, game_map: GameMap, player: Entity):
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

    def handle_events(self, events: Iterable[Any]) -> None:
        """
         Pass the events to it so it can iterate through them, and it uses self.event_handler to handle the events
        """

        for event in events:

            # Send the event to event_handler’s “dispatch” method, which sends the event to its proper place.
            # In this case, a keyboard event will be sent to the ev_keydown method. The Action returned from that method is assigned to local action variable.

            action = self.event_handler.dispatch(event)

            if action is None:
                continue

            action.perform(self, self.player)

    def render(self, console: Console, context: Context) -> None:
        """
        This handles drawing our screen. Iterates through the self.entities and prints them to their proper locations, then present the context, and clears the console
        """
        self.game_map.render(console)

        for entity in self.entities:
            console.print(entity.x, entity.y, entity.character, fg=entity.color)

        # Draw the player's HP bar.
        tcod.console_print_ex(console, 8, 1, tcod.BKGND_NONE, tcod.CENTER, '{0}: {1}/{2}'.format("HP", self.player.hp, self.player.max_hp))

        y = settings.SCREEN["HEIGHT"] - 1
        i = 1
        for message in self.logs[::-1]:
            tcod.console_print_ex(console, 1, y-i, tcod.BKGND_NONE, tcod.LEFT, message)
            i += 1
            if i > 4: break

        context.present(console)
        console.clear()
