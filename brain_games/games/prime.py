from random import randint

START = 1
END = 100
DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'

random_number = randint(START, END)


def is_prime() -> bool:
    for i in range(2, int(random_number ** 0.5) + 1):
        if random_number % i == 0:
            return False
    return True


def generate_data() -> tuple[str, str]:
    if is_prime():
        answer = 'yes'
    else:
        answer = 'no'
    question = random_number
    return str(question), answer
