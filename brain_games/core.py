from types import ModuleType

import prompt

ROUNDS = 3


def launch_game(game: ModuleType) -> None:
    """Base function of the project. Its starts the game, greets the player,
    asks questions and checks the answers with the help of result of function
    get_game_objects().

    Args:

        game (ModuleType): Module of a game, which must contain the function.
    In this project, function get_game_objects(), which is situated at
    game`s module

    Returns:

        None: this function returns nothing, but output a result of game
    to the screen
    """

    print('Welcome to the Brain games')
    name = prompt.string('May I have your name? ')
    print(
          f'Hello, {name}\n'
          f'{game.DESCRIPTION}'
    )

    for _ in range(ROUNDS):
        question, answer = game.get_game_objects()
        print(f'Question: {question}')
        player_answer = prompt.string('Your answer: ')

        if player_answer != answer:
            print(
                  f'"{player_answer}" is wrong answer'
                  f';(. Correct answer was "{answer}"\n'
                  f'Let\'s try again, {name}!'
            )

            return

        print('Correct!')

    print(f'Congratulations, {name}!')
