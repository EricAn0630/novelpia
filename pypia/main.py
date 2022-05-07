import requests
import json
from typing import List, Dict, Final
from .errors import NonExistNovel

R_HEADER: Final[dict] = {
'User-Agent' : ('Mozilla/5.0 (Windows NT 10.0;Win64; x64)\
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98\
Safari/537.36') }

class Novelpia:

    def search_novel(self, keyword: str) -> Dict[str, str]:
        '''
        keyword와 연관된 소설의 데이터를 Dict로 리턴합니다.\n
        검색한 소설이 존재하지 않을 시 NonExistNovel 에러를 일으킵니다.\n
        연관된 소설이 복수일 시 조회수가 가장 많은 소설이 리턴됩니다.
        '''

        params = {
            "page": 1,
            "search_text": keyword,
            "rows": 1
        }

        res1 = json.loads(
            requests.get(
                "https://novelpia.com/proc/novelsearch_v2/",
                headers=R_HEADER,
                params=params).content
        )["novel_search"]["list"][0]

        res2 = json.loads(
            requests.get(
                f"https://novelpia.com/proc/novelsearch/{keyword}",
                headers=R_HEADER
            )
        )["data"]["search_result"]


    def search_novels(self, keyword: str, amount: int) -> List[dict]:
        '''
        keyword와 연관된 소설들의 데이터를 amount의 수량만큼 List로 리턴합니다.\n
        List의 순서는 조회순입니다.
        '''
