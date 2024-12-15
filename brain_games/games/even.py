from random import randint

START = 1
END = 100
DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_data() -> tuple[str, str]:
    number = randint(START, END)
    if number % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'
    question = number
    return str(question), answer  # !
