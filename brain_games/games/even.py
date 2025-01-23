from random import randint

START_GAP = 1
END_GAP = 100
DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number: int) -> bool:
    """ Determines number`s parity.

    Args:
        number[int]: A number to check
    Returns:

        bool: A number bool parity check
    """
    return number % 2 == 0


def get_game_objects() -> tuple[str, str]:
    """ Function uses result of is_even() function to return question
    and answer for player

    Returns:
        tuple[str, str]: A tuple of two elements:
    - a string as a question
    - a string with the answer ('yes' if the number is even, 'no' if odd)
    """
    number = randint(START_GAP, END_GAP)
    answer = 'yes' if is_even(number) else 'no'

    return str(number), answer
