def count_letters(number, letter, text): # создаем функцию 
  the_container_fo_the_digits = 0 # контейнер для подсчета чисел
  container_for_letters = 0 # контейнер для подсчета букв
  for search in text: # создание цикла на проверку строки
    if search == number:
      the_container_fo_the_digits += 1 
    elif search == letter:
      container_for_letters += 1
  print('Количество цифр',number,':', the_container_fo_the_digits ) # выпод результата по цифрам
  print('Количество цифр',letter,':', container_for_letters ) # вывод результата по буквам


number = input('Какую цифру ищем? ') # запрос поиска цифры
letter = input('Какую букву ищем? ') # запрос поиска буквы
text = input('Введите текст: ') #запрос строки от пользователя
count_letters(number, letter, text) #запуск функции в которую передаем строку
