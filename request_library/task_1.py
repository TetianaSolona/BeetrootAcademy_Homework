import requests
from bs4 import BeautifulSoup


def text_from_wikipedia(url):
    response = requests.get(url)
    bs = BeautifulSoup(response.text, 'lxml')
    data = bs.find_all('p')
    for a in bs.find_all('a'):
        a.replaceWith('')
    for s in bs.find_all('sup'):
        s.replaceWith('')
    for sp in bs.find_all('span'):
        sp.replaceWith('')
    with open('robot.txt', 'w', encoding='utf-8') as fb:
        for i in data:
            fb.write(i.getText())


text_from_wikipedia('https://ru.wikipedia.org/wiki/Python')
