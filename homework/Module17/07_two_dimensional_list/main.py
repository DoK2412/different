# создаем список со значениями от 1 до 12
all_values = [number for number in range(1, 13)]
# режем список по индексам и создаем новые
filtering_1 = [all_values[separation::4] for separation in range(len(all_values) // 3)]
# выводим данные
print(filtering_1)


# мне очень понравилось решение этой задачи
# вначале я хотел решить ее таким образом

# режем список на части через сркзы
#filtering_1 = [str(all_values[::4])]
#filtering_2 = [str(all_values[1::4])]
#filtering_3 = [str(all_values[2::4])]
#filtering_4 = [str(all_values[3::4])]
# соединяем их вместе
#total_value = [filtering_1 + filtering_2 + filtering_3 + filtering_4]

# но когда его написал обратил внимание что срез всегда идет по 4 значению и меня осенило
# c каждым разом мне нравится этот язык все больше и больше

# Другой вариант:
my_list = [[j_num for j_num in range(i_list, 13, 4)] for i_list in range(1, 5)]
print(my_list)
