from random import randint

START_GAP = 1
END_GAP = 100
DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'

random_number = randint(START_GAP, END_GAP)


def is_prime() -> bool:
    for i in range(2, int(random_number ** 0.5) + 1):
        if random_number % i == 0:
            return False
    return True


def get_gameinfo() -> tuple[str, str]:
    if is_prime():
        answer = 'yes'
    else:
        answer = 'no'
    question = random_number
    return str(question), answer
