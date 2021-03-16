
x = int(input('Введите сумму вклада в банке: '))
p = int(input('Введите процент ежегодной надбавки: '))
y = int(input('Введите необходимую сумму: '))
years = 0
interest_amounts = (x / 100) * p
while x <= y:
  x += interest_amounts
  years += 1
print(years)