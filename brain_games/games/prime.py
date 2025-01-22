from random import randint

START_GAP = 1
END_GAP = 100
DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number: int) -> bool:
    """Checks number`s prime status'
    Args:
        number[int]: A number to check
    Returns:
        bool: Number`s prime status
    """

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def get_game_objects() -> tuple[str, str]:
    """This function randomizes a number, checks it`s prime status
    by the result of function is_prime() in it`s body

    Returns:
        tuple[str, str]: A tuple with 2 strings:
        - a question number
        - the answer.
    """
    number = randint(START_GAP, END_GAP)
    question = str(number)
    answer = 'yes' if is_prime(number) else 'no'
    return question, answer