from __future__ import annotations

from typing import TYPE_CHECKING
from components import Player, Item, Monster
import maps

import random
import math

if TYPE_CHECKING:
    from engine import Engine


class Action:
    def __init__(self, direction_x: int, direction_y: int, type):
        self.direction_x = direction_x
        self.direction_y = direction_y
        self.type = type

    def perform(self, engine: Engine, player: Player) -> None:
        if player.hp > 0:
            if self.type == "move":
                engine.logs.clear()
                engine.talk_to.clear()
                engine.caused_damage.clear()
                engine.weapon_display.clear()
                engine.is_inventory_shown = False
                dest_x = player.x + self.direction_x
                dest_y = player.y + self.direction_y
                blocking_entity = None
                
                print(f"move: {dest_x}, {dest_y}")

                if not engine.game_map.tiles["walkable"][dest_x, dest_y]:
                    engine.logs.append("Well, you cannot go through the wall.")
                    return None  # Destination is blocked by a tile.

                if engine.game_map.get_blocking_entity(dest_x, dest_y):
                    blocking_entity = engine.game_map.get_blocking_entity(dest_x, dest_y)
                    engine.x = dest_x
                    engine.y = dest_y
                    message = blocking_entity.talk_to_player
                    engine.talk_to.append(message) if not blocking_entity.is_gate or not player.has_gate_key() else None

                    if blocking_entity.is_gate:
                        if player.has_gate_key():
                            current_map = engine.game_map

                            # map change
                            if current_map.next_map:
                                engine.game_map = current_map.next_map
                                engine.entities = current_map.next_map.entities
                                player.x = current_map.next_map.start_coords[0]
                                player.y = current_map.next_map.start_coords[1]
                                engine.entities.add(player)
                                engine.current_round += 1
                                player.remove_gate_key()
                            else:
                                engine.logs.append("Next levels under construction")
                            return
                        
                    if isinstance(blocking_entity, Monster):  # attack
                        current_attack = random.randint(player.attack - 5, player.attack + 5)
                        if random.random() > 0.2:
                            engine.logs.append(f"You attacked {blocking_entity.name} and caused {current_attack} damage.")


                        else:
                            current_attack *= 1.5
                            engine.logs.append(f"CRITICAL HIT! {blocking_entity.name.title()}'s bleeding! Caused {math.floor(current_attack)} damage.")
                        blocking_entity.current_hp -= math.floor(current_attack)


                        if blocking_entity.current_hp <= 0:
                            player.current_exp += blocking_entity.exp
                            if player.current_exp >= player.exp_to_level_up:
                                player.current_exp = player.current_exp - player.exp_to_level_up
                                player.level += 1
                                player.exp_to_level_up += 50
                                player.max_hp += 30
                                player.attack += 10
                                player.current_attack += 10
                                player.defense += 10
                                player.current_defense += 10
                                engine.logs.append(f"WOW! Level up! Your current level is {player.level}")

                            engine.logs.append(f"You've killed {blocking_entity.name}")
                            if (blocking_entity.item):
                                blocking_entity.item.x = blocking_entity.x
                                blocking_entity.item.y = blocking_entity.y
                                engine.entities.add(blocking_entity.item)
                            engine.entities.remove(blocking_entity)
                        else:
                            enemy_attack = random.randint(blocking_entity.attack - 5, blocking_entity.attack + 5)
                            if random.random() > 0.2:
                                engine.logs.append(f"{blocking_entity.name.title()} attacked you and caused {enemy_attack - player.defense} damage.")
                                engine.weapon_display.append(f'!')
                            else:
                                enemy_attack *= 1.5
                                engine.logs.append(f"CRITICAL HIT RECEIVED! {blocking_entity.name.title()}'s piercing strike caused {math.floor(enemy_attack) - player.defense} damage ")
                            player.hp -= math.floor(enemy_attack) - player.defense

                            if player.hp <= 0:
                                player.hp = 0
                                engine.logs.append(f"You died! {blocking_entity.name.title()} killed you...")
                                engine.weapon_display.append('DEAD')

                        engine.caused_damage.append(f'+{math.floor(current_attack)}')


                else:
                    player.move(self.direction_x, self.direction_y)

                # monster movement
                for entity in engine.entities:
                    if isinstance(entity, Monster) and random.random() > 0.8 and entity != blocking_entity:
                        monster_direction_x = random.randint(-1, 1)
                        monster_direction_y = random.randint(-1, 1)
                        monster_dest_x = entity.x + monster_direction_x
                        monster_dest_y = entity.y + monster_direction_y
                        if engine.game_map.tiles["walkable"][monster_dest_x, monster_dest_y]:
                            entity.move(monster_direction_x, monster_direction_y)

            elif self.type == "grab":
                engine.is_inventory_shown = False
                for single_entity in engine.entities:
                    if isinstance(single_entity, Item) and player.x == single_entity.x and player.y == single_entity.y:
                        result = player.inventory.add(single_entity)
                        if (result["is_added"]):
                            engine.entities.remove(single_entity)
                        engine.logs.append(result["message"])
                        break
                else:
                    engine.logs.append("There is nothing to pick up here")

            elif self.type == "check":
                engine.is_inventory_shown = False
                for single_entity in engine.entities:
                    if isinstance(single_entity, Item) and player.x == single_entity.x and player.y == single_entity.y:
                        article = "an" if single_entity.name[0] in "aeiou" else "a"
                        engine.logs.append(f"This is {article} {single_entity.get_description()}")
                        break
                else:
                    engine.logs.append("There is nothing interesting here")

            elif self.type == "inventory":
                engine.is_inventory_shown = True
                engine.logs.clear()
                items = player.inventory.get_items()

                if len(items) > 0:
                    cur_i = 0
                    for item_type in items:
                        items_by_type_str = ""
                        if item_type in ["food", "weapon", "armor"]:

                            items_by_type_str = ", ".join(
                                [f"[{cur_i + i + 1}] " + items[item_type][i].get_description() for i in range(len(items[item_type]))])
                            cur_i += len(items[item_type])
                        else:
                            items_by_type_str = ", ".join([single_item.get_description() for single_item in items[item_type]])
                        engine.logs.append(f"{item_type}: {items_by_type_str}")
                else:
                    engine.logs.append("Your inventory is empty")

            elif self.type in [char for char in "1234567890"] and engine.is_inventory_shown is True:
                engine.logs.clear()
                count = 0
                index = int(self.type) - 1
                items = player.inventory.get_items()
                item_type = ""
                item_to_use = ""
                item_index = None
                for key, values in items.items():
                    if key in ["food", "armor", "weapon"]:
                        for single_value in values:
                            if count == index:
                                item_type = key
                                item_to_use = single_value
                                item_index = values.index(single_value)
                            count += 1
                article = "an" if item_to_use.name in "aeiou" else "a"

                if item_type == "food":
                    player.hp = min(player.hp + item_to_use.bonus, player.max_hp)
                    engine.logs.append(f"You ate {article} {item_to_use.name}")

                elif item_type == "weapon":
                    player.current_attack = player.attack + item_to_use.bonus
                    engine.logs.append(f"Your weapon now is {article} {item_to_use.name} and your bonus attack is +{item_to_use.bonus}")

                elif item_type == "armor":
                    player.current_defense = player.defense + item_to_use.bonus
                    engine.logs.append(f"You wear {article} {item_to_use.name} and your bonus armor is +{item_to_use.bonus}")

                del player.inventory.items[item_type][item_index]
                if len(player.inventory.items[item_type]) == 0:
                    del player.inventory.items[item_type]

                    engine.is_inventory_shown = False
