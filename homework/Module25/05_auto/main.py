import MotorTransport

x = int(input('Введите точку Х в которой находится транспорт: '))
y = int(input('Введите точку Y в которой находится транспорт: '))
corner = int(input('Введите в каком направление двидется '
                   'транспорт (в градусах): '))

bus = MotorTransport.Bus(x, y, corner)

while True:
    bus_actions = int(input('Введите действие:'
                            '\n1. Сели пассажиры.'
                            '\n2. Вышли пассажиры.'
                            '\n3. Изменилось направление двужения.'
                            '\n4. Рейс окончен\n'))
    if bus_actions == 1:
        number_of_passengers = int(input('Введите сколько пассажиров село: '))
        if (number_of_passengers > 20) or \
                (bus.get_passengers() + number_of_passengers > 20):
            print('В автобусе не хватает мест всем желающим.'
                  '\nВсего свободных мест: ', 20 - bus.get_passengers())
        else:
            # MotorTransport.Bus.enter(bus, number_of_passengers)
            # TODO почему не так? Это же проще:
            bus.enter(number_of_passengers)
            print(bus)
    elif bus_actions == 2:
        checking_passengers = True
        while checking_passengers:
            passengers_out = int(input('Введите сколько пассажиров вышло: '))
            if bus.get_passengers() < passengers_out:
                print('Из автобуса не может выйти больше людей чем зашло!')
            else:
                MotorTransport.Bus.its_out(bus, passengers_out)
                print('Вышло {0} пассажира.\nСвободных мест в автобусе: {1}'
                      .format(passengers_out, 20 - bus.get_passengers()))
                checking_passengers = False
    elif bus_actions == 3:
        naw_angle = int(input('Введите на сколько градусов '
                              'повернул автобус: '))
        MotorTransport.Bus.moving_forward(bus, naw_angle)
        print('Автобус продолжает двидение к точке: {0} {1}'
              .format(int(bus.get_y()), int(bus.get_x())))
    elif bus_actions == 4:
        print('За дань вы заработали : {0}, общее число перевезенных '
              'пассажиров: {1}'.format(bus.get_money(),
                                       bus.get_number_of_passengers()))
        break
