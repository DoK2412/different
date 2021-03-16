
def corridor():
  motion= int(input('Мы в коридоре. Куда идем? \n1 - в спальню \n2 - в ванну \n3 - на кухню \n4 - в дверь\n'))
  if motion == 1:
    bedroom()
  elif  motion == 2:
    bath()
  elif  motion == 3:
    kitchen()
  elif  motion == 4:
    print('Вы вышли из квартиры.\nИгра окончена')
  
def bedroom():
  motion= int(input('Мы в спальне. Куда идем? \n1 - в ванну \n2 - в корридор\n'))
  if motion == 1:
    bath()
  elif  motion == 2:
    corridor()

def bath():
  motion= int(input('Мы в ванне. Куда идем? \n1 - в спальню \n2 - в корридор\n'))
  if motion == 1:
    bedroom()
  elif  motion == 2:
    corridor()

def kitchen():
  motion= int(input('Мы на кухне. Куда идем? \n1 - в корридор \n2 - в окно\n'))
  if motion == 1:
    corridor()
  elif  motion == 2:
    print('Серьезно? В окно? с 13 этажа?\nИгра окончена!')


corridor() 

# не буду расписывать каждую функцию, создал 4 функции, с одной запустил программу и начал водить по комнатам пока не выбросился из окна или вышел через дверь