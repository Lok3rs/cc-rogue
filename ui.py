import tcod
import settings


class GameScreen:

    def __init__(self):
        self.screen_width = settings.SCREEN['WIDTH']
        self.screen_height = settings.SCREEN['HEIGHT']
        self.tileset = tcod.tileset.load_tilesheet("dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD) # Load the font, a 32 by 8 tile font  - tileset is a collection of graphical tiles.


    def run_window_screen(self, engine):

        with tcod.context.new_terminal(  # New window for a console of size columns×rows
                                        self.screen_width,
                                        self.screen_height,
                                        tileset=self.tileset,
                                        title="Roguelike",
                                        vsync=True) as context:

            # Create the main console.
            root_console = tcod.Console(self.screen_width, self.screen_height, order="F")
            while True:  # Main loop, runs until SystemExit is raised.
                engine.render(console=root_console, context=context)
                events = tcod.event.wait()
                engine.handle_events(events)


