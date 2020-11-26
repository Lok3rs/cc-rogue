from __future__ import annotations

from typing import TYPE_CHECKING
from components import Player, Item

if TYPE_CHECKING:
    from engine import Engine


class Action:
    def __init__(self, direction_x: int, direction_y: int, type):
        self.direction_x = direction_x
        self.direction_y = direction_y
        self.type = type

    def perform(self, engine: Engine, player: Player) -> None:

        if self.type == "move":
            engine.logs.clear()
            dest_x = player.x + self.direction_x
            dest_y = player.y + self.direction_y
            print(f"move: {dest_x}, {dest_y}")

            if not engine.game_map.tiles["walkable"][dest_x, dest_y]:
                print('Wall blocked...')
                return None  # Destination is blocked by a tile.
            if engine.game_map.get_blocking_entity(engine.entities, dest_x, dest_y):
                print('Entity blocked...')
                return None

            player.move(self.direction_x, self.direction_y)
        elif self.type == "grab":
            for single_entity in engine.entities:
                if isinstance(single_entity, Item) and player.x == single_entity.x and player.y == single_entity.y:
                    messsage = player.inventory.add(single_entity)
                    engine.entities.remove(single_entity)
                    engine.logs.append(messsage)
                    break
            else:
                engine.logs.append("There is nothing to pick up here")
        elif self.type == "check":
            for single_entity in engine.entities:
                if isinstance(single_entity, Item) and player.x == single_entity.x and player.y == single_entity.y:
                    article = "an" if single_entity.name[0] in "aeiou" else "a"
                    engine.logs.append(f"This is {article} {single_entity.name}")
                    break
            else:
                engine.logs.append("There is nothing interesting here")
        elif self.type == "inventory":
            player.inventory.show()
