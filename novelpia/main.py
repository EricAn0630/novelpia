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

    # def __init__(self, token: Iterable[str] = None) -> None:
    #     self.token = token

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
                    novel = {
                        'title': res2[i]["novel_name"],
                        'author': res1["writer_nick"],
                        'description': res1["novel_story"],
                        'count': {
                            'view': res2[i]["count_view"],
                            'book': res2[i]["count_book"],
                            'good': res2[i]["count_good"]
                        },
                        'thumbnail': "https://image.novelpia.com" + res2[i]["novel_thumb"],
                        'is_secondary_creation': res2[i]["is_secondary_creation"],
                        'content_viewdate': res2[i]["content_viewdate"],
                        'novel_age': res2[i]["novel_age"],
                        'novel_no': res2[i]["novel_no"]
                    }
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
                    ROUTE + f"/novelsearch/{keyword}/",
                    headers=R_HEADER).content
            )["data"]["search_result"]

            for i in range(len(res1)):
                for j in range(len(res2)):
                    if int(res2[j]["novel_no"]) == res1[i]["novel_no"]:
                        novel = {
                            'title': res2[j]["novel_name"],
                            'author': res1[i]["writer_nick"],
                            'description': res1[i]["novel_story"],
                            'count': {
                                'view': res2[j]["count_view"],
                                'book': res2[j]["count_book"],
                                'good': res2[j]["count_good"]
                            },
                            'thumbnail': "https://image.novelpia.com" + res2[j]["novel_thumb"],
                            'is_secondary_creation': res2[j]["is_secondary_creation"],
                            'content_viewdate': res2[j]["content_viewdate"],
                            'novel_age': res2[j]["novel_age"],
                            'novel_no': res2[j]["novel_no"]
                        }
                        novels.append(novel)

            return novels
        except IndexError:
            raise NonExistNovel

    # def attendance(self):
    #     '''
    #     token에 해당하는 계정으로 출석합니다.
    #     연속출석을 모두 채울 시 실버코인이 지급됩니다.
    #     '''
    #     key = self.token
    #     data = {
    #         "csrf": "791bdd7505a7ee88b5f254c4789744e0", #csrf 토큰이 수시로 재발급되지만 실력이 부족하여 그 값을 받아오지 못합니다.
    #         "cmd": "attendance_check"
    #     }
    #     cookies = {"LOGINKEY": key}

    #     res1 = json.loads(
    #         requests.post(
    #             ROUTE + "/mileage_attendance_new/",
    #             data=data,
    #             cookies=cookies
    #         ).content
    #     )

    #     if res1["code"] == "200":
    #         data = {
    #             "csrf": "791bdd7505a7ee88b5f254c4789744e0",
    #             "cmd": "add_coin"
    #         }
    #         requests.post(
    #             ROUTE + "/mileage_attendance_new/",
    #             data=data,
    #             cookies=cookies
    #         )
    #     elif res1["code"] == "500":
    #         return res1["msg"]
    #     else:
    #         return res1

    def get_hotlist(self) -> List[dict]:
        '''
        현재 실시간 HOT의 조회수 TOP 3 작품들을 List로 리턴합니다.
        '''
        data = {
            "listpage": 0,
            "mode": "getHotList"
        }
        novels = []

        res = json.loads(
            requests.post(
                ROUTE + "/main/",
                data=data,
                headers=R_HEADER
            ).content
        )

        if res["status"] == "200":
            for i in range(len(res["result"])):
                novel = res["result"][i]
                novels.append(
                    {
                        'title': novel["novel_name"],
                        'author': novel["mem_nick"],
                        'thumbnail': "https:" + novel["novel_thumb"],
                        'novel_age': novel["novel_age"],
                        'novel_no': novel["novel_no"],
                        'tag': novel["novel_genre"]
                    }
                )
            return novels
