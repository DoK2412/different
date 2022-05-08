import math


class Car:
    def __init__(self, x, y, angle):
        self.__x = x
        self.__y = y
        self.__angle = angle

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_angle(self):
        return self.__angle

    def moving_forward(self, naw_angle):
        self.__x = self.__x * math.cos(naw_angle) \
                   - self.__y * math.sin(naw_angle)
        self.__y = self.__x * math.sin(naw_angle) \
            + self.__y * math.cos(naw_angle)


class Bus(Car):
    def __init__(self, x, y, corner, passengers=0, money=0):
        super().__init__(x, y, corner)
        self.__passengers = passengers
        self.__money = money
        self.__number_of_passengers = 0

    def get_money(self):
        return self.__money

    def get_number_of_passengers(self):
        return self.__number_of_passengers

    def get_passengers(self):
        return self.__passengers

    def enter(self, gone, fare=50):
        self.__passengers += gone
        self.__number_of_passengers += gone
        self.fare(gone, fare)

    def its_out(self, out):
        self.__passengers -= out

    def fare(self, gone, fare):
        self.__money += fare * gone

    def __str__(self):
        return 'В автобусе ' + str(self.__passengers) + \
               ' пассажиров, сумма заработаных денег: ' + str(self.__money)
