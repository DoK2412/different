weekday = int(input('Введите номер дня недели: '))
time = int(input('Введите количество часов до конца рабочего дня: '))

if weekday == 1:
  print('Сегодня понедельник.')
  if time == 0:
    print('Рабочий день окончен пора домой')
  elif time > 0:
    print('Осталось работать всего', time , 'часов')
elif weekday == 2:
  print('Сегодня вторник')
  if time == 0:
    print('Рабочий день окончен пора домой')
  elif time > 0:
    print('Осталось работать всего', time , 'часов')
elif weekday == 3:
  print('Сегодня среда')
  if time == 0:
    print('Рабочий день окончен пора домой')
  elif time > 0:
    print('Осталось работать всего', time , 'часов')
elif weekday == 4:
  print('Сегодня четверг')
  if time == 0:
    print('Рабочий день окончен пора домой')
  elif time > 0:
    print('Осталось работать всего', time , 'часов')
elif weekday == 5:
  print('Сегодня пятница')
  if time == 0:
    print('Рабочий день окончен пора домой')
  elif time <=2:
    print('Можно уйти пораньше')
  elif time > 0:
    print('Осталось работать всего', time , 'часов')
elif weekday == 6:
  print('Сегодня суббота')
  if time == 0:
    print('Рабочий день окончен пора домой')
  elif time > 0:
    print('Осталось работать всего', time , 'часов')
elif weekday == 7:
  print('Сегодня воскресенье')
  if time == 0:
    print('Рабочий день окончен пора домой')
  elif time > 0:
    print('Осталось работать всего', time , 'часов')
else: 
    print('На вторые сутки')
