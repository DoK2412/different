counter = 0
for number in range(30, 35):
  people = int(input('Людей в {} секторе: '.format(number)))
  if people < 10:
    print('Все спокойно')
  elif people >= 10:
    print('Нарушение! Слишком много людей в секторе!')
    counter += 1
print('Количество нарушений: ', counter)
