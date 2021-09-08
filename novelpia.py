import requests
from bs4 import BeautifulSoup
from errors import NonExistNovel


class Novelpia:

    def search_novel_as_date(self, title: str):

        res = requests.get(f'https://novelpia.com/search/keyword/date/1/{title}')
        html = res.text
        soup = BeautifulSoup(html, 'html.parser')
        asd = soup.find_all('div', {"class": "col-md-12 novelbox mobile_hidden"})

        if asd == []:
            raise NonExistNovel

        for i in range(len(asd)):
            main = str(asd[i])
            novel = BeautifulSoup(main, 'html.parser')
            title = novel.find('b', {"style": "font-size:20px;letter-spacing: -2px;cursor:pointer;"})
            author = novel.find('b', {"style": "cursor:pointer;font-weight:500;"})
            print(f"{title.text} - {author.text}")



