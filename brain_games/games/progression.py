from random import randint


BEGINNING = 0
END = 100
MIN_SIZE = 5
MAX_SIZE = 10
START_INDEX = 0
DESCRIPTION_PROGRESSION = 'What number is missing in the progression?'

def get_progression() -> list:
    first_element = randint(BEGINNING, END)
    step = randint(BEGINNING, END)
    size_progression = randint(MIN_SIZE, MAX_SIZE)
    progression_list = [first_element]

    for i in range(size_progression - 1):
        progression_list.append(progression_list[i] + step)

    return progression_list



def get_task_for_progression():
    progression = get_progression()
    index_for_task = randint(START_INDEX, len(progression) - 1)
    answer = str(progression[index_for_task])
    progression[index_for_task] = '..'
    question = (" ".join(map(str, progression)))
    return question, str(answer)


print(get_task_for_progression())





