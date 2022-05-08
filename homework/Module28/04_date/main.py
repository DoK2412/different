class Date:
    '''

    работа класс основана на слеующих методах:

    conversion - проверяет корректрость ввода данных
    from_string - формирует вовод даты по необходимым значеним
    is_date_valid - возвращает корректно введено значение или нет
        в виде буллового значения

    статическая переменная processed_date принимает значения даты если она
    прошла проверку

    '''
    processed_date = list()
    # у функции 2 задачи
    # 1: проверить правильность подачи даты
    # 2: сформировать список для работы с датой
    @classmethod
    def conversion(cls, date_str: str) -> bool:
        conversion = date_str.split('-')
        if 0 < int(conversion[0]) <= 31 and 0 < int(conversion[1]) <= 12 \
                and 0 < int(conversion[2]) <= 3000:
            Date.processed_date.extend(conversion)
            return True
        else:
            return False


    # метод для формирования вывода значний даты
    @classmethod
    def from_string(cls, date_str: str) -> str:
        Date.processed_date = list()
        if Date.conversion(date_str):
            return 'День: {day}\tМесяц: {month}\tГод: {year}'\
                        .format(day=Date.processed_date[0],
                                month=Date.processed_date[1],
                                year=Date.processed_date[2])
        else:
            Date.conversion(date_str)

    # метод для проверки корректрости введеной даты
    @classmethod
    def is_date_valid(cls, date_str: str) -> bool:
        return Date.conversion(date_str)


date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))
date = Date.from_string('24-12-2077')
print(date)
print(Date.is_date_valid('24-12-1993'))
print(Date.is_date_valid('31-12-2077'))
