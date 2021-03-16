run = int(input('Какой пробег по показаниям: '))
day = int(input('Какой сегодня день: '))
a=(run//100)%10
b=(run%100)//10
c=run%10
sum = a + b + c
if sum > day:
  print('Сброс')
else:
  print('Сегодня не сломался')
