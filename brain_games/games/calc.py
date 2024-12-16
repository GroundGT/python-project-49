from operator import add, mul, sub
from random import choice, randint

START_GAP = 1
END_GAP = 100
DESCRIPTION = 'What is the result of the expression?'


def get_gameinfo() -> tuple[str, str]:
    """Generates an arithmetic expression and its result.

    The function creates a random arithmetic expression with two numbers
    and one operator (+, - or *), and also calculates its result.

    Returns:
        tuple[str, str]: A tuple of two elements:
    - a string with an arithmetic expression
    - a string with an answer (the result of calculating the expression)

    Note:
        Supported operators: addition (+), subtraction (-), multiplication (*).
    """
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
