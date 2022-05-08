# получаем данные от пользователя
data_from_the_user = input('Введите строку: ')
# определяем индекс первой и последней необходимой буквы
index_of_the_first_value = data_from_the_user.find('h')
index_of_the_last_value = data_from_the_user.rfind('h')
# выводим данные
print('Вывод вырезки строки наоборот: ', data_from_the_user[index_of_the_last_value-1:index_of_the_first_value:-1])

