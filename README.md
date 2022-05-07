<div align="center">
    <h1>novelpia-python</h1>
</div>

> ### 노벨피아의 소설 데이터를 가져오는 비공식 라이브러리 입니다.
>초짜 급식이 만든거라 문법에 맞지 않는 곳이 **매우 많고**, 이상한 점이나 비효율적인 점도 **매우 많습니다**. 많이 지적해주세요.

사용 예
------
```py
from novelpia import Novelpia

novel = Novelpia()

print(novel.search_novel("노벨쨩의 기묘한 일상!"))
```

* ### 리턴
  ```
  {'novel_no': '19876', 
  'novel_name': '노벨쨩의 기묘한 일상!', 
  'novel_age': '0', 
  'novel_thumb': '/imagebox/cover/f0f4d53e8682b6fcaf99c69d2a375db8_108865_ori.file', 
  'mem_nick': '하와와노벨쨩', 
  'is_secondary_creation': '1', 
  'count_view': '171782', 
  'count_good': '19520', 
  'count_book': '19', 
  'content_viewdate': '2022-02-16 11:05:41'
  }
  ```  

현재 search_novel, search_novels만 사용 가능합니다.

--- 10 / 23 추가 ---

search_list를 추가하였읍니다.
간단하게 설명하면 search_novel과 비슷하지만 한 페이지 전체를 긁어오는 것입니다.


--- 11 / 9 추가 ---

리턴값에 표지 링크를 추가했읍니다.
다만 '표지 준비중' 표지를 제외한 다른 표지 링크는 모두 다운로드 링크이니 이 점 유의해주세요.
또한 PEP8에 최대한 맞춰(...) 보려고 코드의 한 줄의 최대 길이를 79자 이하로 바꿨읍니다.

--- 2022 / 5 / 8 추가 ---

대대적으로 리워크 했습니다. 이제 BeautifulSoup를 이용한 크롤링 방식이 아닌 노벨피아의 api를 이용하여 데이터를 가져오게 되었습니다.
이 모든 것은 시험이 끝났다고 심심해 했던 제가 노벨피아를 해체해 보던 도중 발견한 코드에 의해 급작스레 진행되었습니다. 솔직히 진짜로 찾을 줄 몰랐어요.
조만간 출석체크 기능이 생길 수 있습니다.
Docs는 헌재 구상중입니다.


