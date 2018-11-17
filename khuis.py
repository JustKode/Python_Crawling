from bs4 import BeautifulSoup
import requests
import json

class KHUIS:
    def __init__(self, userId, password):
        self.userId = userId
        self.password = password

    def auth(self):
        base_url = 'https://info21.khu.ac.kr/com/KsignCtr/checkAndGetSocpsId.do'
        login_info = {'userId':self.userId, 'userPw':self.password}
        login_info2 = {'userId':self.userId, 'userPw':self.password, 'returnurl':None, 'socpsId':'', 'loginRequest':''}

        with requests.Session() as session:
            user_res = session.post(base_url, data=json.dumps(login_info), allow_redirects=True)
            temp_json = json.loads(user_res.text)

            if temp_json['result'] == "pass":
                return 0
            elif temp_json['result'] == "noUser":
                return 1
            elif temp_json['result'] == "wrongPswd":
                return 2
            else:
                return 3


    def get_student_info(self):
        base_url = 'https://info21.khu.ac.kr/com/KsignCtr/checkAndGetSocpsId.do'
        login_info = {'userId':self.userId, 'userPw':self.password}
        login_info2 = {'userId':self.userId, 'userPw':self.password, 'returnurl':None, 'socpsId':'', 'loginRequest':''}

        with requests.Session() as session:
            user_res = session.post(base_url, data=json.dumps(login_info), allow_redirects=True)
            user_res = session.post('https://info21.khu.ac.kr/com/KsignCtr/loginProc.do', data=login_info2, allow_redirects=True)
            user_res = session.get('https://khuis.khu.ac.kr/java/ksign/index.jsp', allow_redirects=True)
            user_res = session.get('https://khuis.khu.ac.kr/java/servlet/controllerCosy?action=19&menuId=hsip&startpage=start', allow_redirects=True)
            
            soup = BeautifulSoup(user_res.text, 'html.parser')
            list_var = list(map(lambda x: x.text, soup.select('#GNB-student > p')))

            name = list_var[0][list_var[0].find(':') + 2:-1]
            temp = list_var[1].split()
            college = temp[2]
            major = temp[3]
            
            temp = session.cookies.get_dict()
            studentID = temp['EMP_NO']
            birth = temp['JUMINNO'][:6]

            return {'studentID': studentID, 'name': name, 'college':college, 'major':major, 'birth': birth}

