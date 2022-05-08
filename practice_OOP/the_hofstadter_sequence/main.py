from collections.abc import Iterator
import sys

class Qsequence:
    """Класс осуществляет посдчет последовательности Хофштадтера"""
    def __init__(self, q: int, stop: int) -> None:
        self.set_q(q)
        self.counter = 2
        self.stop = stop

    def __iter__(self) -> Iterator:
        return self

    def __next__(self) -> int:
        if self.counter == self.stop:
            raise StopIteration
        else:
            number = self.q[self.counter - self.q[self.counter - 1]] + \
                self.q[self.counter - self.q[self.counter - 2]]
            self.counter += 1
            return number

    def set_q(self, q):
        if q == [1, 1]:
            self.q = q
        else:
            print('Не удалось сгенерировать последовательность, '
                  'введены неточные значения.')
            sys.exit()


print('Для точной генерации последовательности Хофштадтера '
      'значения должны быть 1 1!')
q = list((int(input('Введите первое значние: ')),
          int(input('Введите второе значение: '))))

stop = int(input('Укажите сколько чисел последовательности '
                 'Вы хотите вывести: '))
q_sequence = Qsequence(q, stop)
for i_sequence in q_sequence:
    q.append(i_sequence)
print('Последовательность Хофштадтера сгенерирована: \n ', ' '.join(map(str, q)))
