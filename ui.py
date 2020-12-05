import tcod
import settings


class GameScreen:

    def __init__(self):
        self.screen_width = settings.SCREEN['WIDTH']
        self.screen_height = settings.SCREEN['HEIGHT']
        # Load the font, a 32 by 8 tile font  - tileset is a collection of graphical tiles.
        self.tileset = tcod.tileset.load_tilesheet("components/dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD)
        self.game_on = False

    def main_menu(self, console, context):

        # show the game's title, and some credits!
        title = "Select your character race"
        options = ["Human", "Dwarf", "Elf", "Tiefling"]

        tcod.console_set_default_foreground(console, tcod.light_yellow)
        tcod.console_print(console, int(settings.SCREEN["WIDTH"]/2 - len(title)/2),
                           int(settings.SCREEN["HEIGHT"]/2 - len(options)/2 - 2), title)

        # print all the options
        tcod.console_set_default_foreground(console, tcod.white)

        y = int(settings.SCREEN["HEIGHT"]/2 - len(options)/2)
        x = int(settings.SCREEN["WIDTH"]/2 - max([len(x) for x in options])/2) - 3
        letter_index = ord('A')
        for option_text in options:
            text = '(' + chr(letter_index) + ') ' + option_text
            tcod.console_print(console, x, y, text)
            y += 1
            letter_index += 1

        context.present(console)

        choice = None
        while choice is None:
            key = tcod.console_wait_for_keypress(True)
            if key.vk == tcod.KEY_ESCAPE or key.vk == tcod.KEY_NONE:
                raise SystemExit()

            index = key.c - ord('a')
            if 0 <= index < len(options):
                choice = index

        self.game_on = True
        return options[choice]

    def run_window_screen(self, engine):
        with tcod.context.new_terminal(  # New window for a console of size columns×rows
                self.screen_width,
                self.screen_height,
                tileset=self.tileset,
                title="Dungeons&Dragons",
                vsync=True) as context:
            # Create the main console.
            root_console = tcod.Console(self.screen_width, self.screen_height, order="F")

            if not self.game_on:
                race = self.main_menu(root_console, context)
                engine.player.set_race(race)
            if self.game_on and engine.player.race:
                while True:  # Main loop, runs until SystemExit is raised.
                    engine.render(console=root_console, context=context)
                    events = tcod.event.wait()
                    engine.handle_events(events)
