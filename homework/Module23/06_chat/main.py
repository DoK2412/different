import os
import time


def checking_the_input():
    action = int(input('Выбирете действие из предложенных: \n\t\t1. \
Посмотреть текущий текст чата.\n\t\t2. Отправить сообщение.\n\t\t3. \
Выйти из чата.\n\t'))
    if action == '':
        raise ValueError
    else:
        return action


def name_verification():
    name = input('\nВведите имя пользователя: ')
    if name == '':
        raise ValueError
    else:
        return name


# запускаем бесконечный цикл
while True:
    try:
        # запрашиваем и проверяем ввод имени
        name = name_verification()
        # запрашиваем и проверяем действие
        action = checking_the_input()
        # в зависимости от ответа определяем выводить историю или записывать ее
        if action == 1:
            with open(
                    os.path.abspath(os.path.join('chat_history.txt')),
                    'r', encoding='utf-8') as history:
                print(history.read())
        elif action == 2:
            message = input('Введите сообщение: ')
            with open(
                    os.path.abspath(os.path.join('chat_history.txt')),
                    'a', encoding='utf-8') as recording_a_message:
                recording_a_message.write(
                    str(time.strftime('/%d.%m.%Y %H:%M:%S/')) +
                    ' ' + name + ': ' + str(message) + '\n')
        elif action == 3:
            print('Чат закрыт.')
            break
        else:
            print('Введено не верное значние.')
    # ловим ошибку
    except ValueError:
        print('Ничего не введено')
