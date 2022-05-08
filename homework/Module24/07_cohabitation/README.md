## Задача 7. Совместное проживание
Для того, чтобы понять, стоит ли Артёму жить с кем-то или всё же остаться в гордом одиночестве,
он решил провести довольно необычное “исследование”. Для этого он реализовал модель человека и модель дома.
Человек может:
- Есть (+сытость, -еда)
- Работать (-сытость, +деньги)
- Играть (-сытость)
- Ходить в магазин за едой (+еда, -деньги)

У человека есть имя, степень сытости (изначально 50) и дом. 

В доме есть холодильник с едой (изначально 50 еды) и тумбочка с деньгами (изначально 0 денег)

Если сытость человека становится меньше нуля, то человек умирает.

Логика действий человека определяется следующим образом:
1. Генерируется число кубика от 1 до 6
2. Если сытость < 20, то поесть
3. Иначе если еды в доме < 10, то сходить в магазин
4. Иначе если денег в доме < 50, то работать
5. Иначе если кубик равен 1, то работать
6. Иначе если кубик равен 2, то поесть
7. Иначе играть

По такой логике “эксперимента” человеку надо прожить 365 дней.

Реализуйте такую программу и создайте двух людей, живущих в одном доме. Проверьте работу программы несколько раз. Надеемся, эти люди живы...