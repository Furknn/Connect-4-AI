from Evaluation import Evaluation


class HeuristicOne(Evaluation):
    def __init__(self):
        self.possible_symbols = ['X', 'O']
        self.board = None

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
                if self.board[i][j:j + 4] in threat_windows:
                    threat_count += 1

        # check vertical if there is a threat
        for i in range(4):
            for j in range(5):
                if [self.board[i][j], self.board[i + 1][j], self.board[i + 2][j], self.board[i + 3][j]] == \
                        threat_windows[1]:
                    threat_count += 1

        # check diagonal if there is a threat from either side
        for i in range(4):
            for j in range(5):
                if [self.board[i][j], self.board[i + 1][j + 1], self.board[i + 2][j + 2],
                    self.board[i + 3][j + 3]] in threat_windows:
                    threat_count += 1

        # check diagonal if there is a threat from either side
        for i in range(4):
            for j in range(3, 7):
                if [self.board[i][j], self.board[i + 1][j - 1], self.board[i + 2][j - 2],
                    self.board[i + 3][j - 3]] in threat_windows:
                    threat_count += 1

        return -threat_count
