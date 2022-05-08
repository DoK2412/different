import requests
from bs4 import BeautifulSoup
# получаем исходный код страници
site_page = requests.get('http://www.columbia.edu/~fdc/sample.html')
# переводим полученные данные в текст
date = BeautifulSoup(site_page.text, 'html.parser')
# извлекаем все теги h3 из полученного файла
sorted_tags = date.find_all('h3')
# выводим циклом чистые данные без тегов html разметки
for tags in sorted_tags:
    print(tags.text)
