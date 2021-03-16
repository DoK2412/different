number = int(input('Введите количество проверяемых чисел: '))
theInitialNumber = 0 #получеое число
summOfTheNumber = 0 #сумма числа
theHighestAmount = 0 # наибольшая сумма
theHargestNumber = 0 # число с наибольшей суммой


for processing in range(number):
  score = int(input('Введите число: '))
  theInitialNumber = score # передаем первое число в контейнер числа

  while score > 0: # цикл на подсчет суммы числа
    summ = score % 10
    summOfTheNumber += summ 
    score //= 10
    

  if summOfTheNumber > theHighestAmount: # сравнение если сумма числа больше преведещей то:
    theHighestAmount = summOfTheNumber # переопредеение если полученная сумма больше преведущей то перезаписываем контейнер
    theHargestNumber = theInitialNumber # переопределение контейнера числом сумма которого была наибольшей
    summOfTheNumber = 0 #обнуляем конйнер суммы для новой утерации
    theInitialNumber = 0 # обнуляем контейнер числа для новой итерации
  else:
    summOfTheNumber = 0# обнуляем контейнер суммы в случае если сумма не оказалась больше преведущей

print('Введенное число ', theHargestNumber, ' и его сумма: ', theHighestAmount)
