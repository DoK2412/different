n = input('Введите слово: ') # запрашиваем слово

if n == n[::-1]: #сравниваем слово с его перевернутым значеним
    print('Слово является палиндромом')
else:
    print('Слово не является палиндромом')