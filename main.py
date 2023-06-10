# connect 4 game in console without pygame
from Game import Game


def main():
    # Choose game mode
    print('Choose game mode:')
    print('1. Player vs Player')
    print('2. Player vs AI')
    print('3. AI vs AI')

    mode = int(input('Enter mode: '))

    # if mode has AI choose strategy
    strategy = 0
    if mode != 1:
        print('Choose strategy:')
        print('1. Random')
        print('2. Minimax')
        print('3. Alpha-Beta')
        strategy = int(input('Enter strategy: '))

    game = Game(mode, strategy)
    game.play()


if __name__ == '__main__':
    main()
