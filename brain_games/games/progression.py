import random

START_GAP = 0
END_GAP = 100
MIN_SIZE = 5
MAX_SIZE = 10
START_INDEX = 0
DESCRIPTION = 'What number is missing in the progression?'


def get_progression() -> list[int]:
    """Generates an arithmetic progression. The function randomly
    selects the first element of the progression, the step of the
    progression and its size.

    Returns:
        list[int]: A list containing the elements of the arithmetic progression.
    """
    first_element = random.randint(START_GAP, END_GAP)
    step = random.randint(START_GAP, END_GAP)
    size_progression = random.randint(MIN_SIZE, MAX_SIZE)

    return [first_element + step * i for i in range(size_progression)]


def get_game_objects() -> tuple[str, str]:
    """ Generates a question and answer for the game based on the sequence.
    The function extracts a random element from the progression and forms a
    string of the question, replacing this element with '..'.

    Returns:
         tuple[question: str, answer: str]: A tuple containing a question string
    and an answer string:
    - the question is a progression with the replacement of one element by '..'.
    - the answer is a string representation of the element of the progression
    that was replaced.
    """
    progression = get_progression()
    answer = str(random.choice(progression))
    question = (" ".join(map(str, progression))).replace(answer, '..')

    return question, answer
