cipher = input('Введите зашифрованное сообщение: ')
counter_1 = ''
counter_2 = ''

for checking_1 in cipher[0::2]: 
  counter_1+=checking_1
for checking_2 in cipher[1::2]:
  counter_2+=checking_2
counter_1+=counter_2[::-1]

print('Расшифрованное сообшение: ', counter_1)

