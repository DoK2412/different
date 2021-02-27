video_cards = int(input('Введите количество видеокарт: '))
list_video_cards = [] # список под все видеокарты
new_list_video_cards = [] #список под оставшиеся видеокарты

for i in range(video_cards): # получение и сохранение в список видеокарты
    maps = int(input(f'{i + 1} Видеокарта: '))
    list_video_cards.append(maps)

maximum_generation = max(list_video_cards) # определения наибольшего поколения видеокарты

for i in list_video_cards: # отсеиваем из списка проданные видеокарты
    if maximum_generation != i:
        new_list_video_cards.append(i)

# вывод старого и нового списка видеокарт
print('Старый список видеокарт: ', list_video_cards)
print('Старый список видеокарт: ', new_list_video_cards)