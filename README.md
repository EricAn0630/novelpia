<h1>novelpia-python</h1>


> ### 비공식 노벨피아 API Wrapper 라이브러리
>현직 고등학생이 야매로 만들었기 때문에 많이 이상할 수 있습니다.

<img src="https://img.shields.io/pypi/v/novelpia">

## 사용 예

```py
from novelpia import Novelpia

novelpia = Novelpia()

def get_novel(title):
  novel = novelpia.search_novel(title)
  print(novel)

get_novel("노벨쨩의 기묘한 일상!")
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
<br>

#### 여담
  현재 파이썬에 대해 공부중인 고1이 평소에 즐겨보던 *소설 연재 웹사이트 노벨피아*를 호기심에 뜯어보다가 발견한 것들을 바탕으로
  예전에 크롤링 연습을 위해 만든 노벨피아 크롤링 라이브러리를 재작성하였습니다.


