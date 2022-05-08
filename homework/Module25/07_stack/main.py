import stack

task_list = stack.Store()
sorting_the_drain = dict()
while True:
    # Запрос дейтвий от пользователя
    action = int(input('Выбирете действие:\n1 - Ввести работу;'
                       '\n2 - Вывести приоритет работ.\n'))
    if action == 1:
        # добавление данных в список
        stack.TaskManager.new_task(task_list,
                                   (input('Ввеите работу: '),
                                    int(input('Введите приоритет: '))))
    elif action == 2:
        # после формирование задач, распределяем их по степени важности
        # и стираем из основного списка
        # работа происходит от последнего поступившего элемента к первому
        # по принципу последним пришел первым ушел
        for work in task_list.stack[::-1]:
            if work[1] in sorting_the_drain:
                sorting_the_drain[work[1]].append(work[0])
                stack.TaskManager.deleting_an_element(task_list)
            else:
                sorting_the_drain[work[1]] = list()
                sorting_the_drain[work[1]].append(work[0])
                stack.TaskManager.deleting_an_element(task_list)
        break
# вывод отсортированных данных пользователю
for priority, case in sorted(sorting_the_drain.items()):
    print(priority, ', '.join(case))

