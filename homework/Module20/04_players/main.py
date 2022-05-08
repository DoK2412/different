# создаем функцию для обработкт базы данных
def database_processing(base):
    # создаем цикл для обработки полученной информации
    # и список для ее хранения
    base_conversion = list()
    for key, value in players.items():
        base_conversion.append(key + value)
    # возвращаем обработанные данные в запрос
    return base_conversion

players = {
    ("Ivan", "Volkin"): (10, 5, 13),
    ("Bob", "Robbin"): (7, 5, 14),
    ("Rob", "Bobbin"): (12, 8, 2)
}
# запрос функции и вывод данных
print(database_processing(players))
