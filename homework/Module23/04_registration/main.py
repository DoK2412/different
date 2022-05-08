import os


def string_length(i_user):
    if len(i_user) < 3:
        raise IndexError('Введены не все необходимые параметры.')


def numbers_in_the_name(i_user):
    if i_user[0].isalpha() == 0:
        raise NameError('В имени присутствуют цифры.')


def checking_the_sign(i_user):
    if '@' not in i_user[1] or '.' not in i_user[1]:
        raise SyntaxError('В эмейле отсутствуют "@", "."')


def age_verification(i_user):
    if int(i_user[2]) < 10 or int(i_user[2]) > 100:
        raise ValueError('Возраст меньше 10 либо больше 100')


# создаем функцию в ней цикл и указавает сорторовку данных
def verifying_user_data(list_of_users):
    for i_user in list_of_users:
        try:
            # проверка длины строки - Точнее количество параметров или полноту данных
            string_length(i_user)
            # проверка присутствия посторонних знаков в имени
            numbers_in_the_name(i_user)
            # проверка начилия @ и . в эмейле
            checking_the_sign(i_user)
            # проверка возраста
            age_verification(i_user)
        except (IndexError, NameError, SyntaxError, ValueError,) as exc:
            with open(
                    'registrations_bad.log', 'a', encoding='utf-8') as error:
                error.write('Несоответствие в: ' + str(i_user) +
                            ' ' + str(exc) + '\n')
        else:
            with open(
                    'registrations_good.log', 'a',
                    encoding='utf-8') as accordance:
                accordance.write(str(i_user) + '\n')
    print('Данные успешно отсортированы.')

# открываем файл и создаем список пользователейдля работы
with open(
    os.path.abspath(
        os.path.join('registrations.txt')), 'r', encoding='utf-8') as users:
    list_of_users = [user.split() for user in users.read().splitlines()]
    verifying_user_data(list_of_users)
