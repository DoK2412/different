# запрашиваем количество чисел в списке и создаем на этой основе свисок
request_for_quantity = int(input('Сколько чисоел будет в списке? '))
numerology = [int(input('Введите число: ')) for _ in range(request_for_quantity)]
# создаем цикл и проверяем наличие 0 если находим то стораем и 
# переносим в конец списка по индексу
for transfer in numerology:
    if transfer == 0:
        numerology.remove(transfer)
        numerology.insert(len(numerology), transfer)
print(numerology)
# проверяем еще раз список и добавляем в него все значения кроме 0
numerology = [check for check in numerology if check != 0]
print(numerology)
