class Board:
    def __init__(self):
        self.board = [[' ' for _ in range(7)] for _ in range(8)]

    def print_board(self):
        # print column numbers with lines
        for i in range(7):
            print('|' + str(i + 1), end='')
        print('|')

        print('-' * 15)

        # print board, match symbols with column numbers with spaces
        for i in range(8):
            for j in range(7):
                print('|' + self.board[i][j], end='')
            print('|')

        print('-' * 15)

    def insert(self, symbol, column):
        # check if column is within range
        if column < 0 or column > 6:
            return False

        if self.is_column_full(column):
            return False

        # place symbol in bottom of column or on top of other symbol
        # reverse for loop
        for i in range(7, -1, -1):
            if self.board[i][column] == ' ':
                self.board[i][column] = symbol
                return True

    def check_win(self, symbol):
        # Check if there are 4 symbols in a line
        # check horizontal
        win = False
        for row in self.board:
            for i in range(4):
                if row[i] == row[i + 1] == row[i + 2] == row[i + 3] == symbol:
                    win = True

        # check vertical
        for i in range(7):
            for j in range(5):
                if self.board[j][i] == self.board[j + 1][i] == self.board[j + 2][i] == self.board[j + 3][i] == symbol:
                    win = True

        # check diagonal
        for i in range(4):
            for j in range(5):
                if self.board[j][i] == self.board[j + 1][i + 1] == self.board[j + 2][i + 2] == self.board[j + 3][
                    i + 3] == symbol:
                    win = True

        # check other diagonal
        for i in range(4):
            for j in range(5, 8):
                if self.board[j][i] == self.board[j - 1][i + 1] == self.board[j - 2][i + 2] == self.board[j - 3][
                    i + 3] == symbol:
                    win = True

        return win

    def is_column_full(self, column):
        return self.board[0][column] != ' '

    def is_full(self):
        for column in range(7):
            if not self.is_column_full(column):
                return False
        return True
