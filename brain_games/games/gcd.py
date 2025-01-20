from random import randint

START_GAP = 1
END_GAP = 50
DESCRIPTION = 'Find the greatest common divisor of given numbers.'

def generate_random_numbers() -> tuple[int, int]:
    """Generates two random numbers within the specified range.

    Returns:
        tuple[int, int]: A tuple containing two random integers.
    """
    first_number = randint(START_GAP, END_GAP)
    second_number = randint(START_GAP, END_GAP)
    return first_number, second_number

def calculate_gcd(a: int, b: int) -> int:
    """Calculates the greatest common divisor (GCD) of two numbers
    using the Euclidean algorithm.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The greatest common divisor of the two numbers.
    """
    while b != 0:
        a, b = b, a % b
    return a

def get_gameinfo() -> tuple[str, str]:
    """Generates two random numbers and finds their greatest common divisor (GCD).

    Returns:
        tuple[str, str]: A tuple of two elements:
        - a string with two numbers separated by a space (for example, "15 25")
        - a string with their largest common divisor
    """
    first_number, second_number = generate_random_numbers()
    question = f'{first_number} {second_number}'
    answer = calculate_gcd(first_number, second_number)
    return question, str(answer)
