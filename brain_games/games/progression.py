from random import randint

START_GAP = 0
END_GAP = 100
MIN_SIZE = 5
MAX_SIZE = 10
START_INDEX = 0
DESCRIPTION = 'What number is missing in the progression?'


def get_progression() -> list[int]:
    """Generates an arithmetic progression.

    The function randomly selects the first element of the progression,
    the step of the progression and its size,and then returns a list
    containing the elements of this progression.

    Returns:
        list[int]: A list containing the elements of the arithmetic progression.

    Note:
    - the first element of the progression and the step are randomly generated
    in the range from START_GAP to END_GAP.
    - the size of the progression is randomly selected in the range from
    MIN_SIZE to MAX_SIZE.
    """
    first_element = randint(START_GAP, END_GAP)
    step = randint(START_GAP, END_GAP)
    size_progression = randint(MIN_SIZE, MAX_SIZE)

    progression_list = [first_element + step * i for i in range(size_progression)]

    return progression_list


def make_task() -> tuple[str, str]:
    """ Generates a question and answer for the game based on the sequence.
    The function extracts a random element from the progression and forms a
    string of the question, replacing this element with '..'.

    Returns:
         tuple[str, str]: A tuple containing a question string and an
    answer string:
    - the question is a progression with the replacement of one element by '..'.
    - the answer is a string representation of the element of the progression
    that was replaced.
    """
    progression = get_progression()
    element_for_task = randint(START_INDEX, len(progression) - 1)
    answer = str(progression[element_for_task])
    question = (" ".join(map(str, progression)))
    question = question.replace(answer, '..')

    return question, str(answer)
