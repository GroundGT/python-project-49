from random import randint


BEGINNING = 0
END = 100
MIN_SIZE = 5
MAX_SIZE = 10
START_INDEX = 0
DESCRIPTION = 'What number is missing in the progression?'

def get_progression() -> list[int]:
    """Данная функция генерирует прогрессию, используя рандомизацию
    первого элемента прогрессии, шага и количества элементов в прогрессии,
    после чего возвращает прогрессию в виде списка. Результат работы функции
    используется в след. ниже функции generate_data в ткущем модуле"""
    first_element = randint(BEGINNING, END)
    step = randint(BEGINNING, END)
    size_progression = randint(MIN_SIZE, MAX_SIZE)
    progression_list = [first_element]  # Добавляем сгенерированный первый элемент в начало списка

    for i in range(size_progression - 1):  # change on list comprehension!!!!!!!!!!!
        progression_list.append(progression_list[i] + step)

    return progression_list


def generate_data() -> tuple[str, str]:
    """Функция в теле обрабатывает список, как результат работы функции get_progression(),
    генерирует число 'пропущенного' элемента в прогрессии, заменяет его на '..', собирает
    прогрессию воедино. Функция возвращает кортеж со списком прогрессии с пропущенным элементом, а
    также сам пропущенный элемент в виде строки"""

    progression = get_progression()
    index_for_task = randint(START_INDEX, len(progression) - 1)
    answer = str(progression[index_for_task])
    progression[index_for_task] = '..'
    question = (" ".join(map(str, progression)))

    return question, str(answer)







