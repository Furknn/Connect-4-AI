from Board import Board


class Player:
    def __init__(self, symbol):
        self.symbol = symbol

    def play(self, board: Board):
        # print current player score with heuristic
        print('Player ' + self.symbol + ' turn')
        print('Score: ' + str(board.heuristic_h2(self.symbol)))

        while True:
            try:
                column = int(input('Enter column: ')) - 1
                if board.insert(self.symbol, column):
                    break
                else:
                    print('Column is invalid!')
            except ValueError:
                print('Invalid column!')
