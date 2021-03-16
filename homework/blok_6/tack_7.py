the_bell = False
at_work = False
tasks = 0
hours = 0
print('Начался 8-часовой рабочий день')
beginning = int(input('Вы прибыли на работу? 0/1'))
while True:
  if beginning == 1:
    at_work = True
    if at_work == True:
      hours += 1
      print(hours, 'час')
      work = int(input('Сколько задач решит Mаксим? '))
      tasks += work
      wife = int(input('Звонит жена. Взять трубку? 0/1'))
      if wife == 1:
        the_bell = True
      if hours == 8:
        print('Рабочий день закончился. Всего выполнено задач: ', tasks)
        break
if the_bell == True:
  print('Нужно зайти в магазин')
