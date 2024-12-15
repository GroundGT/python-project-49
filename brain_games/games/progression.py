from random import randint

START_GAP = 0
END_GAP = 100
MIN_SIZE = 5
MAX_SIZE = 10
START_INDEX = 0
DESCRIPTION = 'What number is missing in the progression?'


def get_progression() -> list[int]:
    element_1st = randint(START_GAP, END_GAP)
    step = randint(START_GAP, END_GAP)
    size_progression = randint(MIN_SIZE, MAX_SIZE)

    progression_list = [element_1st + step * i for i in range(size_progression)]

    return progression_list


def get_gameinfo() -> tuple[str, str]:
    progression = get_progression()
    element_for_task = randint(START_INDEX, len(progression) - 1)
    answer = str(progression[element_for_task])
    question = (" ".join(map(str, progression)))
    question = question.replace(answer, '..')

    return question, str(answer)
