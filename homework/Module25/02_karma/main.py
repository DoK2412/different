import simulator
# общая карма и экземпляр класса
daily_karma = 0
first_life = simulator.Life()
# цикл подсчета карты
while daily_karma <= simulator.Life.get_final(first_life):
    try:
        simulator.Life.score += 1
        simulator.Life.line += 1
        daily_karma += simulator.Life.one_day(first_life)
        print('Общая карма: ', daily_karma)
    except (simulator.KillError, simulator.DrunkError,
            simulator.CarCrashError, simulator.GluttonyError,
            simulator.DepressionError) as error:
        # запись ошибок в файл
        with open('karma.log', 'a', encoding='utf-8') as karma:
            karma.write(str(error) + '\n')

print('Поздравляем Ваша карма превысила необходимую норму!')
