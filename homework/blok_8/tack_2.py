tree = int(input('Сколько лет было дереву? '))
period = int(input('Как часто будем сажать деревья? '))
alena = 6
counter = 0
for landing in range(6, tree + 1, period):
  trees = int(input('Сколько посадим деревьев в этот раз? '))
  counter += trees
print('За', tree - alena, 'лет посажено',counter, 'деревьев')
