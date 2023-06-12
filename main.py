# connect 4 game in console without pygame
from Game import Game
from Evaluation import HeuristicOne, HeuristicTwo


def main():
    # Choose game mode
    print('Choose game mode:')
    print('1. Player vs Player')
    print('2. Player vs AI')
    print('3. AI vs AI')

    mode = int(input('Enter mode: '))

    # choose strategy for each ai player
    if mode == 3:
        print('Choose strategy for each AI player:')
        print('1. Heuristic 1')
        print('2. Heuristic 2')

        strategy = int(input('Enter strategy for AI player 1: '))
        depth = int(input('Enter depth for AI player 1: '))

        strategy2 = int(input('Enter strategy for AI player 2: '))
        depth2 = int(input('Enter depth for AI player 2: '))

        if strategy == 1:
            strategy = HeuristicOne(depth)
        elif strategy == 2:
            strategy = HeuristicTwo(depth)
        else:
            print('Invalid strategy!')
            return

        if strategy2 == 1:
            strategy2 = HeuristicOne(depth2)
        elif strategy2 == 2:
            strategy2 = HeuristicTwo(depth2)
        else:
            print('Invalid strategy!')
            return

        # play game
        game = Game(mode, strategy, strategy2)


    elif mode == 2:
        print('Choose strategy for AI player:')
        print('1. Heuristic 1')
        print('2. Heuristic 2')

        strategy = int(input('Enter strategy for AI player: '))
        depth = int(input('Enter depth for AI player: '))

        if strategy == 1:
            strategy = HeuristicOne(depth)

        elif strategy == 2:
            strategy = HeuristicTwo(depth)

        else:
            print('Invalid strategy!')
            return

            # play game
        game = Game(mode, strategy)

    else:
        # play game
        game = Game(mode)

    game.play()



if __name__ == '__main__':
    main()
