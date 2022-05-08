import re
# регулярные вырадения для проверки номеров
regular_private = r'\b\w{1}\d{3}\w{2}\d{2,3}'
regular_tax = r'\b\w{2}\d{3}\d{2,3}'
# список имеющихся номеров
list_car = 'А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666'
# проверка на личные машины
private_car = re.findall(regular_private, list_car)
print('Список номеров частных автомобилей:', private_car)
# проверка на машины такси
tax_car = re.findall(regular_tax, list_car)
print('Список номеров такси:', tax_car)
