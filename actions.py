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
            dest_x = entity.x + self.direction_x
            dest_y = entity.y + self.direction_y

            if not engine.game_map.tiles["walkable"][dest_x, dest_y]:
                return None    # Destination is blocked by a tile.

            entity.move(self.direction_x, self.direction_y)
        elif self.type == "grab":
            for e in engine.entities:
                if isinstance(e, Item) and entity.x == e.x and entity.y == e.y:
                    entity.inventory.add(e)
                    engine.entities.remove(e)
                    break
            else:
                print("There is nothing to pick up here")
        elif self.type == "inventory":
            entity.inventory.show()
