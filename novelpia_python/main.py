import requests
from bs4 import BeautifulSoup
from novelpia_python.errors import NonExistNovel

class Novelpia:

    def search_novel(self, keyword: str):
        '''
        소설 데이터를 dict로 리턴합니다.\n
        검색한 소설이 존재하지 않을 시 NonExistNovel 에러를 일으킵니다.
        '''

        res = requests.get(f'https://novelpia.com/search/keyword/date/1/{keyword}')
        html = res.text
        soup = BeautifulSoup(html, 'html.parser')
        div = soup.find_all('div', {"class": "col-md-12 novelbox mobile_hidden"})
        tags_list = []

        if div == []:
            raise NonExistNovel

        #1페이지의 모든 소설 이름이랑 저자를 가져오는건데 지우기엔 아깝고 모든 소설 반환은 아직 안만들어서 남겨둔 코드
        # for i in range(len(div)):
        #     nv = str(div[i])
        #     novel = BeautifulSoup(nv, 'html.parser')
        #     title = novel.find('b', {"style": "font-size:20px;letter-spacing: -2px;cursor:pointer;"})
        #     author = novel.find('b', {"style": "cursor:pointer;font-weight:500;"})
        #     description = novel.find('font', {"style": "font-size:14px;color:#666;font-weight:400;"})
        nv = str(div[0])
        novel = BeautifulSoup(nv, 'html.parser')

        title = novel.find('b', {"style": "font-size:20px;letter-spacing: -2px;cursor:pointer;"}).text
        author = novel.find('b', {"style": "cursor:pointer;font-weight:500;"}).text
        description = novel.find_all('font', {"style": "font-size:14px;color:#666;font-weight:400;"})[1].text
        is_free = novel.find('span', {"class": "b_free s_inv"})
        if is_free == None:
            is_free = False
        else:
            is_free = True
        tags = novel.find_all('span', {'style': 'color:#5032df;border: 2px solid #5032df; border-radius: 20px; padding: 3px 10px; line-height: 20px; user-select: none;cursor:pointer;'})
        count = novel.find('span', {"style": "font-size:14px;font-weight:600;color:#333;"}).text



        for i in range(len(tags)):
            tags_list.append(tags[i].text)

        view, f = count.split('명')
        book, s = f.split('회차')
        good = s.split('회')[0]

        view = ''.join(view.split())
        book = ''.join(book.split())
        good = ''.join(good.split())
        return {
            "title": title,
            "author": author,
            "description": description,
            "is_free": is_free,
            "count": {
                "view": view,
                "book": book,
                "good": good
            },
            "tags": tags_list
        }
