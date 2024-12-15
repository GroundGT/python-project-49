from operator import add, mul, sub
from random import choice, randint

START_GAP = 1
END_GAP = 100
DESCRIPTION = 'What is the result of the expression?'


def get_gameinfo() -> tuple[str, str]:
    first_number = randint(START_GAP, END_GAP)
    second_number = randint(START_GAP, END_GAP)

    operators = {
        '+': add(first_number, second_number),
        '-': sub(first_number, second_number),
        '*': mul(first_number, second_number)
    }

    action = choice(list(operators.keys()))
    question = f'{first_number} {action} {second_number}'
    answer = operators.get(action)

    return question, str(answer)
