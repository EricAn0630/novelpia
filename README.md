<div align="center">
    <h1>novelpia-python</h1>
</div>

> ### 비공식 노벨피아 API WRAPPER 라이브러리
>현직 고등학생이 야매로 만들었기 때문에 많이 불안정합니다.

사용 예
------
```py
from novelpia import Novelpia

novel = Novelpia()

print(novel.search_novel("노벨쨩의 기묘한 일상!"))
```

* ### 리턴
  ```
  {
    'title': '노벨쨩의 기묘한 일상!', 
    'author': '하와와노벨쨩', 
    'description': '노벨쨩은 오늘도 열심히 일하고 잇서요..!', 
    'count': {
      'view': '171915', 
      'book': '19', 
      'good': '19524'
    }, 
    'thumbnail': 'https://image.novelpia.com/imagebox/cover/f0f4d53e8682b6fcaf99c69d2a375db8_108865_ori.file', 
    'is_secondary_creation': '1', 
    'content_viewdate': '2022-02-16 11:05:41', 
    'novel_age': '0', 
    'novel_no': '19876'
  }
  ```


--- 2022 / 5 / 8 추가 ---

대대적으로 리워크 했습니다. 이제 BeautifulSoup를 이용한 크롤링 방식이 아닌 노벨피아의 api를 이용하여 데이터를 가져오게 되었습니다.
이 모든 것은 시험이 끝났다고 심심해 했던 제가 노벨피아를 해체해 보던 도중 발견한 코드에 의해 급작스레 진행되었습니다. 솔직히 진짜로 찾을 줄 몰랐어요.
조만간 출석체크 기능이 생길 수 있습니다.
Docs는 헌재 구상중입니다.


--- 2022 / 5 / 9 추가 ---

출석체크 기능 대신 get_hotlist가 생겼습니다. 실시간 Hot 작품 중 TOP 3 작품들을 가져오는 기능입니다.
리턴 값에 변경점이 생겼습니다. 키 네임이 예전과 유사하게 변경되었습니다.


