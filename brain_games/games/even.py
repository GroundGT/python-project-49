from random import randint

START_GAP = 1
END_GAP = 100
DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_gameinfo() -> tuple[str, str]:
    number = randint(START_GAP, END_GAP)
    if number % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'
    question = number
    return str(question), answer  # !
