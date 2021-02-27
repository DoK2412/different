number_of_cells = int(input('Введите количество клеток: '))
list_of_cells = []

for cell in range(number_of_cells):
    efficiency = int(input(f'Эффективность {cell + 1} клетки: '))
    if efficiency < cell:
        list_of_cells.append(efficiency)

print('Неподходящие значения: ', ' '.join(map(str, list_of_cells)))
