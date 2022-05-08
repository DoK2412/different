import random


class Life:
    """Создание рабочего экземпляра, подсчет кармы, запись ошибок"""
    score = 0
    line = 0

    def __init__(self, final_karma=500):
        self.__finalkarma = final_karma

    def get_final(self):
        return self.__finalkarma

    def one_day(self):
        if 1 / Life.score == 1/9:
            mistakes = [KillError, DrunkError,
                        CarCrashError, GluttonyError, DepressionError]
            mistake = random.choice(mistakes)
            Life.score = 0
            raise mistake('Ошибка типа: ', mistake)
        else:
            the_amount_of_karma = random.randint(1, 7)
            print('За сегодняшний день карма увеличилас '
                  'на: ', the_amount_of_karma)
            return the_amount_of_karma


# создание ошибок
class PossibleErrors(Exception):
    pass


class KillError(PossibleErrors):
    def __str__(self):
        return 'Определено исключение типа: ' \
               'KillError в строке: ' + str(Life.line)


class DrunkError(PossibleErrors):
    def __str__(self):
        return 'Определено исключение типа: ' \
               'DrunkError  в строке: ' + str(Life.line)


class CarCrashError(PossibleErrors):
    def __str__(self):
        return 'Определено исключение типа: ' \
               'CarCrashError  в строке: ' + str(Life.line)


class GluttonyError(PossibleErrors):
    def __str__(self):
        return 'Определено исключение типа: ' \
               'GluttonyError  в строке: ' + str(Life.line)


class DepressionError(PossibleErrors):
    def __str__(self):
        return 'Определено исключение типа: ' \
               'DepressionError  в строке: ' + str(Life.line)
