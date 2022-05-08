def data_processing(n, x, y):
    if n == 1:
        print('Переложить диск {0} со стержня номер {1} на стержень номер {2}'.format(n, x, y) )
    else:
        transfer = 6 - x - y
        data_processing(n-1, x, transfer)
        print('Переложить диск {0} со стержня номер {1} на стержень номер {2}'.format(n, x, y) )
        data_processing(n-1, transfer, y)


n = int(input('Введите количество дисков: '))
x = 1
y = 3
data_processing(n, x, y)
