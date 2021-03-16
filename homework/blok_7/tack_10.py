cards = int(input('Введите количество карточек в игре: '))
progression = 0
for number in range(1, cards + 1):
  progression += number
for number in range(cards - 1):
  progression -= int(input('Введите карточку: '))
print('Не хватает карточки: ', progression)
