class Potato:
    maturity = {0: 'посажен', 1: 'росток',  2: 'цветоние', 3: 'созрела'}

    # инициализация посадки
    def __init__(self, seedling):
        self.height = 0
        self.seedling = seedling

    # рост картошки
    def heigh(self):
        if self.height <= 4:
            self.height += 1
            self.info_height()

    # информация о росте картошки
    def info_height(self):
        print('{0} находится на стадиии роста: {1}'
              .format(self.seedling, Potato.maturity[self.height]
                      ))


class GardenBed:
    # инициализация грядки
    def __init__(self, seedlings, ):
        self.list_of_potatoes = [
            Potato(seedlings) for potatoes in
            range(1, int(input('Сколько саженцев бужем сажать? ')) + 1)]

    # вывод информации о росте
    def info_potato(self):
        for i in self.list_of_potatoes:
            Potato.info_height(i)


class TheGardener:
    # инициализация садивника
    def __init__(self, name):
        self.delay = 0
        self.name = name
        self.gardeners_menu()

    # садим грядку
    def planting_a_garden_bed(self):
        self.content = input('Введите что сажаем на грядке: ')
        self.working_bed = GardenBed(self.content).list_of_potatoes
        for seedling in self.working_bed:
            Potato.info_height(seedling)
        self.work()

    # уход за грядкой
    def care_of_the_garden_bed(self):
        try:
            if self.working_bed:
                for seedlin in self.working_bed:
                    if seedlin.height < 3 and seedlin.seedling == self.content:
                        Potato.heigh(seedlin)
                if seedlin.height == 3:
                    collection = input(
                        '\n\tПосадка взашла!\n\tХотите собрать урожай? да/нет '
                        )
                    if collection.lower() == 'да':
                        self.collecting_beds()
                    else:
                        if self.delay == 2:
                            new_sowing = input(
                                '\t\nУрожай испортился!\
\t\nХотите посадить новую грядку? да/нет ')
                            if input.lower() == 'да':
                                self.gardeners_menu()
                            else:
                                print('\nНа нет и суда нет :D')
                        print('\t\nУрожаю больше расти не может!')
                        self.delay += 1
                        self.care_of_the_garden_bed()
                self.work()
        except AttributeError:
            not_planted = input(
                '\nГрядка не засажена.\nЗасадить грядку? да/нет ')
            if not_planted.lower() == 'да':
                self.planting_a_garden_bed()
            else:
                print('\nПоговорите с садовником.')
                self.gardeners_menu()

    # сбор грядки
    def collecting_beds(self):
        print(f'Садовник {self.name} собрал {self.content} в колличестве\
 {len(self.working_bed)} штук.')
        self.working_bed.clear()

        re_boarding = input('\n\tХотите повторно засадить грядку? да/нет ')
        if re_boarding.lower() == 'да':
            self.gardeners_menu()
        elif re_boarding.lower() == 'нет':
            print('Садовник ушел отдыхать.')


    # действия садовника
    def gardeners_menu(self):
        self.action = int(input(
            '\nВыберите возможное действие:\n\t\
1. Посадить грядку.\n\t2. Взять выходной.\n'))
        if self.action == 1:
            self.planting_a_garden_bed()
        elif self.action == 2:
            print('{0} насегодня взял выходной.'.format(self.name))
        else:
            print('Вы ввели неверное действие.')
            self.gardeners_menu()

        # работа на грядке
    def work(self):
        works = int(input('\nЧем займеся на гядке?\n\t1. Полить.\
 \n\t2. Убрать соряки\n\t3. Опрыскать от паразитв.\n'))
        if works == 1:
            self.care_of_the_garden_bed()
        elif works == 2:
            self.care_of_the_garden_bed()
        elif works == 3:
            self.care_of_the_garden_bed()
