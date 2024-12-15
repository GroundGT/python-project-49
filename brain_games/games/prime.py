from random import randint


BEGINNING = 1
END = 100
DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime() -> bool | int:  # predicats return only bool
    """Данная функция генерирует число и определяет является ли оно простым,
    после чего возвращает булево значение и само число. Результат работы данной фукнции
    используется в след. ниже функции (generate_data()) в текущем модуле"""
    random_number = randint(BEGINNING, END)
    for i in range(2, int(random_number ** 0.5) + 1):
        if random_number % i == 0:
            return False, random_number
    return True, random_number


def generate_data(): # channe name of functions everywhere (not data)
    """Данная функция в своем теле обрабатывает результат работы функции is prime()
    преобразует полученное булево значение в строку 'да' или 'нет', после чего возвращает
    строку с ответом и полученное число"""
    check, random_number = is_prime()
    if check:
        answer = 'yes'
    else:
        answer = 'no'
    question = random_number
    return str(question), answer
