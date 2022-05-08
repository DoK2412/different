import requests
import json

# получаем данные о общем количестве серий
page_parser = requests.get('https://breakingbadapi.com/api/episodes')
date = json.loads(page_parser.text)
# получаем данные о смертности в сериях
death_parser = requests.get('https://breakingbadapi.com/api/deaths')
death_date = json.loads(death_parser.text)
death = {'episode': 0, 'season': 0, 'number_of_deaths': 0}
# ищем наибольшее количество смертей в сериях и создаем словарь с данными
for i_death in death_date:
    if i_death['number_of_deaths'] > death['number_of_deaths']:
        death['episode'] = i_death['episode']
        death['season'] = i_death['season']
        death['number_of_deaths'] = i_death['number_of_deaths']
        death['death'] = i_death['death']
# сравниваем серию и сезон и получем номер серии в сквозном потоке
# после этого добавляем в ранее созданные словарь
for i_date in date:
    if i_date['episode'] == str(death['episode']) \
            and i_date['season'] == str(death['season']):
        death['episode_id'] = i_date['episode_id']
# выводим результат на экран
print('Наибольшее количество смертей было зафиксировано в {0} серии {1}'
      'сезона, оно заключалось в {2} человеческих жизней.'
      '\nСвязано это было с: {3}'.format(str(death['episode']),
                                         str(death['season']),
                                         str(death['number_of_deaths']),
                                         str(death['death'])))
# записываем резульат в файл
with open('result.json', 'a', encoding='utf-8') as result:
    result.write('Наибольшее количество смертей было зафиксировано в {0} '
                 'серии {1} сезона, оно заключалось в {2} человеческих '
                 'жизней.\nСвязано это было с: {3}'
                 .format(str(death['episode']),
                         str(death['season']),
                         str(death['number_of_deaths']),
                         str(death['death'])))
    print('\nДанные сохранены в файл: result.json')
