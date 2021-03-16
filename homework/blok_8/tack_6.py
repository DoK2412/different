educational_grant  = int(input('Ежемесячная стипендия: '))
expenses  = int(input('Расходы на проживание: '))
summ_scholarship = educational_grant
zoom_expenses = expenses
summ_expenses = 0
for folding in range(2, 11):
  #print(folding, 'месяц') # вывод месяца

  zoom_expenses += zoom_expenses * 0.03
  #print('Сумма расходов', zoom_expenses) # вывод расходов в месяц с учетом 3%

  summ_scholarship += educational_grant
  #print('Сумма стипендии',summ_scholarship) # вывод суммы стипендии

  summ_expenses += zoom_expenses
  #print('Сумма расходов общая',summ_expenses + expenses) # вывод общей суммы с процентами 
  #print() #

result = int((summ_expenses + expenses) - summ_scholarship)
print('Для нормального проживания необходимо попросить у родителей:',result, 'рублей')
