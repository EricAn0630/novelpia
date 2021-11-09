import requests
from bs4 import BeautifulSoup

from .errors import NonExistNovel


class Novelpia:

    def search_novel(self, keyword: str) -> dict:
        '''
        소설 데이터를 dict로 리턴합니다.\n
        검색한 소설이 존재하지 않을 시 NonExistNovel 에러를 일으킵니다.
        '''

        res = requests.get(
            f'https://novelpia.com/search/keyword/date/1/{keyword}'
            )
        html = res.text
        soup = BeautifulSoup(html, 'html.parser')
        div = soup.find_all(
            'div',
            {"class": "col-md-12 novelbox mobile_hidden"}
            )

        tags_list = []

        if div == []:
            raise NonExistNovel

        nv = str(div[0])
        novel = BeautifulSoup(nv, 'html.parser')

        title = novel.find(
            'b',
            {"style": "font-size:20px;letter-spacing: -2px;cursor:pointer;"}
            ).text
        author = novel.find(
            'b',
            {"style": "cursor:pointer;font-weight:500;"}
            ).text
        description = novel.find_all(
            'font',
            {"style": "font-size:14px;color:#666;font-weight:400;"}
            )[1].text
        is_free = novel.find(
            'span',
            {"class": "b_free s_inv"}
            )
        tags = novel.find_all(
            'span',
            {'style': 'color:#5032df;border: 2px solid #5032df; '
            'border-radius: 20px; padding: 3px 10px; line-height: 20px; '
            'user-select: none;cursor:pointer;'}
            )
        count = novel.find(
            'span',
            {"style": "font-size:14px;font-weight:600;color:#333;"}
            ).text
        thumbnail = novel.find(
            'img',
            {"style": "height:150px;width:100px;box-shadow: 2px 0px 10px 0px "
            "rgba(0,0,0,0.3);background-position:center;border-radius: 0px "
            "30px 30px 0px;"}).get('data-src')

        if is_free == None:
            is_free = False
        else:
            is_free = True

        for i in range(len(tags)):
            tags_list.append(tags[i].text)

        v, i = count.split('명')
        b, j = i.split('회차')
        g = j.split('회')[0]

        view = ''.join(v.split())
        book = ''.join(b.split())
        good = ''.join(g.split())

        return {
            "title": title,
            "author": author,
            "description": description,
            "is_free": is_free,
            "count": {
                "view": view,
                "book": book,
                "good": good,
            },
            "tags": tags_list,
            "thumbnail": "https:" + thumbnail,
        }

    def search_list(self, keyword:str) -> list:
        """
        검색 1페이지의 모든 소설 데이터를 dict로 묶어서 list로 리턴합니다.
        """
        res = requests.get(
            f'https://novelpia.com/search/keyword/date/1/{keyword}'
            )
        html = res.text
        soup = BeautifulSoup(html, 'html.parser')
        div = soup.find_all(
            'div',
            {"class": "col-md-12 novelbox mobile_hidden"}
            )
        
        novel_list = []

        if div == []:
            raise NonExistNovel

        for i in range(len(div)):
            nv = str(div[i])
            novel = BeautifulSoup(nv, 'html.parser')
            tags_list = []

            title = novel.find(
                'b',
                {"style": "font-size:20px;letter-spacing: -2px;"
                "cursor:pointer;"}
                ).text
            author = novel.find(
                'b',
                {"style": "cursor:pointer;font-weight:500;"}
                ).text
            description = novel.find_all(
                'font',
                {"style": "font-size:14px;color:#666;font-weight:400;"}
                )[1].text
            is_free = novel.find(
                'span',
                {"class": "b_free s_inv"}
                )
            tags = novel.find_all(
                'span',
                {"style": "color:#5032df;border: 2px solid #5032df; "
                "border-radius: 20px; padding: 3px 10px; line-height: 20px; "
                "user-select: none;cursor:pointer;"}
                )
            count = novel.find(
                'span',
                {"style": "font-size:14px;font-weight:600;color:#333;"}
                ).text
            thumbnail = novel.find(
                'img',
                {"style": "height:150px;width:100px;"
                "box-shadow: 2px 0px 10px 0px rgba(0,0,0,0.3);"
                "background-position:center;"
                "border-radius: 0px 30px 30px 0px;"}
                ).get('data-src')

            if is_free == None:
                is_free = False
            else:
                is_free = True

            for i in range(len(tags)):
                tags_list.append(tags[i].text)

            v, i = count.split('명')
            b, j = i.split('회차')
            g = j.split('회')[0]

            view = ''.join(v.split())
            book = ''.join(b.split())
            good = ''.join(g.split())

            novels = {
                "title": title,
                "author": author,
                "description": description,
                "is_free": is_free,
                "count": {
                    "view": view,
                    "book": book,
                    "good": good
                },
                "tags": tags_list,
                "thumbnail": "https:" + thumbnail,
            }

            novel_list.append(novels)
        
        return novel_list
