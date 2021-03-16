the_lower_bound = int(input('ВВедите нижнюю границу: '))
the_upper_limit = int(input('Введите верхнюю границу: '))
step = int(input('Введите шаг: '))

print('C',' '* 2, 'F') # создаем шкалу Фаренгейта и Цельсия
for work in range(the_lower_bound, the_upper_limit+1, step): # задаем цикл с диапазоном работы
  temperature = int(work * 1.8 + 32) #переводим цельсий в фарингейт
  print(work, '\t', round(temperature, 2))

temperature = int(the_upper_limit * 1.8 + 32) # так как нам нужна вержняя точка постоянно прописываем ее вне цикла
print(the_upper_limit, '\t',round(temperature, 1)) 
