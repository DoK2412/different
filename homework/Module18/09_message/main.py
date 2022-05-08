# запрашиваем у пользователя строку и список символов для проверки
proposal = input('Сообщение: ').split()
signs = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '"', '№', ';', ':', '?', '.', ',', '\\', '/', '|']
c = 0
# берем каждое слово из списка полученной строки
for i in proposal:
    # делаем цикл на проверку если в строке нет симполов
    for x in signs:
        if x not in i:
            proposal[c] = i[::-1]
    # делаем цикл на провеерку если в строке есть символ
    for z in i:
        if z in signs:
            # проверка на наличие символа в начале
            if i.startswith(z):
                proposal[c] = i[0] + i[len(i):0:-1]
            # проверка на наличие символа в конце
            elif i.endswith(z):
                proposal[c] = i[len(i)-2::-1] + i[len(i)-1]
            # проверка на наличие символа внутри
            elif z in signs:
                for b in signs:
                    if z == b:
                        sign_in_the_center = i.index(z)
                        proposal[c] = i[sign_in_the_center-1::-1] + i[sign_in_the_center] + i[:sign_in_the_center:-1]
    c += 1
# вывод данных
print(' '.join(proposal))
