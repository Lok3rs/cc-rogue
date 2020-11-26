from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from engine import Engine
    from entity import Entity


class Action:
    def __init__(self, direction_x: int, direction_y: int):
        self.direction_x = direction_x
        self.direction_y = direction_y

    def perform(self, engine: Engine, entity: Entity) -> None:
        dest_x = entity.x + self.direction_x
        dest_y = entity.y + self.direction_y

        if not engine.game_map.tiles["walkable"][dest_x, dest_y]:
            return None  # Destination is blocked by a tile.

        entity.move(self.direction_x, self.direction_y)
