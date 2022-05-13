class NonExistNovel(Exception):
    def __init__(self):
        super().__init__('해당 소설에 대한 검색 결과가 존재하지 않습니다.')