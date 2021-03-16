dug_up = int(input('Бабушка с дедушкой вскопали: '))
distance = int(input('На каком расстоянии посажена картошка: '))
potato = 0
for number in range(dug_up, 101, distance):
  potato += 3
print('Антон накопал:', potato, 'клубня картошки.')
