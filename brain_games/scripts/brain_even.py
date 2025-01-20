from brain_games.core import launch_game
from brain_games.games import even


def main():
    """Starts the main game.This function initializes and launches the
    game using the launch_game function with the parameter even.
    """
    launch_game(even)


if __name__ == '__main__':

    main()