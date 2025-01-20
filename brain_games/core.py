import prompt

ROUNDS = 3


def launch_game(game):
    """Base function of the project. Its starts the game, greets the player,
    asks questions and checks the answers with the help of result of function
    get_gameinfo().

    Parameters:
        game: A game object that should contain the get_gameinfo() method that
    generates questions and answers and also, constants : DESCRIPTION and
    a number of ROUNDS

    Returns:
        str objects that contain the results of user`s answers
    """

    print('Welcome to the Brain games')
    name = prompt.string('May I have your name? ')
    print(f'''Hello, {name}'
    {game.DESCRIPTION}'''
    )

    for _ in range(ROUNDS):
        question, answer = game.make_task()
        print(f'Question: {question}')
        player_answer = prompt.string('Your answer: ')

        if player_answer != answer:
            print(f'''"{player_answer}" is wrong answer ;(. Correct answer was "{answer}"
            Let\'s try again, {name}!'''
            )
            break
        else:
            print('Correct!')
    else:
        print(f'Congratulations, {name}!')
