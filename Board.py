class Board:
    def __init__(self):
        # 7x8 board
        self.board = []
        for i in range(7):
            self.board.append([' '] * 8)

    def print_board(self):
        for row in self.board:
            print('| ' + ' | '.join(row) + ' |')
        print('-' * 31)

    def insert(self, symbol, column):
        for i in range(7):
            if self.board[i][column] == ' ':
                self.board[i][column] = symbol
                return True
        return False

    def check_win(self, symbol):
        # check horizontal
        for row in self.board:
            for i in range(5):
                if row[i] == symbol and row[i+1] == symbol and row[i+2] == symbol and row[i+3] == symbol:
                    return True
        # check vertical
        for i in range(8):
            for j in range(4):
                if self.board[j][i] == symbol and self.board[j+1][i] == symbol and self.board[j+2][i] == symbol and self.board[j+3][i] == symbol:
                    return True
        # check diagonal
        for i in range(5):
            for j in range(4):
                if self.board[i][j] == symbol and self.board[i+1][j+1] == symbol and self.board[i+2][j+2] == symbol and self.board[i+3][j+3] == symbol:
                    return True
        for i in range(5):
            for j in range(3, 7):
                if self.board[i][j] == symbol and self.board[i+1][j-1] == symbol and self.board[i+2][j-2] == symbol and self.board[i+3][j-3] == symbol:
                    return True
        return False
