from random import randint

START_GAP = 1
END_GAP = 50
DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_gameinfo() -> tuple[str, str]:
    first_number = randint(START_GAP, END_GAP)
    second_number = randint(START_GAP, END_GAP)
    question = f'{first_number} {second_number}'

    while first_number != 0 and second_number != 0:
        if first_number > second_number:
            first_number %= second_number
        else:
            second_number %= first_number

    answer = first_number + second_number
    return question, str(answer)
