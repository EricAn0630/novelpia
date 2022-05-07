import json
from typing import Dict, Final, Iterable, List

import requests

from .errors import NonExistNovel

R_HEADER: Final[dict] = {
    'User-Agent': ('Mozilla/5.0 (Windows NT 10.0;Win64; x64)\
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98\
Safari/537.36')}

ROUTE: Iterable[str] = "https://novelpia.com/proc"


class Novelpia:

    def search_novel(self, keyword: Iterable[str]) -> Dict[str, str]:
        '''
        keyword와 연관된 소설의 데이터를 Dict로 리턴합니다.\n
        검색한 소설이 존재하지 않을 시 NonExistNovel 에러를 일으킵니다.\n
        연관된 소설이 복수일 시 조회수가 가장 많은 소설이 리턴됩니다.
        '''
        novel = {}

        params = {
            "page": 1,
            "search_text": keyword,
            "rows": 1
        }

        try:
            res1 = json.loads(
                requests.get(
                    ROUTE + "/novelsearch_v2/",
                    headers=R_HEADER,
                    params=params).content
            )["novel_search"]["list"][0]

            res2 = json.loads(
                requests.get(
                    ROUTE + f"/novelsearch/{keyword}",
                    headers=R_HEADER).content
            )["data"]["search_result"]

            for i in range(len(res2)):
                if int(res2[i]["novel_no"]) == res1["novel_no"]:
                    novel = res2[i]

            return novel
        except IndexError:
            raise NonExistNovel

    def search_novels(self, keyword: Iterable[str], amount: Iterable[int]) -> List[dict]:
        '''
        keyword와 연관된 소설들의 데이터를 amount의 수량만큼 List로 리턴합니다.\n
        List의 순서는 조회순입니다.
        '''
        novels = []

        params = {
            "page": 1,
            "search_text": keyword,
            "rows": amount
        }

        try:
            res1 = json.loads(
                requests.get(
                    ROUTE + "/novelsearch_v2/",
                    headers=R_HEADER,
                    params=params).content
            )["novel_search"]["list"]

            res2 = json.loads(
                requests.get(
                    ROUTE + f"/novelsearch/{keyword}",
                    headers=R_HEADER).content
            )["data"]["search_result"]

            for i in range(len(res1)):
                for j in range(len(res2)):
                    if int(res2[j]["novel_no"]) == res1[i]["novel_no"]:
                        novels.append(res2[j])

            return novels
        except IndexError:
            raise NonExistNovel
