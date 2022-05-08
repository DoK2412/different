import copy
site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iphone',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}

'''в функции обрабатывем исходный файл, видоизменяем
нужные нам данные и возвращаем полученое из функции'''


def search(copy_site, site, number_of_sites):
    first_conversion = 'Куплю/продам телефон недорого'
    second_conversion = 'У нас самая низкая цена на iphone'
    for meaning in site.values():
        for v_meaning in meaning.values():
            for key, values in v_meaning.items():
                if values == first_conversion:
                    copy_site['html']['head']['title'] = 'Куплю/продам {0} недорого'.format(products)
                if values == second_conversion:
                    copy_site['html']['body']['h2'] = 'У нас самая низкая цена на {}'.format(products)
    return copy_site
# запрашиваем у вользователя количество сайтов
# и создаем место их хранения
number_of_sites = int(input('Сколько сайтов: '))
ite_database = dict()

'''создаем цикл обработки и выводаданных данных,
создаем передачу новых сайтов в хранилище и обработку
сайтов на вывод данных'''
for number in range(number_of_sites):
    copy_site = copy.deepcopy(site)
    products = input('\nВведтье название продукции: ')
    ite_database[products] = search(copy_site, site, number_of_sites)

    for product, website in ite_database.items():
        for v_website in website.values():
            print('\n', product)
            for site_data in v_website.values():
                print('\t', site_data)
