
def cannuity_payment(summ, percent, deadline): #считаем  аннуитетный платёж
  calculation = ((percent / 100) * ((1 + (percent / 100)) ** deadline)) / ((1 + (percent / 100)) ** deadline - 1) 
  ap = calculation * summ
  return ap # возвращаем значение

summ = float(input('Введите сумму кредите: '))
deadline = int(input('На сколько лет: '))
percent = float(input('Какой процент годовых:'))
period = 0 # период
score = 0 # итерации
extension = 0 #конечная итерация

payment = round(cannuity_payment(summ, percent, deadline), 2)# запрос функции

while summ != 0: # работа цикла
  period += 1
  print('\nПериод: ', period)
  
  print('Остаток долга на начало периода: ', summ)

  amount_for_the_year = summ * percent / 100 # % за год
  print('Выплачено процентов за год: ', amount_for_the_year)
  
  bodies_paid_out = payment - amount_for_the_year # вычисляем тело кредита
  print('Выплачно тела кредита: ', bodies_paid_out)
  summ  -= bodies_paid_out
  score += 1

 #запрос новых данных и остановка цикла
  if score == 3:
    print('\nОстаток долга: ', round(summ, 2)) 
    period = 0
    deadline_2 = int(input('\n\tНа сколько лет продревается договор: '))
    extension = deadline_2 + deadline #определяем сколько у нас будет еще итераций
    deadline = deadline - score + deadline_2 # определяем какой срок осталось выплачивать кредит
    percent = float(input('\tУвеличение ставки до: '))
    
    payment = round(cannuity_payment(summ, percent, deadline), 2)# запрашиваем новые данные из функции

  elif score == extension: # заканчиваем цикл
    print('\nОстаток долга: ', summ)
    break