from random import randint

START_GAP = 1
END_GAP = 100
DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even() -> tuple[int, bool]:
    """ Generates a random number and determines its parity.

    Returns:
        tuple[int, str]: A tuple of two elements: A number and it`s bool
    parity check
    """
    number = randint(START_GAP, END_GAP)
    return number, number % 2 == 0


def get_game_objects() -> tuple[str, str]:
    """ Function uses result of is_even() function to return question
    and answer for player

    Returns:
        tuple[str, str]: A tuple of two elements:
    - a string as a question
    - a string with the answer ('yes' if the number is even, 'no' if odd)
    """
    number, check = is_even()
    return str(number), 'yes' if check else 'no'
