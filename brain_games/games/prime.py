from random import randint


BEGINNING = 1
END = 100
QUESTION_PRIME = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime():
        random_number = randint(BEGINNING, END)
        for i in range(2, int(random_number ** 0.5) + 1):
            if random_number % i == 0:
                return False, random_number
        return True, random_number


def get_answer():
    check, random_number = is_prime()
    if check:
        answer = 'yes'
    else:
        answer = 'no'
    return str(random_number), answer

print(get_answer())

