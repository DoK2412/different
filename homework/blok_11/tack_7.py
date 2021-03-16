import math # подключаем модуль

print('Введите местоположение коня: ') # получаем координаты положения коня
horse_by_x = float(input()) * 10 # положение х и переносим точку на 1 знак вперед
horse_by_y = float(input()) * 10# положение у и переносим точку на 1 знак вперед

print('Введите местоположение точки на доске: ') # получаем желаемое положение коня
point_by_x = float(input()) * 10# положение х и переносим точку на 1 знак вперед
point_by_y = float(input()) * 10# положение у и переносим точку на 1 знак вперед


software_by_x = math.floor(horse_by_x) - math.floor(point_by_x) # определяем переменную х
software_by_y = math.floor(horse_by_y) - math.floor(point_by_y) # определяем переменную у


if horse_by_x < 0 or horse_by_y < 0 or point_by_x >=9 or point_by_y >= 9:
  print('Координаты введены некорректро')
else:
  if (software_by_x == -1 and software_by_y == -2) or (software_by_x == -2 and software_by_y == -1) or (software_by_x == -2 and software_by_y == 1) or (software_by_x == -1 and software_by_y == 2) or (software_by_x == 1 and software_by_y == -2) or (software_by_x == 2 and software_by_y == -1) or (software_by_x == 2 and software_by_y == 1) or (software_by_x == 1 and software_by_y == 2): # создаем проверку возможного хода
    
    print('Конь в клетке (', math.floor(horse_by_x),',', math.floor(horse_by_y), '). Точка в клетке (', math.floor(point_by_x),',', math.floor(point_by_y), ').')
    print('Да, конь может ходить вэту точку')
  else: # вывод если ни одно условие возможного хода не сработало
    print('Конь в клетке (', math.floor(horse_by_x),',', math.floor(horse_by_y), '). Точка в клетке (', math.floor(point_by_x),',', math.floor(point_by_y), ').')
    print('Нет, конь может ходить вэту точку')
