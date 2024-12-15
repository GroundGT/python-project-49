import prompt


ROUNDS = 3


def launch_game(game):
    """Данная функция является логическим ядром проекта brain-games. В начале приветствуем пользователя,
     получив его имя, далее выводим описание задания, полученное из модуля с выбранной игрой. Инициализируем цикл
     из трех попыток-ответов, как итог - заканчиваем цикл в случае если ответы правильные, также заканчиваем цикл,
     если ответ неверный"""
    print('Welcome to the Brain games')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print(game.DESCRIPTION)

    for _ in range(ROUNDS):
        question, answer = game.generate_data()
        print(f'Question: {question}')
        player_answer = prompt.string('Your answer: ')

        if player_answer != answer:
            print(f'"{player_answer}" is wrong answer ;(. Correct answer was "{answer}"')
            print(f'Let`s try again, {name}!')
            break
        else:
            print('Correct!')
    else:
        print(f'Congratulations, {name}!')
