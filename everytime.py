import requests
from bs4 import BeautifulSoup

class Everytime():
    def __init__(self, userid, password):
        self.userid = userid
        self.password = password
        self.auth = False
        self.lecture_list = []

    def set_lecture_list(self, year=2018, semester=2):
        userId = self.userid
        password = self.password

        self.lecture_list = []

        login_info = {'userid': userId, 'password': password, 'redirect': '/'}
        base_url = 'https://everytime.kr'

        with requests.Session() as session:
            user_res = session.post(base_url+'/user/login', data=login_info)
            soup = BeautifulSoup(user_res.text, 'html.parser').select('body div')

            # 첫 번째 예외 처리 // 로그인 실패
            if len(soup) == 0:
                return False
            
            table_res = session.post(base_url+'/find/timetable/table/list/semester', data={"year":year, "semester":semester})
            
            # 두 번째 예외 처리 // 시간표 없음
            soup = BeautifulSoup(table_res.text, 'lxml')
            id_token = soup.select_one("table")["id"]
            
            if id_token == None:
                return False

            lecture_res = session.post(base_url+'/find/timetable/table', data={"id": id_token})
            lecture_soup = BeautifulSoup(lecture_res.text, "html.parser")

            num_list = list(map(lambda x: x["value"], lecture_soup.select("internal")))
            name_list = list(map(lambda x: x["value"], lecture_soup.select("name")))
            professor_list = list(map(lambda x: x["value"], lecture_soup.select("professor")))

            for i in range(len(num_list)):
                self.lecture_list.append({"subject": name_list[i], "subjnum": num_list[i], "professor": professor_list[i]})

            self.auth = True


        return True

    def get_lecture_list(self):
        return self.lecture_list