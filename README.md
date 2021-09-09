<div align="center">
    <h1>novelpia-python</h1>
</div>

> ### 노벨피아의 소설 데이터를 가져오는 비공식 라이브러리 입니다.
>초짜 급식이 만든거라 문법에 맞지 않는 곳이 **매우 많고**, 이상한 점이나 비효율적인 점도 **매우 많습니다**. 많이 지적해주세요.

사용 예
------
```py
from novelpia_python import search_novel

search_novel("노벨쨩의 기묘한 일상!")
```

* ### 리턴
  ```
    {
      'title': '노벨쨩의 기묘한 일상!',
      'author': '하와와노벨쨩', 
      'description': '노벨쨩은 오늘도 열심히 일하고 잇서요..!', 
      'is_free': True,
      'count': {'view': '48.9K', 'book': '9', 'good': '6.5K'},
      'tags': ['#판타지', '#현대', '#일상', '#무협', '#일기']
    }
  ```  

docs는 업습니다...

