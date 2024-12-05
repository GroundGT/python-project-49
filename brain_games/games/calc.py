from random import randint, choice


LIST_OF_OPERATIONS = ['+', '-', '*']
BEGINNING = 1
END = 100
QUESTION_CALC = 'What is the result of the expression?'


def calculate_two_numbers():

    action = choice(LIST_OF_OPERATIONS)
    first_number = randint(BEGINNING, END)
    second_number = randint(BEGINNING, END)
    print(first_number, second_number, action)

    match action:
        case '+':
            expression = f'{first_number} + {second_number}'
            answer =  first_number + second_number
            return expression, answer
        case '-':
            if first_number >= second_number:
                expression = f'{first_number} - {second_number}'
                answer = first_number - second_number
                return expression, answer
            else:
                expression = f'{second_number} - {first_number}'
                answer = second_number - first_number
                return expression, answer
        case '*':
            expression = f'{second_number} * {first_number}'
            answer = second_number * first_number
            return expression, answer


print(calculate_two_numbers())

