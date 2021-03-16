import math #подключаем модуль

radius = float(input('Введите радиус планеты: ')) #получаем радиус от пользователя

radius_land = 10.8321 * (10 ** 11) # считаем радиус земли
p = math.pi # определяем число пи

the_volume = (4/3 * p) * (radius ** 3) #считаем радиус мифической планеты

# создаем проверку масштабов планет
if radius_land > the_volume: 
  comparing_the_amount = radius_land / the_volume
  print('Объём планеты Земля больше в', round(comparing_the_amount, 3), 'раз')
else:
  comparing_the_amount = the_volume / radius_land
  print('Объём планеты Земля меньше в', round(comparing_the_amount, 3), 'раз')


