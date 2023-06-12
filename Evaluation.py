from Board import Board


class Evaluation:
    depth: int = None

    def __init__(self, depth: int):
        self.depth = depth

    def eval(self, board, player_symbol) -> int:
        pass


class HeuristicOne(Evaluation):
    def __init__(self, depth: int):
        super().__init__(depth)
        self.board: Board = None

    def eval(self, board, player_symbol):
        self.board = board
        return self.heuristic_h1(player_symbol, 3) + self.heuristic_h1(player_symbol, 2)

    def heuristic_h1(self, symbol: str, sequence_len: int = 3):
        # same as h1 but with dynamic sequence length
        # get dimension of board
        x = len(self.board.board)
        y = len(self.board.board[0])

        # count the number of sequence_len sequences that has the symbol and an empty space
        score = 0

        # create sliding window
        # sequence_len* symbol + empty space until total length is 4
        windows = [symbol] * sequence_len + [' '] * (self.board.winning_sequence_len - sequence_len)
        windows = [[symbol] * sequence_len + [' '] * (self.board.winning_sequence_len - sequence_len),
                   windows[::-1]]

        # check horizontal matches the window from either side
        for i in range(x):
            for j in range(y - self.board.winning_sequence_len + 1):
                if self.board.board[i][j:j + self.board.winning_sequence_len] in windows:
                    score += sequence_len

        # check vertical matches the window inverted
        for i in range(x - self.board.winning_sequence_len + 1):
            for j in range(y):
                if [self.board.board[i][j], self.board.board[i + 1][j], self.board.board[i + 2][j],
                    self.board.board[i + 3][j]] == windows[1]:
                    score += sequence_len

        # check diagonal matches the window from either side
        for i in range(x - self.board.winning_sequence_len + 1):
            for j in range(y - self.board.winning_sequence_len + 1):
                if [self.board.board[i][j], self.board.board[i + 1][j + 1], self.board.board[i + 2][j + 2],
                    self.board.board[i + 3][j + 3]] in windows:
                    score += sequence_len

        # check diagonal matches the window from either side
        for i in range(x - self.board.winning_sequence_len + 1):
            for j in range(self.board.winning_sequence_len - 1, y):
                if [self.board.board[i][j], self.board.board[i + 1][j - 1], self.board.board[i + 2][j - 2],
                    self.board.board[i + 3][j - 3]] in windows:
                    score += sequence_len

        return score


class HeuristicTwo(Evaluation):
    def __init__(self, depth: int):
        super().__init__(depth)
        self.possible_symbols = ['X', 'O']
        self.board: Board = None
        self.depth = depth

    def eval(self, board, player_symbol):
        self.board = board
        return self.heuristic_h3(player_symbol)

    def heuristic_h3(self, symbol: str):
        # threat is a square that connects 4 when a symbol is put in by the opponent.
        # count the number of threats
        opn_symbol = self.possible_symbols[(self.possible_symbols.index(symbol) + 1) % 2]
        threat_count = 0

        threat_windows = [[opn_symbol, opn_symbol, opn_symbol, ' '], [' ', opn_symbol, opn_symbol, opn_symbol],
                          [opn_symbol, ' ', opn_symbol, opn_symbol], [opn_symbol, opn_symbol, ' ', opn_symbol]]

        # check horizontal if there is a threat from either side
        for i in range(7):
            for j in range(5):
                if self.board.board[i][j:j + 4] in threat_windows:
                    threat_count += 1

        # check vertical if there is a threat
        for i in range(4):
            for j in range(5):
                if [self.board.board[i][j], self.board.board[i + 1][j], self.board.board[i + 2][j],
                    self.board.board[i + 3][j]] == \
                        threat_windows[1]:
                    threat_count += 1

        # check diagonal if there is a threat from either side
        for i in range(4):
            for j in range(5):
                if [self.board.board[i][j], self.board.board[i + 1][j + 1], self.board.board[i + 2][j + 2],
                    self.board.board[i + 3][j + 3]] in threat_windows:
                    threat_count += 1

        # check diagonal if there is a threat from either side
        for i in range(4):
            for j in range(3, 7):
                if [self.board.board[i][j], self.board.board[i + 1][j - 1], self.board.board[i + 2][j - 2],
                    self.board.board[i + 3][j - 3]] in threat_windows:
                    threat_count += 1

        return -threat_count
