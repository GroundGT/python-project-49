from random import randint


BEGINNING = 1
END = 100
DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'

#  two functions bool and generate_data
def generate_data() -> str | int: # !
    """Данная функция проверяет на четность сгенерируемое число
    и возвращает само число и правильный ответ"""
    number = randint(BEGINNING, END)
    if number % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'
    question = number
    return str(question), answer  # !
