nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
# делаем тройной вложенной цикл for и у нас все готово))
end_list = [divin_3 for divin_1 in nice_list for divin_2 in divin_1 for divin_3 in divin_2]
# осталось вывести данные)
print(end_list)
