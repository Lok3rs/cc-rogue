from __future__ import annotations

from typing import TYPE_CHECKING
from components import Player, Monster, SOUNDS
from random import randint, random, choice
from maps import MAPS_LIST
from components.item import Item

import math

if TYPE_CHECKING:
    from engine import Engine


class Action:
    def __init__(self, direction_x: int, direction_y: int, type):
        self.direction_x = direction_x
        self.direction_y = direction_y
        self.type = type


def perform(engine: Engine, player: Player, action_type: str, direction_x: int, direction_y: int, ) -> None:
    if player.hp > 0:

        if action_type == "move":
            
            engine.logs.clear()
            engine.talk_to.clear()
            engine.caused_damage.clear()
            engine.weapon_display.clear()
            engine.defense_log.clear()
            engine.attack_log.clear()
            engine.is_inventory_shown = False

            dest_x = player.x + direction_x
            dest_y = player.y + direction_y
            blocking_entity = None
            print(f"move: {dest_x}, {dest_y}")

            # Destination is blocked by a tile.
            if not engine.game_map.tiles["walkable"][dest_x, dest_y]:
                engine.logs.append("Well, you cannot go through the wall.")
                SOUNDS['bump'].play()
                return None

            # Talk to player.
            if engine.get_blocking_entity(dest_x, dest_y):
                blocking_entity = engine.get_blocking_entity(dest_x, dest_y)
                engine.entity_x = dest_x
                engine.entity_y = dest_y
                message = blocking_entity.talk_to_player
                engine.talk_to.append(message) if not blocking_entity.is_gate or not player.has_gate_key() else None

                current_map_index = MAPS_LIST.index(engine.game_map)

                # Set up next and previous map.
                if blocking_entity.is_gate:
                    if current_map_index != 0 and current_map_index != 2:
                        engine.next_map = MAPS_LIST[current_map_index + 1]
                        engine.prev_map = MAPS_LIST[current_map_index - 1]

                    elif current_map_index == 0:
                        engine.next_map = MAPS_LIST[current_map_index + 1]
                        engine.prev_map = None

                    elif current_map_index == 2:
                        engine.next_map = None
                        engine.prev_map = MAPS_LIST[current_map_index - 1]

                    # Map change
                    if player.has_gate_key() and blocking_entity.gate_to == 'next_map':
                        engine.game_map = engine.next_map
                        engine.entities = engine.next_map.entities
                        player.x = engine.next_map.start_coords[0]
                        player.y = engine.next_map.start_coords[1]
                        engine.entities.add(player)
                        SOUNDS['weapon'].play()
                        player.remove_gate_key()

                    elif blocking_entity.gate_to == 'prev_map':
                        engine.game_map = engine.prev_map
                        engine.entities = set({entity for entity in engine.prev_map.entities
                                               if not isinstance(entity, Monster) or entity.name != "dragon"})
                        player.x = engine.prev_map.finish_cords[0]
                        player.y = engine.prev_map.finish_cords[1]
                        engine.entities.add(player)
                        SOUNDS['weapon'].play()
                        if not player.has_gate_key():
                            player.inventory.add(Item('special', 'silver key', bonus=1))

                # Attack on monster
                if isinstance(blocking_entity, Monster):
                    current_attack = randint(player.attack - 5, player.attack + 5)
                    if random() > 0.1:
                        engine.attack_log.append(f"You attacked {blocking_entity.name} and "
                                                 f"caused {current_attack} damage.")
                        choice(SOUNDS['sword']).play()

                    else:
                        current_attack *= 1.5
                        SOUNDS['crit'].play()
                        engine.attack_log.append(f"CRITICAL HIT! {blocking_entity.name.title()}'s bleeding! "
                                                 f"Caused {math.floor(current_attack)} damage.")
                    blocking_entity.current_hp -= math.floor(current_attack)

                    # Player level up.
                    if blocking_entity.current_hp <= 0:
                        SOUNDS['die'].play()
                        player.current_exp += blocking_entity.exp
                        if player.current_exp >= player.exp_to_level_up:
                            SOUNDS['level_up'].play()
                            player.current_exp = player.current_exp - player.exp_to_level_up
                            player.level += 1
                            player.exp_to_level_up += 50
                            player.max_hp += 30
                            player.attack += 5
                            player.current_attack += 10
                            player.defense += 5
                            player.current_defense += 5
                            engine.logs.append(f"WOW! Level up! Your current level is {player.level}")

                        # Drop item by killed monster.
                        engine.logs.append(f"You've killed {blocking_entity.name}")
                        if blocking_entity.item:
                            blocking_entity.item.x = blocking_entity.x
                            blocking_entity.item.y = blocking_entity.y
                            engine.entities.add(blocking_entity.item)
                            engine.logs.append(f'Monster dropped {blocking_entity.item.name}')
                        if blocking_entity in engine.entities:
                            engine.entities.remove(blocking_entity)

                    else:
                        # Monster attack.
                        enemy_attack = randint(blocking_entity.attack - 5, blocking_entity.attack + 5)
                        if random() > 0.1:
                            choice(SOUNDS['monster']).play()
                            engine.defense_log.append(f"{blocking_entity.name.title()} attacked you and caused "
                                                      f"{max(0, enemy_attack - player.defense)} damage.")
                            engine.weapon_display.append(f'!')

                        else:
                            enemy_attack *= 1.5
                            engine.defense_log.append(f"CRITICAL HIT RECEIVED! {blocking_entity.name.title()}'s "
                                                      f"piercing strike caused "
                                                      f"{max(0, math.floor(enemy_attack) - player.defense)} damage ")
                        player.hp -= max(math.floor(enemy_attack) - player.defense, 0)

                        # Game over
                        if player.hp <= 0:
                            SOUNDS['game_over'][1].play().wait_done()
                            SOUNDS['game_over'][0].play()
                            player.hp = 0
                            engine.logs.append(f"You died! {blocking_entity.name.title()} killed you...")
                            engine.weapon_display.append('DEAD')

                    engine.caused_damage.append(f'+{math.floor(current_attack)}')

            # Players movement
            else:
                player.move(direction_x, direction_y)

            # Monster movement
            for entity in engine.entities:
                if isinstance(entity, Monster) and random() > 0.8 and entity != blocking_entity:
                    monster_direction_x = randint(-1, 1)
                    monster_direction_y = randint(-1, 1)
                    monster_dest_x = entity.x + monster_direction_x
                    monster_dest_y = entity.y + monster_direction_y
                    if engine.game_map.tiles["walkable"][monster_dest_x, monster_dest_y]:
                        entity.move(monster_direction_x, monster_direction_y)

        elif action_type == "grab":
            SOUNDS['pick_up'].play()
            engine.is_inventory_shown = False
            for single_entity in engine.entities:
                if isinstance(single_entity, Item) and player.x == single_entity.x and player.y == single_entity.y:
                    result = player.inventory.add(single_entity)
                    if result["is_added"]:
                        engine.entities.remove(single_entity)
                    engine.logs.append(result["message"])
                    break
            else:
                engine.logs.append("There is nothing to pick up here")

        elif action_type == "check":
            engine.is_inventory_shown = False
            for single_entity in engine.entities:
                if isinstance(single_entity, Item) and player.x == single_entity.x and player.y == single_entity.y:
                    article = "an" if single_entity.name[0] in "aeiou" else "a"
                    engine.logs.append(f"This is {article} {single_entity.get_description()}")
                    break
            else:
                engine.logs.append("There is nothing interesting here")

        # Inventory
        elif action_type == "inventory":
            SOUNDS['inv'].play()
            engine.is_inventory_shown = True
            engine.logs.clear()
            items = player.inventory.get_items()

            # Inventory to print in lower console
            if len(items) > 0:
                cur_i = 0
                for item_type in items:
                    if item_type in ["food", "weapon", "armor"]:

                        items_by_type_str = ", ".join(
                            [f"[{cur_i + i + 1}] " + items[item_type][i].get_description() for i in range(len(items[item_type]))])
                        cur_i += len(items[item_type])
                    else:
                        items_by_type_str = ", ".join([single_item.get_description() for single_item in items[item_type]])
                    engine.logs.append(f"{item_type}: {items_by_type_str}")
            else:
                engine.logs.append("Your inventory is empty")

        elif action_type in [char for char in "1234567890"] and engine.is_inventory_shown is True:
            engine.logs.clear()
            count = 0
            index = int(action_type) - 1
            items = player.inventory.get_items()
            item_type = ""
            item_to_use = None
            item_index = None

            for key, values in items.items():
                if key in ["food", "armor", "weapon"]:
                    for single_value in values:
                        if count == index:
                            item_type = key
                            item_to_use = single_value
                            item_index = values.index(single_value)
                        count += 1

            if not item_to_use:
                return

            article = "an" if item_to_use.name in "aeiou" else "a"

            if item_type == "food":
                SOUNDS['food'].play()
                player.hp = min(player.hp + item_to_use.bonus, player.max_hp)
                engine.logs.append(f"You ate {article} {item_to_use.name}")

            elif item_type == "weapon":
                SOUNDS['weapon'].play()
                player.current_attack = player.attack + item_to_use.bonus
                engine.logs.append(f"Your weapon now is {article} {item_to_use.name} and your bonus attack is"
                                   f" +{item_to_use.bonus}")

            elif item_type == "armor":
                SOUNDS['armor'].play()
                player.current_defense = player.defense + item_to_use.bonus
                engine.logs.append(f"You wear {article} {item_to_use.name} and your bonus armor is "
                                   f"+{item_to_use.bonus}")

            del player.inventory.items[item_type][item_index]
            if len(player.inventory.items[item_type]) == 0:
                del player.inventory.items[item_type]

                engine.is_inventory_shown = False

        # Cheats
        elif action_type == "healing_cheat":
            engine.logs.append("Your health is full now, but I hope it was the last time I had to help you...")
            player.hp = player.max_hp

        elif action_type == "attack_cheat":
            player.current_attack += 50
            player.attack += 50
            engine.logs.append("Weak man... I will enhance your sword.")

        elif action_type == "armor_cheat":
            player.defense += 50
            player.current_defense += 50
            engine.logs.append("I will protect your weak body.")

        elif action_type == "key_cheat":
            cheater_key = Item(type="special", name="cheater key", bonus=1)
            player.inventory.add(cheater_key)
            engine.logs.append("It seems you don't like adventures. Take the key and go away.")
