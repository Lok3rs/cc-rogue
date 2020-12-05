import tcod.event
import tcod
from actions import Action


class EventHandler(tcod.event.EventDispatch[Action]):
    def ev_quit(self, event: tcod.event.Quit):
        raise SystemExit()

    def ev_keydown(self, event: tcod.event.KeyDown, *args):

        key = event.sym  # pressed key down

        # key bindings
        if key == tcod.event.K_w:
            return Action(direction_x=0, direction_y=-1, type="move")
        elif key == tcod.event.K_s:
            return Action(direction_x=0, direction_y=1, type="move")
        elif key == tcod.event.K_a:
            return Action(direction_x=-1, direction_y=0, type="move")
        elif key == tcod.event.K_d:
            return Action(direction_x=1, direction_y=0, type="move")
        elif key == tcod.event.K_g:
            return Action(direction_x=0, direction_y=0, type="grab")
        elif key == tcod.event.K_c:
            return Action(direction_x=0, direction_y=0, type="check")
        elif key == tcod.event.K_i:
            return Action(direction_x=0, direction_y=0, type="inventory")
        elif key == tcod.event.K_KP_1 or key == tcod.event.K_1:
            return Action(direction_x=0, direction_y=0, type="1")
        elif key == tcod.event.K_KP_2 or key == tcod.event.K_2:
            return Action(direction_x=0, direction_y=0, type="2")
        elif key == tcod.event.K_KP_3 or key == tcod.event.K_3:
            return Action(direction_x=0, direction_y=0, type="3")
        elif key == tcod.event.K_KP_4 or key == tcod.event.K_4:
            return Action(direction_x=0, direction_y=0, type="4")
        elif key == tcod.event.K_KP_5 or key == tcod.event.K_5:
            return Action(direction_x=0, direction_y=0, type="5")
        elif key == tcod.event.K_KP_6 or key == tcod.event.K_6:
            return Action(direction_x=0, direction_y=0, type="6")
        elif key == tcod.event.K_KP_7 or key == tcod.event.K_7:
            return Action(direction_x=0, direction_y=0, type="7")
        elif key == tcod.event.K_KP_8 or key == tcod.event.K_8:
            return Action(direction_x=0, direction_y=0, type="8")
        elif key == tcod.event.K_KP_9 or key == tcod.event.K_9:
            return Action(direction_x=0, direction_y=0, type="9")
        elif key == tcod.event.K_F5:
            return Action(direction_x=0, direction_y=0, type="healing_cheat")
        elif key == tcod.event.K_F6:
            return Action(direction_x=0, direction_y=0, type="attack_cheat")
        elif key == tcod.event.K_F7:
            return Action(direction_x=0, direction_y=0, type="armor_cheat")
        elif key == tcod.event.K_F12:
            return Action(direction_x=0, direction_y=0, type="key_cheat")
        elif key == tcod.event.K_ESCAPE:
            raise SystemExit
        # No valid key was pressed
