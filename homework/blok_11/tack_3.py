import math #подключаем модуль 

the_weight_of_the_file = int(input('Введите общий вес файла: ')) #получаем общее число мб
download_speed = int(input('Какова скорость вашего соединения: ')) # получаем скорость соединения
loading_time = 0 #контейнер на время
download_amount = 0 #контейнер на мб

while True: # бесконечный цикл

  if download_amount >= the_weight_of_the_file: # проверка на окончание программы и остановка цикла
    loading_time += 1
    print('Прошло', loading_time , 'сек. Скачано', the_weight_of_the_file , 'из', the_weight_of_the_file, 'Мб ( 100 %)')
    break
  else: # обработка и подсчет времени и суммы мб
    download_amount += download_speed
    if download_amount >= the_weight_of_the_file: # если сумма мб выше основного числа
      continue # пропускаем цикл
    download_percentage = math.ceil((download_amount * 100) /  the_weight_of_the_file)
    loading_time += 1
    print('Прошло', loading_time , 'сек. Скачано', download_amount , 'из', the_weight_of_the_file, 'Мб (', download_percentage, '%)')
