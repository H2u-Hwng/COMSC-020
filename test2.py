import random


def clear_screen():
    print(chr(27) + "[2J")  # Escape sequence to clear screen


def generate_board():
    print('How may activities do you want to enter?')
    num_activities = int(input())

    activities = []

    for i in range(num_activities):
        print('Enter activity ' + str(i + 1) + ':')
        activity = input()
        activities.append(activity)

    side = find_side(num_activities)

    for i in range(side ** 2 - num_activities):
        activities.append('X')

    random.shuffle(activities)

    board = []
    for i in range(0, len(activities), side):
        board.append(activities[i: i + side])

    return board


def in_board(activity, board):
    for activities in board:
        if activity in activities:
            activities.replace(activity, 'X')
            return True
    return False


def check_bingo(array):
    """
    Check if bingo in an array
    """

    l = len(array)

    # check for horizontal win
    for x in range(l):
        count = 0
        for y in range(l):
            if array[y][x] != 'X':
                break
            else:
                count += 1
        if count == l:
            return True

    # check for vertical win
    for y in range(l):
        count = 0
        for x in range(l):
            if array[y][x] != 'X':
                break
            else:
                count += 1
        if count == 5:
            return True

    # check for diagonal - top left to bottom right
    count = 0
    for i in range(l):
        if array[i][i] != 'X':
            break
        else:
            count += 1
    if count == l:
        return True

    # check for diagonal - top right to bottom left
    count = 0
    for x in range(l):
        if array[l - 1 - x][x] != 'X':
            break
        else:
            count += 1
    if count == l:
        return True

    return False


def print_board(board):
    print('Productivity Bingo Board')
    for y in range(len(board)):
        for x in range(len(board)):
            print(f'{board[x][y]:5}', end=' ')
        print()


def play_board():
    board = generate_board()

    clear_screen()
    print_board(board)

    while True:
        print('Enter the activity you finished or q to quit:')
        user = input()
        if user == 'q':
            print_board(board)
            print('Game Over')
            exit()
        else:
            in_board(board, user)
            if check_bingo(board):
                while True:
                    clear_screen()
                    print_board(board)
                    print('Winner! Enter "new" to start new game. Enter "q" to quit.')
                    user = input()
                    if user == 'new':
                        return True
                    elif user == 'q':
                        print('Game Over')
                        return False


def find_side(square):
    """
    Find the side of a square
    """
    while not (square ** 0.5).is_integer():
        square += 1

    return int(square ** 0.5)

