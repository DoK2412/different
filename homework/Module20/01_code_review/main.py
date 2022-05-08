# я не стал править старый код,а напсал свой.

# создаем функцию для расавковки словарей
# и возврата данных по интересам и фамилиям отдельно


def unpacking_the_database(user):

    surname = students[user]['surname']
    interests = students[user]['interests']
    return surname, interests


students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology', 'swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}

# места хранения распакованных данных
list_of_interests = list()
surname_list = list()
# цикл для распаковки словаря и обработк полученных данных
for i_students in students:
    print('ID студента {0} - его возраст {1}'.format(i_students, students[i_students]['age']))
    surname, interests = unpacking_the_database(i_students)
    surname_list.append(surname)
    for i_interests in interests:
        list_of_interests.append(i_interests)


# вывод конечного результата
print('Общие интересы: ', list_of_interests)
print('Общая длинна всех фамилий: ', len(''.join(surname_list)))
