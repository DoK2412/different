north_south = 8
east_west = 10


while True:
  sides = input(f'Марсоход в позиции {north_south, east_west} куда дальше едем? север - W, юг - S, запад - A, восток - D ')

  if sides == 'W' and north_south < 20:
    north_south += 1
  elif sides == 'S' and north_south > 0:
    north_south -= 1
  elif sides == 'A' and east_west < 20:
    east_west += 1
  elif sides == 'D' and east_west > 0:
    east_west -= 1
  elif north_south == 20 or north_south == 0 or east_west == 20 or east_west == 0:
    print('Марсоход уперся в стену')
  else:
    print('Команда не распознана!')
