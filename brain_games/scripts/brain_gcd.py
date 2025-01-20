from brain_games.core import launch_game
from brain_games.games import gcd


def main():
    """Starts the main game.This function initializes and
    launches the game using the launch_game function with
    the parameter gcd.
    """
    launch_game(gcd)


if __name__ == '__main__':

    main()