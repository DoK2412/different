# получение данных от пользователя 
summ_purchases = float(input('Введите стоимость покупки в евро: '))
#конвертация чисел 
conversion = float((summ_purchases * 1.25) * 60.87)
# вывод данных конвертации
print('Ваша покупка составит', round(conversion, 2), 'рублей')
