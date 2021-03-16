
algebra = int(input('Введите колличество боллов по алгебре: '))
informatics = int(input('Введите колличество боллов по информатике: '))
russian = int(input('Введите колличество боллов по русскому языку: '))
result = algebra + informatics + russian
if result >= 190:
  print('Поздравляю вы поступили на бюджет набрав: ', result, 'баллов')
else:
  print('К сожалению вы не поспупили. Вам не хватило:', 190 - result, 'баллов')