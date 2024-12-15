from random import randint

BEGINNING = 1
END = 50
DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def generate_data() -> str | str:
    first_number = randint(BEGINNING, END)
    second_number = randint(BEGINNING, END)
    question = f'{first_number} {second_number}'

    while first_number != 0 and second_number != 0:
        if first_number > second_number:
            first_number %= second_number
        else:
            second_number %= first_number

    answer = first_number + second_number
    return question, str(answer)
