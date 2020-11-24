def create_board(width, height):

    board = [['-'] * width]

    for row in range(height):
        board.append(['|'] + (width-2) * [' '] + ['|'])

    board.append(['-'] * width)

    return board


def display_board(board):
    for row in board:
        for cell in row:
            print(cell, end='')
        print()
