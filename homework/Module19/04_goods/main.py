goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# раскрыли первый список
for name, code in goods.items():
    # переменные на подсчет суммы и количества
    quantity = 0
    summ = 0
    # раскрываем второй список и считаем количество и сумму
    for item in store[code]:
        quantity += item['quantity']
        summ += item['quantity'] * item['price']
    # выводим данные на экран
    print('{0}  {1} - шт, стоимость {2} руб'.format(name, quantity, summ))
