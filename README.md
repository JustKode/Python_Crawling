# Python Crawling
경희대 학생들이 프로젝트를 할 때 웹 크롤링을 하는 경우가 많습니다. 그래서 저는 학생들이 크롤링을 쉽게 할 수 있도록 이를 Class 형태로 제공, 자유롭게 웹 페이지들을 크롤링 할 수 있도록 준비했습니다.

단, 이러한 Crawling Class 들을 사적인 용도로 사용하지 마십시오. 법적인 제재를 받을 수 있습니다.
사적인 용도로 사용하여 얻는 불이익은 책임지지 않습니다.

## Installation
pip을 이용해 두 개의 모듈을 설치 해 주세요!

```bash
pip install requests
pip install bs4
```

## Usage

KLAS Class

```python
from klas import KLAS

klasObj = KLAS('KLAS 아이디', 'KLAS 비밀번호') # KLAS 아이디와 비밀번호를 입력 합니다.
klasObj.set_lecture_list() # 크롤링을 시행, 학생이 듣는 강의의 목록을 가져 옵니다. 성공 시 True, 실패 시 False를 반환합니다.
list_var = klasObj.get_lecture_list() # 크롤링을 해서 가져온 강의의 정보를 반환 합니다.
print(list_var) # 학생의 수강중인 강의 정보를 반환 합니다. ex) [{"subject": 강의명, "subjnum": 학수 번호, "professor": 교수명}, ...]
```

Everytime

```python
from everytime import Everytime

etObj = Everytime('에브리타임 아이디', '에브리타임 비밀번호') # 에브리타임의 아이디와 비밀번호를 입력 합니다.
etObj.set_lecture_list() # 크롤링을 시행, 2018년 2학기의 에타 시간표를 가져 온다.
etObj.set_lecture_list(2017, 2) # Parameter에 년도와 학기를 입력하여, 해당하는 년도와 학기의 시간표를 가져올 수 있습니다.
list_var = etObj.get_lecture_list() # 크롤링을 해서 가져온 강의의 정보를 반환 합니다.
print(list_var) # 학생의 수강중인 강의 정보를 반환 합니다. ex) [{"subject": 강의명, "subjnum": 학수 번호, "professor": 교수명}, ...]
```

## Contributing
pull request를 환영 합니다! 버그 혹은 문제점이 발생 했다면 github issues를 이용 해 주세요!

## License
[MIT](https://choosealicense.com/licenses/mit/)