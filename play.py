import engine
import ui
import util
import settings


def play_game():

    player = {'player_icon': settings.PLAYER_ICON, 'position_x': settings.PLAYER_START_X, 'position_y': settings.PLAYER_START_Y}
    board = ui.create_board(settings.BOARD_WIDTH, settings.BOARD_HEIGHT)

    is_running = True

    while is_running:

        board = engine.put_player_on_board(board, player)
        ui.display_board(board)

        key = util.get_move(player, board)

        if key == 'q':
            is_running = False
        if key == 'p':
            print('Heeeeeeeeloooooooooooo')

        else:
            continue
