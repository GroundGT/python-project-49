from random import randint


BEGINNING = 1
END = 100
QUESTION_EVEN = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_even() -> int and str:
    number = randint(BEGINNING, END)
    if number % 2 == 0:
        value = 'yes'
    else:
        value = 'no'
    return number, value

print(generate_even())



