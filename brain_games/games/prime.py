from random import randint


BEGINNING = 1
END = 100
QUESTION_PRIME = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime():
        random_number = randint(BEGINNING, END)
        for i in range(2, int(random_number ** 0.5) + 1):
            if random_number % i == 0:
                return False
        return True


def get_answer():
    if is_prime():
