import deductionOtaxes


# функция для подсчета общего налога
def general_tax(house_tax, car_tax, dacha_tax):
    return house_tax.the_tax + car_tax.the_tax \
           + dacha_tax.the_tax


money = int(input('Введите количество ваших денег: '))
# созданеи экземляров имущества
house_tax = deductionOtaxes.Apartment(
    int(input('Введите стоимость квартиры: ')))
car_tax = deductionOtaxes.Car(int(input('Введите стоимость машины: ')))
dacha_tax = deductionOtaxes.CountryHouse(
    int(input('Введите стоимость дачи: ')))
# вывод даннх о погошении налогов
if money > general_tax(house_tax, car_tax, dacha_tax):
    print('Ваших денег хватает что бы оплатить налоги\nНалог составляет: ',
          general_tax(house_tax, car_tax, dacha_tax))
else:
    print('Для оплаты налогов вам не хватает: ',
          general_tax(house_tax, car_tax, dacha_tax) - money)