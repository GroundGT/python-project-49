import prompt

ROUNDS = 3


def launch_game(game):
    """Base function of the project. Its starts the game, greets the player,
    asks questions and checks the answers with the help of result of function
    get_game_objects().

    Parameters:
        game: A game object that should contain the get_game_objects() method that
    generates questions and answers and also, constants : DESCRIPTION and
    a number of ROUNDS

    Returns:
        str objects that contain the results of user`s answers
    """

    print('Welcome to the Brain games')
    name = prompt.string('May I have your name? ')
    print(
          f'Hello, {name}\n'
          f'{game.DESCRIPTION}'
    )

    answer_check = True
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
            answer_check = False
            break

        print('Correct!')

    if answer_check:
        print(f'Congratulations, {name}!')
