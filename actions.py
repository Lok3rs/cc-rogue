from __future__ import annotations

from typing import TYPE_CHECKING
from components import Player, Item
from components.monsters import Monster

import random
import math
from copy import deepcopy

if TYPE_CHECKING:
    from engine import Engine



class Action:
    def __init__(self, direction_x: int, direction_y: int, type):
        self.direction_x = direction_x
        self.direction_y = direction_y
        self.type = type

    def perform(self, engine: Engine, player: Player) -> None:
        if player._hp > 0:
            if self.type == "move":
                engine.logs.clear()
                engine.is_inventory_shown = False
                dest_x = player.x + self.direction_x
                dest_y = player.y + self.direction_y
                print(f"move: {dest_x}, {dest_y}")

                if not engine.game_map.tiles["walkable"][dest_x, dest_y]:
                    print('Wall blocked...')
                    return None  # Destination is blocked by a tile.
                if engine.game_map.get_blocking_entity(engine.entities, dest_x, dest_y):
                    entity = engine.game_map.get_blocking_entity(engine.entities, dest_x, dest_y)
                    # ATTACK
                    if isinstance(entity, Monster):
                        current_attack = random.randint(player.attack - 5, player.attack + 5)
                        if random.random() > 0.2:
                            engine.logs.append(f"You attacked {entity.name} and caused {current_attack} damage.")
                        else:
                            current_attack *= 1.5
                            engine.logs.append(f"CRITICAL HIT! {entity.name.title()}'s bleeding! Caused {math.floor(current_attack)} damage.")
                        entity.current_hp -= math.floor(current_attack)

                        if entity.current_hp <= 0:
                            engine.logs.append(f"You've killed {entity.name}")
                            for single_entity in engine.entities:
                                if isinstance(single_entity, Item) and single_entity.index == entity.index:
                                    single_entity.x = entity.x
                                    single_entity.y = entity.y
                            entity.x = -1
                            entity.y = -1



                        else:
                            enemy_attack = random.randint(entity.attack - 5, entity.attack + 5)
                            if random.random() > 0.2:
                                engine.logs.append(f"{entity.name.title()} attacked you and caused {enemy_attack} damage.")
                            else:
                                enemy_attack *= 1.5
                                engine.logs.append(f"CRITICAL HIT RECEIVED! {entity.name.title()}'s piercing strike caused {math.floor(enemy_attack)} damage ")
                            player._hp -= math.floor(enemy_attack)

                            if player._hp <= 0:
                                player._hp = 0
                                engine.logs.append(f"You died! {entity.name.title()} killed you...")

                    return None

                player.move(self.direction_x, self.direction_y)
            elif self.type == "grab":
                engine.is_inventory_shown = False
                for single_entity in engine.entities:
                    if isinstance(single_entity, Item) and player.x == single_entity.x and player.y == single_entity.y:
                        messsage = player.inventory.add(single_entity)
                        engine.entities.remove(single_entity)
                        engine.logs.append(messsage)
                        break
                else:
                    engine.logs.append("There is nothing to pick up here")
            elif self.type == "check":
                engine.is_inventory_shown = False
                for single_entity in engine.entities:
                    if isinstance(single_entity, Item) and player.x == single_entity.x and player.y == single_entity.y:
                        article = "an" if single_entity.name[0] in "aeiou" else "a"
                        engine.logs.append(f"This is {article} {single_entity.name}")
                        break
                else:
                    engine.logs.append("There is nothing interesting here")
            elif self.type == "inventory":
                engine.is_inventory_shown = True
                engine.logs.clear()
                items = player.inventory.get_items()
                if (len(items) > 0):
                    for item_type in items:
                        items_by_type_str = ""
                        if item_type == "food":
                            items_by_type_str = ", ".join([f"[{i+1}] "+items[item_type][i].name for i in range(len(items[item_type]))])
                        else:
                            items_by_type_str = ", ".join([single_item.name for single_item in items[item_type]])
                        engine.logs.append(f"{item_type}: {items_by_type_str}")
                else:
                    engine.logs.append("Your inventory is empty")
            elif self.type in "1234567890" and engine.is_inventory_shown is True:
                engine.logs.clear()

                index = int(self.type) - 1
                item_to_eat = player.inventory.items["food"][index]
                player._hp = min(player._hp + item_to_eat.bonus, player.max_hp)
                del player.inventory.items["food"][index]
                if len(player.inventory.items["food"]) == 0:
                    del player.inventory.items["food"]

                article = "an" if item_to_eat.name in "aeiou" else "a"
                engine.logs.append(f"You ate {article} {item_to_eat.name}")

                engine.is_inventory_shown = False
