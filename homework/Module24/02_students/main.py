from student import Student

list_of_students = list()
sorting_points = list()

# создание и запрос данных о студентах
for students in ['id_' + str(index) for index in range(1, 3)]:
    student = Student(
        input('\nВведите фамилию студента: '),
        input('Введите имя студента: '),
        input('Введите отчетсво студента: '),
        input('Введите группу студента: '),
        input('Введите список оценок студента: ').split()
        )
    # сохраняем общие данные и отдельно баллы
    list_of_students.append(student)
    sorting_points.append(student.academic_performance)

# создаем цикл для вывода сортировки
for scores in sorted(sorting_points):
    for studen in list_of_students:
        if scores == studen.academic_performance:
            studen.info_students()
