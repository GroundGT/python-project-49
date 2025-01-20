from random import randint

START_GAP = 1
END_GAP = 100
DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'

random_number = randint(START_GAP, END_GAP)


def is_prime() -> bool:
    """Returns bool value of variable 'random-number.'

    Returns:
        'True' if the number is prime
        'False' if the number is not prime
    """
    for i in range(2, int(random_number ** 0.5) + 1):
        if random_number % i == 0:
            return False
    return True


def make_task() -> tuple[str, str]:
    """This function get the result of function is_prime() in it`s body

    Returns:
        tuple[str, str]: A tuple with the question number and answer.
    """
    if is_prime():
        answer = 'yes'
    else:
        answer = 'no'
    question = random_number
    return str(question), answer
