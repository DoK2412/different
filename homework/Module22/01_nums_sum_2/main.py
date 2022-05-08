import os

# переменная для суммы
the_amount = 0
# обработка первого файла определение данных и счет суммы
file_processing = open(os.path.join('numbers.txt'), 'r', encoding='utf-8')
print('Содержимое файла numbers.txt')
for i_file in file_processing:
    print(i_file, end='')
    if i_file.strip():
        the_amount += int(i_file.strip())
file_processing.close()
# создание файла и сохранение в него данных
with open('answer.txt', 'w') as data:
    data.write(str(the_amount))
# вывод данных из второго файла
print('\nСодержимое файла answer.txt')
with open('answer.txt', 'r') as data:
    data_output = data.read()
    print(data_output)
