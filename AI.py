from copy import deepcopy

from Board import Board
from Player import Player
from random import randint
from Evaluation import Evaluation


class AI(Player):
    evaluation_strategy: Evaluation

    def __init__(self, symbol, evaluation_strategy: Evaluation):
        super().__init__(symbol)
        self.evaluation_strategy: Evaluation = evaluation_strategy

    def play(self, board: Board):
        while True:
            column = self.strategy(board)
            if board.insert(self.symbol, column):
                break

    def strategy(self, board: Board):
        # Get the available columns for the current board state
        available_columns = self.get_available_columns(board)

        # Initialize the best column and best score
        best_column = None
        best_score = float('-inf')

        # Apply the minimax algorithm with alpha-beta pruning
        for column in available_columns:
            # Make a copy of the board
            board_copy = deepcopy(board)
            # Simulate making a move in the current column
            board_copy.insert(self.symbol, column)
            # Calculate the score for the current move using minimax with alpha-beta pruning
            score = self.minimax(board_copy, self.evaluation_strategy.depth, False, float('-inf'), float('inf'))
            # Update the best score and best column if necessary
            if score > best_score:
                best_score = score
                best_column = column
            elif score == best_score:
                if randint(0, 1) == 1:
                    best_column = column

        return best_column

    def get_available_columns(self, board):
        return [col for col in range(8) if not board.is_column_full(col)]

    def minimax(self, board: Board, depth, maximizing_player, alpha, beta):
        # Check if the game is over or the maximum depth is reached
        if board.check_win(self.symbol):
            return float('inf')

        if board.check_win(self.get_opponent_symbol()):
            return float('-inf')

        if depth == self.evaluation_strategy.depth:
            return self.evaluation_strategy.eval(board, self.symbol)

        if maximizing_player:
            max_score = float('-inf')
            available_columns = self.get_available_columns(board)
            for column in available_columns:
                board_copy = deepcopy(board)
                board_copy.insert(self.symbol, column)
                score = self.minimax(board_copy, depth + 1, False, alpha, beta)
                max_score = max(max_score, score)
                alpha = max(alpha, score)
                if beta <= alpha:
                    break
            return max_score
        else:
            min_score = float('inf')
            available_columns = self.get_available_columns(board)
            for column in available_columns:
                board_copy = deepcopy(board)
                board_copy.insert(self.get_opponent_symbol(), column)
                score = self.minimax(board_copy, depth + 1, True, alpha, beta)
                min_score = min(min_score, score)
                beta = min(beta, score)
                if beta <= alpha:
                    break
            return min_score

    def get_opponent_symbol(self):
        return 'X' if self.symbol == 'O' else 'O'
