"""
Напишите игру "Крестики-нолики".
"""
from pynput.keyboard import Key, Listener
from os import system as sys


def won():
    combo = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for i in combo:
        if board[i[0]] == board[i[1]] == board[i[2]] == x or board[i[0]] == board[i[1]] == board[i[2]] == o:
            return True
    return False


def del_cursor():
    if board[cursor[1]] == cursor[0]: board[cursor[1]] = " "


def released(key):
    global player, board, game
    n = 0
    if key == Key.up:
        if not cursor[1] in (6, 7, 8):
            n = 10
            if board[cursor[1] + 3] == " ":
                n = 3
            elif cursor[1] in (0, 1, 2) and board[cursor[1] + 6] == " ":
                n = 6

    if key == Key.down:
        if not cursor[1] in (0, 1, 2):
            n = 10
            if board[cursor[1] - 3] == " ":
                n = -3
            elif cursor[1] in (6, 7, 8) and board[cursor[1] - 6] == " ":
                n = -6

    if key == Key.left:
        if not cursor[1] in (0, 3, 6):
            n = 10
            if board[cursor[1] - 1] == " ":
                n = -1
            elif cursor[1] in (2, 5, 8) and board[cursor[1] - 2] == " ":
                n = -2

    if key == Key.right:
        if not cursor[1] in (2, 5, 8):
            n = 10
            if board[cursor[1] + 1] == " ":
                n = 1
            elif cursor[1] in (0, 3, 6) and board[cursor[1] + 2] == " ":
                n = 2

    if key == Key.space:
        if game:
            board[cursor[1]] = o if player else x
            if won():
                print_board(board, f"ПОБЕДИЛ {'нолик' if player else 'крестик'}! Пробел - продолжить")
                game = False
            else:
                n = 10
                player = not player
        else:
            board = [" " for i in range(9)]
            board[cursor[1]] = cursor[0]
            print_board(board, f"Пробел - сделать ход, Enter - выход. Ходит {'нолик' if player else 'крестик'} ")
            game = True

    if n == 10 and " " in board:
        n = board.index(" ") - cursor[1]

    if n and not n == 10:
        del_cursor()
        cursor[1] += n
        board[cursor[1]] = cursor[0]
        print_board(board, f"ходит {'нолик' if player else 'крестик'}")

    if key == Key.enter:
        # Stop detecting when enter key is pressed
        return False


def print_board(board, message=""):
    sys('cls')
    print(message)
    print(f' {board[6]} | {board[7]} | {board[8]} ')
    print('---|---|---')
    print(f' {board[3]} | {board[4]} | {board[5]} ')
    print('---|---|---')
    print(f' {board[0]} | {board[1]} | {board[2]} ')


if __name__ == '__main__':
    player = False  # False-крестик, True-нолик
    game = True
    cursor = ["\033[31m*\033[0m", 4]
    x = "\033[33mX\033[0m"
    o = "\033[32mO\033[0m"
    board = [" " for i in range(9)]
    board[cursor[1]] = cursor[0]
    print_board(board, f"Пробел - сделать ход, Enter - выход. Ходит {'нолик' if player else 'крестик'} ")

    with Listener(on_release=released) as detector:
        detector.join()
