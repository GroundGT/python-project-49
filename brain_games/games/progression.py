from random import randint

START = 0
END = 100
MIN_SIZE = 5
MAX_SIZE = 10
START_INDEX = 0
DESCRIPTION = 'What number is missing in the progression?'


def get_progression() -> list[int]:
    first_element = randint(START, END)
    step = randint(START, END)
    size_progression = randint(MIN_SIZE, MAX_SIZE)
    progression_list = [first_element]

    for i in range(size_progression - 1):
        progression_list.append(progression_list[i] + step)

    return progression_list


def generate_data() -> tuple[str, str]:
    progression = get_progression()
    index_for_task = randint(START_INDEX, len(progression) - 1)
    answer = str(progression[index_for_task])
    progression[index_for_task] = '..'
    question = (" ".join(map(str, progression)))

    return question, str(answer)







