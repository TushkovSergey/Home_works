import requests
from find_match import find_match

from bs4 import BeautifulSoup

KEYWORDS = {'программирование', 'python', 'дизайн', 'фото', 'web'}

result = requests.get('https://habr.com/ru/all/')
soup = BeautifulSoup(result.text, features='html.parser')

link_list = soup.find_all('a', class_="tm-article-snippet__title-link")
for link in link_list:
    href = "https://habr.com" + link.get('href')
    result_href = requests.get(href)
    soup_href = BeautifulSoup(result_href.text, features='html.parser')
    article = soup_href.find(class_="article-formatted-body article-formatted-body_version-2")
    if article == None:
        article = soup_href.find(class_="article-formatted-body article-formatted-body_version-1")
    find_match_result = find_match(article.text, KEYWORDS)
    if find_match_result == 'true':
        time = soup_href.find('time')
        header = soup_href.find('h1')
        print(time.text)
        print(header.text)
        print(href)
        print('-'*20)
