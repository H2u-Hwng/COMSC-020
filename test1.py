import random

class TicTacToe:

    def __init__(self):
        self.board = []
        
    def create_board(self):
        to_do_list = ['cold', 'egg', 'banana', 'fish oil', 'vitamin c', 'ice cream', 'code', 'workout', 'milk']
        
        length = len(to_do_list)
        
        for i in range(3):
            row = []
            for j in range(3):
                index = random.randint(0, length - 1)
                activity = to_do_list[index]
                row.append(activity)
                del to_do_list[index]
                
            self.board.append(row)

    def fix_spot(self, row, col):
        self.board[row][col] = "X"

    def is_player_win(self):
        win = None

        n = len(self.board)

        # checking rows
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[i][j] != "X":
                    win = False
                    break
            if win:
                return win

        # checking columns
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[j][i] != "X":
                    win = False
                    break
            if win:
                return win

        # checking diagonals
        win = True
        for i in range(n):
            if self.board[i][i] != "X":
                win = False
                break
        if win:
            return win

        win = True
        for i in range(n):
            if self.board[i][n - 1 - i] != "X":
                win = False
                break
        if win:
            return win
        return False

        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def show_board(self):
        for row in self.board:
            for item in row:
                print(f"{item:10s}|", end=" ")
            print()
    
    def end(self, limit):
        if self.board.count("X") == limit:
            return true
    
    def start(self):
        self.create_board()

        while True:
            self.show_board()

            # taking user input
            row, col = map(int, input("Enter row and column numbers to fix spot: ").split())
            print()

            # fixing the spot
            self.fix_spot(row - 1, col - 1)

            # checking whether current player is won or not
            if self.is_player_win():
                print(f"Player wins the game!")
                break
            if self.end(8):
                break
        # showing the final view of board
        print()
        self.show_board()
        
        

# starting the game
tic_tac_toe = TicTacToe()
tic_tac_toe.start()
