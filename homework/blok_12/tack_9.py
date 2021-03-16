import random # я использовал в этой программе модуль рандома

def rock_paper_scissors(): # создаем функцию на первую игру
  print('Для остановки игры введите 0')
  while True:
    action = int(input('Ваше выбор: \n1 - камень, \n2 - ножницы, \n3 - бумага\n'))
    the_effect_of_computer = random.randint(1,3)
    if action == 1 and the_effect_of_computer == 1:
      print('Ничья\n')
    elif action == 1 and the_effect_of_computer == 2:
      print('Вы выйграли\n')
    elif action == 1 and the_effect_of_computer == 3:
      print('Компьютер выйграл\n')
    elif action == 2 and the_effect_of_computer == 1:
      print('Компьютер выйграл\n')
    elif action == 2 and the_effect_of_computer == 2:
      print('Ничья\n')
    elif action == 2 and the_effect_of_computer == 3:
      print('Вы выйграли\n')
    elif action == 3 and the_effect_of_computer == 1:
      print('Вы выйграли\n')
    elif action == 3 and the_effect_of_computer == 2:
      print('Компьютер выйграл\n')
    elif action == 3 and the_effect_of_computer == 3:
      print('ничья\n')
    elif action == 0:
      print('Игра остановлена\n')
      break
    else:
      print('Неопределенная команда')
  mainMenu() # возвращаесмя в главное меню

def guess_the_number(): # запускаем функцию на вторую игру
  print('Выберете число от 1 до 10 \nДля остановки игры введите 0 ')
  while True:
    the_user = int(input('Введте число:'))
    computer = random.randint(1, 10)
    if the_user < computer:
      print('Число немного больше')
    elif the_user > computer:
      print('Число немного меньше')
    elif the_user == computer:
      print('Угадал!')
    elif the_user == 0:
      print('Игра окончена')
      break
  mainMenu() # возвращаемся в главное меню


def mainMenu(): # создаем функцию с главным меню
  print('Я хочу сыграть с тобой в игру!')
  game = int(input('Выбери игру:  \n1 - «Камень, ножницы, бумага»\n2 - «Угадай число»\n'))
  if game == 1:
    rock_paper_scissors()
  elif game == 2:
    guess_the_number()
  else:
    print('Команда не определена')
  
mainMenu() # запускаем программу через функцию
