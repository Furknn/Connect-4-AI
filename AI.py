from Board import Board
from Player import Player
from random import randint


class AI(Player):
    def __init__(self, symbol, strategy):
        super().__init__(symbol)
        self.strategy = strategy

    def play(self, board: Board):
        while True:
            if self.strategy == 1:
                column: int = self.random_strategy(board)
            elif self.strategy == 2:
                column: int = self.minimax_strategy(board)
            else:
                column: int = self.minmax_alpha_beta_pruning(board)
            if board.insert(self.symbol, column):
                break

    def random_strategy(self, board: Board):
        # select random column that is not full
        while True:
            column = randint(0, 6)
            if board.is_column_full(column):
                continue
            else:
                return column

