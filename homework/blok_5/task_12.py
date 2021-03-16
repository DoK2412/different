
time = int(input('Введите время: '))

if (time >= 0 and time < 8) or (time >= 10 and time <12) or (time >= 14 and time < 15) or (time >= 18 and time < 20) or time >= 22:
  print('Посылку получить нельзя')

#if (time >= 8 and time < 10) or (time >= 12 and time < 14) or (time >= 15 and time < 18) or (time >= 20 and time < 22):
  #print('Можно получить посылку')