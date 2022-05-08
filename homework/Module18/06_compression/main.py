# запрашиваем данные от пользователя
the_string_being_checked = input('Введите строку: ')
# создаем переменную для сравнеия и подсчета
promotion = 1
the_variable_being_compared = the_string_being_checked[promotion:promotion+1]
counting_characters = 1
# цикл для проверки и подчсета букв
for i_string in the_string_being_checked:
    if i_string == the_variable_being_compared:
        counting_characters += 1
    else:
        print(i_string, end='')
        print(counting_characters, end='')
        counting_characters = 1
    # изменение индекса для переопределения проверяемого значения
    promotion += 1
    the_variable_being_compared = the_string_being_checked[promotion:promotion+1]
