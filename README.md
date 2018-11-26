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

Everytime Class

```python
from everytime import Everytime

etObj = Everytime('에브리타임 아이디', '에브리타임 비밀번호') # 에브리타임의 아이디와 비밀번호를 입력 합니다.
etObj.set_lecture_list() # 크롤링을 시행, 2018년 2학기의 에타 시간표를 가져 옵니다. 성공 시 True, 실패 시 False를 반호나 합니다.
etObj.set_lecture_list(2017, 2) # Parameter에 년도와 학기를 입력하여, 해당하는 년도와 학기의 시간표를 가져올 수 있습니다.
list_var = etObj.get_lecture_list() # 크롤링을 해서 가져온 강의의 정보를 반환 합니다.
print(list_var) # 학생의 수강중인 강의 정보를 반환 합니다. ex) [{"subject": 강의명, "subjnum": 학수 번호, "professor": 교수명}, ...]
```

KHUIS Class

```python
from khuis import KHUIS

khuisObj = KHUIS('Info21 아이디', 'Info21 비밀번호') # Info21의 아이디와 비밀번호를 입력 합니다.
khuisObj.auth() # 0 = 로그인 성공, 1 = 유저 없음, 2 = 비밀번호 오류, 3 = 기타 에러
khuisObj.get_student_info() # {'studentID': 학번, 'name': 이름, 'college': 단과 대학, 'major': 전공, 'birth' : 생년월일}

```

Dorm2Food Class

```python
from dorm2food import Dorm2Food

dorm2 = Dorm2Food() # Dorm2Food 객체 생성
dorm2.getTodayFood()
# 오늘 학식 반환 {'mor_main': 아침 메뉴, 'lun_main' : 점심 메뉴, 'eve_main' : 저녁 메뉴, 'special' : 특식, 'mor_sub' : 체육부 아침, 'lun_sub' : 체육부 점심, ''}
dorm2.getSpecialFood() # 이번주 특식 반환 {'special': 특식}
dorm2.getDayFood(1) # 이번주 월~일요일 학식 반환 (1~7 입력), getTodayFood와 반환 형식은 같다.
dorm2.getNextDayFood() # 다음날 학식 반환
# 긁을 수 없는 상황 (ex : 업데이트 안 됨, 다음날의 자료 없음 등등)에는 빈 array를 반환 한다.
```

ETLEC Class (에브리타임의 강의 리뷰를 모두 긁는다.)

```python
from ETLEC import ETLEC

etlec = ETLEC('에브리타임 아이디', '에브리타임 비밀번호')
etlec.set_auth() # 로그인 확인, 성공 시 True, 실패 시 False
etlec.set_professor_list('년도', '학기') # 해당 년도와 학기에 강의를 시행하는 교수 리스트 설정
etlec.set_lecture_list() # 교수 리스트에 있는 교수명들을 이용, 강의 ID 설정
etlec.set_evaluate_list() # 강의 ID를 이용, 강의 평가 리스트 설정
etlec.get_evaluate_list() # [{'university': '경희대학교', 'instructor': '교수명', 'title': '강의명', 'point': '평점', 'content': '강의 '}]

# 긁을 수 없는 상황 (ex : 업데이트 안 됨, 다음날의 자료 없음 등등)에는 빈 dict를 반환 한다.
```

Mongoplate Class

```python
from mangoplate import Mangoplate

mango = Mangoplate() # Mangoplate 객체 생성
mango.setUrl('영통') # 검색어 설정
mango.setEvaluateList() # 크롤링을 통해 가게 리스트와, 리뷰 리스트를 설정한다. 
mango.getStoreList(1) # 가게 리스트 반환
mango.getEvaluateList() # 리뷰 리스트 반환

# 긁을 수 없는 상황 (ex : 업데이트 안 됨, 다음날의 자료 없음 등등)에는 빈 dict를 반환 한다.
```

## Contributing
pull request를 환영 합니다! 버그 혹은 문제점이 발생 했다면 github issues를 이용 해 주세요!

## License
[MIT](https://choosealicense.com/licenses/mit/)
