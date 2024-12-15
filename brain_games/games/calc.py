import random
from operator import add, sub, mul

START_GAP = 1
END_GAP = 100
DESCRIPTION = 'What is the result of the expression?'


def get_gameinfo() -> tuple[str, str]:
    first_number = random.randint(START_GAP, END_GAP)
    second_number = random.randint(START_GAP, END_GAP)

    operators = {
        '+': add(first_number, second_number),
        '-': sub(first_number, second_number),
        '*': mul(first_number, second_number)
    }

    action = random.choice(list(operators.keys()))
    question = f'{first_number} {action} {second_number}'
    answer = operators.get(action)

    return question, str(answer)
