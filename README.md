<div align="center">
    <h1>novelpia-python</h1>
</div>

> ### 노벨피아의 소설 데이터를 가져오는 비공식 라이브러리 입니다.
>초짜 급식이 만든거라 문법에 맞지 않는 곳이 **매우 많고**, 이상한 점이나 비효율적인 점도 **매우 많습니다**. 많이 지적해주세요.

사용 예
------
```py
from novelpia_python import Novelpia

novel = Novelpia()

print(novel.search_novel("노벨쨩의 기묘한 일상!"))
```

* ### 리턴
  ```
  {
      'title': '노벨쨩의 기묘한 일상!',
      'author': '하와와노벨쨩', 
      'description': '노벨쨩은 오늘도 열심히 일하고 잇서요..!', 
      'is_free': True,
      'count': {'view': '48.9K', 'book': '9', 'good': '6.5K'},
      'tags': ['#판타지', '#현대', '#일상', '#무협', '#일기'],
      'thumbnail': 'https://image.novelpia.com/imagebox/cover/f0f4d53e8682b6fcaf99c69d2a375db8_108865_ori.thumb'
  }
  ```  
   
아직 search_novel 밖에 만들지 못했읍니다.   
docs는 업습니다...


--- 10/23 추가 ---

search_list를 추가하였읍니다.
간단하게 설명하면 search_novel과 비슷하지만 한 페이지 전체를 긁어오는 것입니다.


--- 11/9 추가 ---

리턴값에 표지 링크를 추가했읍니다.
다만 '표지 준비중' 표지를 제외한 다른 표지 링크는 모두 다운로드 링크이니 이 점 유의해주세요.
또한 PEP8에 최대한 맞춰(...) 보려고 코드의 한 줄의 최대 길이를 79자 이하로 바꿨읍니다.



