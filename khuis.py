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
            user_res = session.post('https://info21.khu.ac.kr/com/KsignCtr/loginProc.do', data=login_info2, allow_redirects=True)
            user_res = session.get('https://khuis.khu.ac.kr/java/ksign/index.jsp', allow_redirects=True)
            user_res = session.get('https://khuis.khu.ac.kr/java/servlet/controllerCosy?action=19&menuId=hsip&startpage=start', allow_redirects=True)
