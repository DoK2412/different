# получаем от пользователя переменные
a = int(input('Введите на какой угол повернулась часовая стрелка : ')) 
degrees_minutes = 0

degrees_in_hours = 360 / 12 # сколько градусов в 1 часе
degrees_per_minute = 360 / degrees_in_hours # сколько градусов проходит минутная стрелка при 1 градусе часовой

solution_of_the_condition = int(a * degrees_per_minute) % 360 # определяем где находится минутная стрелка

print('Когда часовая стрелка на', a ,'градусах', 'минутная стрелка находится на', solution_of_the_condition, 'гадусах')
