import accommodation
import random

# действия мужа
def duties_of_a_husband(husband, house, results):
    if husband.satiety < 20:
        accommodation.People.to_eat(husband, house, results)
    elif husband.happiness < 30:
        if husband.happiness < 40:
            accommodation.Husband.game(husband)
        else:
            accommodation.People.petting_the_cat(husband)
    else:
        accommodation.Husband.work(husband, house, results)

# действия жены
def duties_of_a_wife(wife, house, results):
    if wife.satiety < 20:
        accommodation.People.to_eat(wife, house, results)
    elif house.dirt > 95:
        accommodation.Wife.cleaning(wife, house)
    elif wife.happiness < 30:
        if wife.happiness < 30 and house.money > 500:
            accommodation.Wife.buying_a_fur_coat(wife, house, results)
        else:
            accommodation.People.petting_the_cat(wife)
    elif house.peoples_food < 50:
        accommodation.Wife.buying_food(wife, house)

# действия кота
def the_life_of_a_cat(cat, house, results):
    actions_of_the_cat = random.choice(('спать', 'драть обои'))
    if cat.satiety < 15:
        accommodation.Cat.eat(cat, house, results)
    if actions_of_the_cat == 'спать':
        accommodation.Cat.sleep(cat)
    elif actions_of_the_cat == 'драть обои':
        accommodation.Cat.tear_up_the_wallpaper(cat, house)

# создание всех необходимых параметров
results = accommodation.ResultsForTheYear()
house = accommodation.House()
husband = accommodation.Husband(input('Введите имя мужа: '))
wife = accommodation.Wife(input('Введите имя жены: '))
cat = accommodation.Cat(input('Введите кличку первого кота: '))
day = 1

# цикл работы на год
while day <= 365:
    print('День: ', day)
    duties_of_a_husband(husband, house, results)
    duties_of_a_wife(wife, house, results)
    the_life_of_a_cat(cat, house, results)
    for i in (husband, wife, cat, house):
        print(i)
    print()
    # работа с грязью в доме
    house.dirt += 5
    if house.dirt > 90:
        husband.happiness -= 10
        wife.happiness -= 10
    # остановка цикла если кто то умер
    if husband.satiety < 0 or husband.happiness < 10:
        print(husband.name, 'умер')
        break
    elif wife.satiety < 0 or wife.happiness < 10:
        print(wife.name, 'умер')
        break
    elif cat.satiety < 0:
        print(cat.name, 'умер')
        break

    day += 1
# вывод данных прожитого года
print(results)
