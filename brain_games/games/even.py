from random import randint

START_GAP = 1
END_GAP = 100
DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_gameinfo() -> tuple[str, str]:
    """ Generates a random number and determines its parity.

    The function creates a random number in a given range and returns
    it along with the parity answer ('yes' for even, 'no' for odd).

    Returns:
        tuple[str, str]: A tuple of two elements:
    - a string with a number to check
    - a string with the answer ('yes' if the number is even, 'no' if odd)

    Note:
        An even number is considered to be divisible by 2 without remainder.
    """
    number = randint(START_GAP, END_GAP)
    if number % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'
    question = number
    return str(question), answer  # !
