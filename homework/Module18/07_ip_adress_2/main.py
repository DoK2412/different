# функция для определения символа в цифрах (возвращает переключатель)
def check_numeric(ip):
    confirmation = True
    lowercase_characters = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
    for i_ip in ip:
        for i in i_ip:
            if i in lowercase_characters:
                print(i_ip, '- не целое число')
                confirmation = False
                break
    return confirmation
# функция для определения количества значений и величины ip адреса
def checking_for_a_string(ip):
    if len(ip) < 4:
            print('Адрес - это четыре числа, разделенные точками')
    else:
        for i_ip in ip:
            if 0 <= int(i_ip) >= 255:
                print(i_ip, 'превышает 255')
                break
        else:
            print('IP-адрес введен корректно')
# ввод ip адреса для проверки
ip = input('Введите ip адрес:').split('.')
# первая проверка ip адреса на наличие строчных значений
confirmation = check_numeric(ip)
# итоговая проверка ip адреса
if confirmation:
    checking_for_a_string(ip)
