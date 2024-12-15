from random import randint, choice
# from operator import add, sub, mul


LIST_OF_OPERATIONS = ['+', '-', '*']  # !
BEGINNING = 1
END = 100
DESCRIPTION = 'What is the result of the expression?'


def generate_data() -> int and str:
    """Данная функция рандомно генерирует математическое выражение
    из двух чисел и возвращает подготовленное выражение, а также ответ
    на это выражение"""
    action = choice(LIST_OF_OPERATIONS)
    first_number = randint(BEGINNING, END)
    second_number = randint(BEGINNING, END)

    """Сверяемся с тем, какое выражение рандомизировала программа,
    производим соответсвующее вычисление:"""
    match action:

        case '+':
            expression = f'{first_number} + {second_number}'
            answer =  first_number + second_number
            return expression, str(answer)
        case '-':
            if first_number >= second_number:
                expression = f'{first_number} - {second_number}'
                answer = first_number - second_number
                return expression, str(answer)
            else:
                expression = f'{second_number} - {first_number}'
                answer = second_number - first_number
                return expression, str(answer)
        case '*':
            expression = f'{second_number} * {first_number}'
            answer = second_number * first_number
            return expression, str(answer)
