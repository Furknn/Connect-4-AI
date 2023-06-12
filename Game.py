from AI import AI
from Board import Board
from Player import Player
from Evaluation import Evaluation, HeuristicOne, HeuristicTwo


class Game:
    def __init__(self, mode: int, strategy1: Evaluation = None, strategy2: Evaluation = None):
        self.mode = mode
        self.board = Board()
        self.players = []

        if mode == 1:
            self.players.append(Player('X'))
            self.players.append(Player('O'))
        elif mode == 2:
            self.players.append(Player('X'))
            self.players.append(AI('O', strategy1))
        else:
            self.players.append(AI('X', strategy1))
            self.players.append(AI('O', strategy2))

    def play(self):
        # game loop
        player_index = 0
        while True:
            # clear screen
            print('\n' * 100)

            # print player
            player: Player = self.players[player_index]
            print('Player ' + player.symbol + ' turn')

            # print board
            self.board.print_board()
            # get player
            player: Player = self.players[player_index]
            # player plays
            player.play(self.board)
            # check win
            if self.board.check_win(player.symbol):
                self.board.print_board()
                print(player.symbol + ' wins!')
                break

            # check draw
            if self.board.is_full():
                self.board.print_board()
                print('Draw!')
                break

            # switch player
            player_index = (player_index + 1) % 2
