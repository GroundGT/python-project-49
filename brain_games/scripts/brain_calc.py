from brain_games.core import launch_game
from brain_games.games import calc


def main():
    """Starts the main game.This function initializes and launches the
    game using the launch_game function with the parameter calc.
    """
    launch_game(calc)


if __name__ == '__main__':

    main()