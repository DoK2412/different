import organization
# создание экземпляра класса
list_of_employees = list()
# запись работкников
ivan = organization.Manager('Иван', 'Петров', '27')
list_of_employees.append(ivan)
lena = organization.Manager('Лена', 'Спиридонова', '36')
list_of_employees.append(lena)
sweta = organization.Manager('Света', 'Сергеева', '42')
list_of_employees.append(sweta)
alexey = organization.Agent('Алексей', 'Петухов', '25', 80000)
list_of_employees.append(alexey)
sasha = organization.Agent('Саша', 'Верховодов', '38', 54000)
list_of_employees.append(sasha)
ksenia = organization.Agent('Ксюша', 'Давнина', '29', 71000)
list_of_employees.append(ksenia)
yura = organization.Worker('Юра', 'Матрюшин', '35', 120)
list_of_employees.append(yura)
oleg = organization.Worker('Олег', 'Савин', '45', 90)
list_of_employees.append(oleg)
nastya = organization.Worker('Настя', 'Совина', '21', 95)
list_of_employees.append(nastya)
# вывод данных всех работников
for worker in list_of_employees:
    print(worker)
