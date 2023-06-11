import time


class Board:
    def __init__(self):
        self.board = [[' ' for _ in range(8)] for _ in range(7)]
        self.winning_sequence_len = 4

    def print_board(self):
        # print column numbers with lines
        for i in range(8):
            print('|' + str(i + 1), end='')
        print('|')

        print('-' * 15)

        # print board, match symbols with column numbers with spaces
        for i in range(7):
            for j in range(8):
                print('|' + self.board[i][j], end='')
            print('|')

        print('-' * 15)

    def insert(self, symbol, column):
        # check if column is within range
        if column < 0 or column > 7:
            return False

        if self.is_column_full(column):
            return False

        # place symbol in bottom of column or on top of other symbol
        # reverse for loop
        for i in range(6, -1, -1):
            if self.board[i][column] == ' ':
                self.board[i][column] = symbol
                return True

    def check_win(self, symbol):
        # Check if there are 4 symbols in a line
        # check horizontal
        win = False

        window = self.winning_sequence_len * [symbol]

        # check horizontal using sliding window
        for i in range(7):
            for j in range(5):
                if self.board[i][j:j + 4] == window:
                    win = True

        # check vertical using sliding window
        for i in range(4):
            for j in range(8):
                if [self.board[i][j], self.board[i + 1][j], self.board[i + 2][j], self.board[i + 3][j]] == window:
                    win = True

        # check diagonal using sliding window
        for i in range(4):
            for j in range(5):
                if [self.board[i][j], self.board[i + 1][j + 1], self.board[i + 2][j + 2],
                    self.board[i + 3][j + 3]] == window:
                    win = True

        # check diagonal using sliding window
        for i in range(4):
            for j in range(3, 8):
                if [self.board[i][j], self.board[i + 1][j - 1], self.board[i + 2][j - 2],
                    self.board[i + 3][j - 3]] == window:
                    win = True

        return win

    def is_column_full(self, column):
        return self.board[0][column] != ' '

    def is_full(self):
        for column in range(8):
            if not self.is_column_full(column):
                return False
        return True
