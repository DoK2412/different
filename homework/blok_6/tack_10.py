beginning = 1
end = 100
while True:
  number = (beginning + end) // 2
  print('Ваше число: ', number, '? 1 - равно, 2 - больше, 3 - меньше')
  request = int(input())
  if request == 1:
    print('Я его угадал!')
    break
  elif request == 2:
    beginning = number + 1
  else:
    end = number - 1
