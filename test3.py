import random
import copy


def clear_screen():
    print(chr(27) + "[2J")  # Escape sequence to clear screen


def generate_board():
    whitelist = ['cold', 'egg', 'banana', 'fish oil',
                 'vitamin c', 'ice cream', 'code', 'workout', 'milk']
    board = [list(), list(), list()]
    for x in range(3):
        for y in range(3):
            i = random.randint(0, len(whitelist) - 1)
            activity = whitelist[i]
            del whitelist[i]
            board[x].append(activity)
    return board


# checks board if contains num
def in_board(num, board):
    for x in range(3):
        for y in range(3):
            if num == board[x][y]:
                board[x][y] = 'X'
                return True
    return False


# bool on if board meets win condition
def did_win(board):
    # check for horizontal win
    for x in range(3):
        count = 0
        for y in range(3):
            if board[y][x] != 'X':
                break
            else:
                count += 1
        if count == 3:
            return True

    # check for vertical win
    for y in range(3):
        count = 0
        for x in range(3):
            if board[y][x] != 'X':
                break
            else:
                count += 1
        if count == 3:
            return True

    # check for diagonal - top left to bottom right
    count = 0
    for i in range(3):
        if board[i][i] != 'X':
            break
        else:
            count += 1
    if count == 3:
        return True

    # check for diagnal - top right to bottom left
    count = 0
    for x in range(3):
        if board[2 - x][x] != 'X':
            break
        else:
            count += 1
    if count == 3:
        return True

    return False

# check if the number is even o
# check if


def print_board(board, og):
    print('         Marked Board          |         Board Numbers          ')
    print('-------------------------------|--------------------------------')
    for y in range(3):
        og_str = ''
        for x in range(3):
            # if board[x][y] != ' X':
                # if int(board[x][y]) < 10:
                #     print(" ", end='')
                #     og_str += ' '
            print(f'{board[x][y]:^9}', end="| ")
            og_str += f'{str(og[x][y]):^9}' + '| '
        print(og_str)


def draw(not_drawn):
    while True:
        print('Input:')
        user_input = input()
        if user_input == 'q' or not_drawn.count('X') == len(not_drawn):
            return 'q'
        elif user_input in not_drawn:
            not_drawn.remove(user_input)
            return user_input
        else:
            print('Invalid input. Try again.')


def play_game():
    not_drawn = ['cold', 'egg', 'banana', 'fish oil',
                 'vitamin c', 'ice cream', 'code', 'workout', 'milk']

    board1 = generate_board()
    og_board1 = copy.deepcopy(board1)

    clear_screen()
    print('Enter the finished activity or q to quit:')
    print_board(board1, og_board1)

    while True:
        cur_draw = draw(not_drawn)
        clear_screen()
        if cur_draw == 'q':
            print('Enter the finished activity or q to quit:')
            print_board(board1, og_board1)
            print("Game Over")
            exit()
        else:
            found = in_board(cur_draw, board1)
            print('Enter the finished activity or q to quit:')
            print_board(board1, og_board1)
            if did_win(board1):
                clear_screen()
                print('Enter the finished activity or q to quit:')
                print_board(board1, og_board1)
                print('BINGO!!! --- YOU WIN! --- Drew ' + cur_draw)
                print('GET REWARD!!!')

            else:
                if found:
                    print("Found a match! (((o(*ﾟ▽ﾟ*)o))) --- Drew " + str(cur_draw))
                else:
                    print("Bad draw. No Match. (ノ°Д°）ノ︵ ┻━┻ --- Drew " + str(cur_draw))


run_game = True
while run_game:
    run_game = play_game()
