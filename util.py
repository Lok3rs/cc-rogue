from typing import Optional
import tcod.event
from actions import Action


class EventHandler(tcod.event.EventDispatch[Action]):
    def ev_quit(self, event: tcod.event.Quit) -> Optional[Action]:
        raise SystemExit()


    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]:
        action: Optional[Action] = None

        key = event.sym  #pressed key down

        # key bindings
        if key == tcod.event.K_w:
            action = Action(direction_x=0, direction_y=-1)
        elif key == tcod.event.K_s:
            action = Action(direction_x=0, direction_y=1)
        elif key == tcod.event.K_a:
            action = Action(direction_x=-1, direction_y=0)
        elif key == tcod.event.K_d:
            action = Action(direction_x=1, direction_y=0)

        elif key == tcod.event.K_ESCAPE:
            raise SystemExit
        # No valid key was pressed
        return action
