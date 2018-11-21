#ETLEC : EveryTime Lecture Evaluation Crawling
import requests
from bs4 import BeautifulSoup

class ETLEC:
    def __init__(self, userid, password):
        self.userid = userid
        self.password = password
        self.auth = False
        self.professorList = []
        self.lectureList = []
        self.LEList = []
    
    def set_auth(self):
        login_info = {'userid': self.userid, 'password': self.password, 'redirect': '/'}
        base_url = 'https://everytime.kr'

        with requests.Session() as session:
            user_res = session.post(base_url+'/user/login', data=login_info)
            soup = BeautifulSoup(user_res.text, 'html.parser').select('body div')

            # 첫 번째 예외 처리 // 로그인 실패
            if len(soup) == 0:
                self.auth = False
                return False
            

            self.auth = True
            return True
    
    def set_professor_list(self, year, semester):
        self.professorList = []

        if self.auth == False:
            return

        login_info = {'userid': self.userid, 'password': self.password, 'redirect': '/'}
        form_data = {'campusId':'8', 'year': year, 'semester': semester, 'startNum': '0', 'limitNum' : '50'}


        with requests.Session() as session:
            user_res = session.post('https://everytime.kr/user/login', data=login_info)
            user_res = session.post('https://everytime.kr/find/timetable/subject/list', data=form_data)

            soup = BeautifulSoup(user_res.text, 'lxml-xml')
            temp = set(map(lambda x: x["professor"], soup.select('subject')))
            temp_set = set(temp)
            print(temp)

            i = 0
            while len(temp) != 0:
                i += 50
                form_data['startNum'] = str(i)
                user_res = session.post('https://everytime.kr/find/timetable/subject/list', data=form_data)

                soup = BeautifulSoup(user_res.text, 'lxml-xml')
                temp = set(map(lambda x: x["professor"], soup.select('subject')))

                temp_set = temp_set | temp

            self.professorList = list(temp_set)
            return

    def get_professor_list(self):
        return self.professorList

    def set_lecture_list(self):
        self.lecutreList = []

        if self.auth == False:
            return

        login_info = {'userid': self.userid, 'password': self.password, 'redirect': '/'}

        temp = set()
        
        with requests.Session() as session:
            user_res = session.post('https://everytime.kr/user/login', data=login_info)

            for i in self.professorList:
                user_res = session.post('https://everytime.kr/find/lecture/list/keyword', data={'keyword': i})
                soup = BeautifulSoup(user_res.text, 'lxml-xml')

                temp_set = set(map(lambda x: x["id"], soup.select('lecture')))
                temp = temp | temp_set
            
            self.lectureList = list(temp)
            return

    def get_lecture_list(self):
        return self.lectureList





        
    