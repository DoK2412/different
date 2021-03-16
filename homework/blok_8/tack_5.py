number_1 = int(input('Первая сторона письма: '))
number_2 = int(input('Вторая сторона письма: '))
area_envelope = 144 # площадь конверта
area_sheet = number_1 * number_2 # площать письма
counter = 0 # счетчик для подсчета сложений
for folding in range(area_envelope, area_sheet + 1):
  area_sheet /= 2 # уменьшаем площадь вдвое (складываем лист)
  counter += 2 
  if area_sheet <= area_envelope: # сравниваем площадь конверта и листа
    print('Письмо поместится в конверт если сложить его',counter, 'разa')
    break
