for number in range(10, 100):
  part_1 = number // 10
  part_2 = number % 10
  result = (part_1 * part_2) * 3
  if result == number:
    print('Числа равные утроенному произведению своих цифр: ', result)
