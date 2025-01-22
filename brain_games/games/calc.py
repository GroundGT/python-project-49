from operator import add, mul, sub
from random import choice, randint

START_GAP = 1
END_GAP = 100
DESCRIPTION = 'What is the result of the expression?'
OPERATORS = {
    '+': add,
    '-': sub,
    '*': mul,
}


def get_game_objects() -> tuple[str, str]:
    """Generates an arithmetic expression and its result.

    The function creates a random arithmetic expression with two numbers
    and one operator (+, - or *), and also calculates its result.

    Returns:
        tuple[str, str]: A tuple of two elements:
    - a string with an arithmetic expression
    - a string with an answer (the result of calculating the expression)
    """
    first_number = randint(START_GAP, END_GAP)
    second_number = randint(START_GAP, END_GAP)

    action = choice(list(OPERATORS.keys()))
    question = f'{first_number} {action} {second_number}'
    answer = str(OPERATORS[action](first_number, second_number))

    return question, answer
