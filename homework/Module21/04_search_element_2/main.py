site = {
    'html': {
        'head': {
            'title': 'Мой сайт',
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'

        }
    }
}


def search(site, the_desired_value, number):
    if the_desired_value in site:
        return site[the_desired_value]
    if number > 1:
        for i_site in site.values():
            if isinstance(i_site, dict):
                result = search(i_site, the_desired_value, number - 1)
                if result:
                    return result
                if number == 0:
                    break
        else:
            result = None


# запрос данных и вызов функции
the_desired_value = input('Какой ключ ищем? ')
number = int(input('Введие глубину поиска: '))
meaning = search(site, the_desired_value, number)

if meaning:
    print(meaning)
else:
    print('Такого ключа нет')

# зачтено
