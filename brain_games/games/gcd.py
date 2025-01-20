from random import randint

START_GAP = 1
END_GAP = 50
DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def make_task() -> tuple[str, str]:
    """ Generates two random numbers and finds their greatest common divisor
    (GCD).

    The function creates two random numbers in a given range and calculates
    their NODE is using the Euclidean algorithm.

    Returns:
        tuple[str, str]: A tuple of two elements:
    - a string with two numbers separated by a space (for example, "15 25")
    - a string with their largest common divisor

    Note:
        The algorithm uses the method of sequential division with remainder
    (Euclid's algorithm) to find the nodes of two numbers.
    """
    first_number = randint(START_GAP, END_GAP)
    second_number = randint(START_GAP, END_GAP)
    question = f'{first_number} {second_number}'

    while first_number != 0 and second_number != 0:
        if first_number > second_number:
            first_number %= second_number
        else:
            second_number %= first_number

    answer = first_number + second_number
    return question, str(answer)
