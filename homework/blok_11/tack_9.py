import math # подключаем библтотеку
# получаем от пользователя переменные
a = int(input('Введите первое число: ')) 
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))
print('Решите квадратное уравнение: ax2+bx+c=0')

discriminant = (b ** 2) - ((4*a)*c) # вычисляем дискриминант 
# отталкиваясь от дискриминанта вычисляем корни
if discriminant > 0:
  root_1 = (-b + math.sqrt(discriminant)) / (2 * a)
  root_2 = (-b - math.sqrt(discriminant)) / (2 * a)
  print(' 1 корень: ', root_1,'\n','2 корень: ', root_2)
elif discriminant == 0:
  root = (-b - math.sqrt(discriminant)) / (2 * a)
  print('В данном выражении один корень: ', root) 
else:
  print('У уровнения нет корней.')
