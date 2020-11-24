import sys
import os


def key_pressed():
    try:
        import tty, termios
    except ImportError:
        try:
            # probably Windows
            import msvcrt
        except ImportError:
            # FIXME what to do on other platforms?
            raise ImportError('getch not available')
        else:
            key = msvcrt.getch().decode('utf-8')
            return key
    else:
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch



def get_move(player, board):

    key = key_pressed()

    if key == 'w':
        if player['position_y'] == 2:
            pass
        else:
            player['position_y'] -= 1

    elif key == 's':
        if player['position_y'] == len(board) - 1:
            pass
        else:
            player['position_y'] += 1

    elif key == 'a':
        if player['position_x'] == 2:
            pass
        else:
            player['position_x'] -= 1

    elif key == 'd':
        if player['position_x'] == len(board[0]) - 1:
            pass
        else:
            player['position_x'] += 1
    else:
        pass
    clear_screen()
    return key




def clear_screen():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')