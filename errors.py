class InvalidSortType(Exception):
    def __init__(self):
        super().__init__('올바르지 않은 정렬 순서 타입입니다.')

class NonExistNovel(Exception):
    def __init__(self):
        super().__init__('해당 소설은 존재하지 않습니다.')