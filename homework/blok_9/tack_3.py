мessage=input('Введите сообщение: ')
counter=1
for checking in мessage:
  if checking == '*':
    print("Символ '*' стоит на позиции: ", counter)
    break
  counter+=1
