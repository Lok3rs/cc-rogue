from __future__ import annotations

from typing import TYPE_CHECKING
from components import Entity, Item

if TYPE_CHECKING:
    from engine import Engine


class Action:
    def __init__(self, direction_x: int, direction_y: int, type):
        self.direction_x = direction_x
        self.direction_y = direction_y
        self.type = type

    def perform(self, engine: Engine, entity: Entity) -> None:

        if self.type == "move":
            engine.logs.clear()
            dest_x = entity.x + self.direction_x
            dest_y = entity.y + self.direction_y

            if not engine.game_map.tiles["walkable"][dest_x, dest_y]:
                return None  # Destination is blocked by a tile.
            if engine.game_map.get_blocking_entity(engine.entities, dest_x, dest_y):
                return None

            entity.move(self.direction_x, self.direction_y)
        elif self.type == "grab":
            for single_entity in engine.entities:
                if isinstance(single_entity, Item) and entity.x == single_entity.x and entity.y == single_entity.y:
                    messsage = entity.inventory.add(single_entity)
                    engine.entities.remove(single_entity)
                    engine.logs.append(messsage)
                    break
            else:
                engine.logs.append("There is nothing to pick up here")
        elif self.type == "check":
            for single_entity in engine.entities:
                if isinstance(single_entity, Item) and entity.x == single_entity.x and entity.y == single_entity.y:
                    article = "an" if single_entity.name[0] in "aeiou" else "a"
                    engine.logs.append(f"This is {article} {single_entity.name}")
                    break
            else:
                engine.logs.append("There is nothing interesting here")
        elif self.type == "inventory":
            entity.inventory.show()
