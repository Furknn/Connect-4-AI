# connect 4 game in console without pygame
from Game import Game


def main():
    # Choose game mode
    print('Choose game mode:')
    print('1. Player vs Player')
    print('2. Player vs AI')
    print('3. AI vs AI')

    mode = int(input('Enter mode: '))

    #loop
    while True:
        game = Game(mode)
        game.play()

        # ask for rematch
        rematch = input('Rematch? (y/n): ')
        if rematch == 'n':
            break



if __name__ == '__main__':
    main()
