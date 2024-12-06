import prompt
from brain_games.cli import welcome_user

ROUNDS = 3


def launch_game(question_and_answer, description):
    name = welcome_user()
    for i in range(ROUNDS):
        question, answer = question_and_answer()
        player_answer = prompt.string(f'Question: {question}\nYour answer: ')
        if player_answer == answer:
            print('Correct!')
        else:
            print(f'"{player_answer}" is wrong answer ;(. Correct answer was {answer}')
            print(f'Let`s try again, {name}!')

            return
    print(f'Congratulations, {name}!')

print(launch_game())