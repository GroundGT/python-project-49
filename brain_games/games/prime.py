from random import randint

START_GAP = 1
END_GAP = 100
DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'

random_number = randint(START_GAP, END_GAP)


def is_prime() -> tuple[int, bool]:
    """Generates random number and checks it`s prime status'

    Returns:
        tuple[int, bool]: A tuple of two elements: A number and it`s bool
    prime check
    """
    random_number = randint(START_GAP, END_GAP)

    for i in range(2, int(random_number ** 0.5) + 1):
        if random_number % i == 0:
            return random_number, False
    return random_number, True


def get_game_objects() -> tuple[str, str]:
    """This function get the result of function is_prime() in it`s body

    Returns:
        tuple[str, str]: A tuple with the question number and answer.
    """
    question, answer = is_prime()
    return str(question), 'yes' if answer else 'no'
