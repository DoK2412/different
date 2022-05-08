
# функция для добавления данных в словарь
def adding_a_subscriber(phonebook):
    assembly_wrench = tuple(input('Введите фамилию и имя: ').title().split())
    if assembly_wrench in phonebook.keys():
        print('Такой аббонент уже есть!')
    else:
        phone_number = int(input('Введите номер телефона: '))
        phonebook[assembly_wrench] = phone_number
        print('Аббонент добавлен в список')
        return phonebook


# функция для поиска данных в словаре
def subscriber_search(phonebook):
    surname = input('Введите фамилию: ').title()
    for key, telephone in phonebook.items():
        if surname in key:
            print(key, ':', telephone)

# словарь для работы
phonebook = dict()
# цикл для полноценной работы с телефонной книгой
while 1:
    act = int(input('Какое действие вы хотите выполнить: 1 - добавить контакт, 2 - найти человека в списке контактов '))
    if act == 1:
        adding_a_subscriber(phonebook)
        print(phonebook, '\n')
    elif act == 2:
        subscriber_search(phonebook)
