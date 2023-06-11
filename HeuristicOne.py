from Evaluation import Evaluation


class HeuristicOne(Evaluation):
    def __init__(self):
        self.board = None

    def eval(self, board, player_symbol):
        self.board = board
        return self.heuristic_h1(player_symbol, 3) + self.heuristic_h1(player_symbol, 2)

    def heuristic_h1(self, symbol: str, sequence_len: int = 3):
        # same as h1 but with dynamic sequence length
        # get dimension of board
        x = len(self.board)
        y = len(self.board[0])

        # count the number of sequence_len sequences that has the symbol and an empty space
        score = 0

        # create sliding window
        # sequence_len* symbol + empty space until total length is 4
        windows = [symbol] * sequence_len + [' '] * (self.board.winning_sequence_len - sequence_len)
        windows = [[symbol] * sequence_len + [' '] * (self.board.winning_sequence_len - sequence_len), windows[::-1]]

        # check horizontal matches the window from either side
        for i in range(x):
            for j in range(y - self.board.winning_sequence_len + 1):
                if self.board[i][j:j + self.board.winning_sequence_len] in windows:
                    score += sequence_len

        # check vertical matches the window inverted
        for i in range(x - self.board.winning_sequence_len + 1):
            for j in range(y):
                if [self.board[i][j], self.board[i + 1][j], self.board[i + 2][j], self.board[i + 3][j]] == windows[1]:
                    score += sequence_len

        # check diagonal matches the window from either side
        for i in range(x - self.board.winning_sequence_len + 1):
            for j in range(y - self.board.winning_sequence_len + 1):
                if [self.board[i][j], self.board[i + 1][j + 1], self.board[i + 2][j + 2],
                    self.board[i + 3][j + 3]] in windows:
                    score += sequence_len

        # check diagonal matches the window from either side
        for i in range(x - self.board.winning_sequence_len + 1):
            for j in range(self.board.winning_sequence_len - 1, y):
                if [self.board[i][j], self.board[i + 1][j - 1], self.board[i + 2][j - 2],
                    self.board[i + 3][j - 3]] in windows:
                    score += sequence_len

        return score
