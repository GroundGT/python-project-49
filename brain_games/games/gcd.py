from random import randint

START_GAP = 1
END_GAP = 50
DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def calculate_gcd(first_number: int, second_number: int) -> int:
    """Calculates the greatest common divisor (GCD) of two numbers
    using the Euclidean algorithm.

    Args:

        first_number (int): The first number to check
        second_number (int): The second number to check

    Returns:

        result[int]: The greatest common divisor of the two numbers.
    """
    while second_number != 0:
        first_number, second_number = (second_number, first_number %
                                       second_number
        )
    result = first_number

    return result


def get_game_objects() -> tuple[str, str]:
    """Generates two random numbers and finds their greatest common
    divisor (GCD).

    Returns:

        tuple[str, str]: A tuple of two elements:
    - a string with two numbers separated by a space
    - a string with their largest common divisor
    """
    first_number = randint(START_GAP, END_GAP)
    second_number = randint(START_GAP, END_GAP)
    question = f'{first_number} {second_number}'
    answer = str(calculate_gcd(first_number, second_number))
    return question, answer
