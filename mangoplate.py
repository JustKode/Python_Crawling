from bs4 import BeautifulSoup
import requests
import json
from random import randint

class Mangoplate:
    def __init__(self):
        self.urlList = []
        self.storeList = []
        self.evaluateList = []
        self.baseUrl = "https://www.mangoplate.com"
    
    def setUrl(self, keyword):
        with requests.Session() as session:
            res_obj = session.get(self.baseUrl + "/search/" + keyword)
            soup = BeautifulSoup(res_obj.text, 'html.parser')
            metaString = str(soup.select('head > meta')[2])
            start_index = metaString.find(" 검색결과는") + 7
            end_index = metaString.find("건", start_index)
            objectNum = int(metaString[start_index:end_index].replace(",", ""))

            for i in range((objectNum // 20) + 1):
                res_obj = session.get(self.baseUrl + "/search/" + keyword + "?keyword=" + keyword + "&page=" + str(i))
                soup = BeautifulSoup(res_obj.text, 'html.parser')
                temp_var = soup.select('figcaption > div.info > a')
                temp = list(map(lambda x : x["href"], temp_var))
                print(temp)
                self.urlList.extend(temp)
                
            return

    def setEvaluateList(self):
        with requests.session() as session:
            for i in self.urlList:
                res_obj = session.get(self.baseUrl + i)
                soup = BeautifulSoup(res_obj.text, 'html.parser')
                
                name = soup.select_one('h1.restaurant_name')
                if name == None:
                    name = ''
                else:
                    name = name.text

                table = soup.select('section.restaurant-detail > table > tbody > tr')
                
                address = ""
                phone = ""
                category = ""
                price = ""
                parking = ""
                time = ""

                for i in table:
                    if i.th.text == "주소":
                        if i.th.span == None:
                            address = i.td.text
                        else:
                            address = i.td.text.span
                    elif i.th.text == "전화번호":
                        if i.th.span == None:
                            phone = i.td.text
                        else:
                            phone = i.td.text.span
                    elif i.th.text == "음식 종류":
                        if i.th.span == None:
                            category = i.td.text
                        else:
                            category = i.td.text.span
                    elif i.th.text == "가격대":
                        if i.th.span == None:
                            price = i.td.text
                        else:
                            price = i.td.text.span
                    elif i.th.text == "주차":
                        if i.th.span == None:
                            parking = i.td.text
                        else:
                            parking = i.td.text.span
                    elif i.th.text == "영업시간":
                        if i.th.span == None:
                            time = i.td.text
                        else:
                            time = i.td.text.span

                postId = soup.select_one('div.restaurant_action_button_wrap > div.wannago_wrap > button')["data-restaurant_uuid"]
                
                temp_store = {
                    "postId" : postId, 
                    "name": name,
                    "address":address.replace('\n', ''),
                    "phone":phone.replace('\n', ''),
                    "category":category.replace('\n', ''),
                    "price":price.replace('\n', ''),
                    "parking":parking.replace('\n', ''),
                    "time":time.replace('\n', '')
                }
                print(temp_store)
                self.storeList.append(temp_store)
                


                res_obj = session.get("https://stage.mangoplate.com/api/v5/restaurants/" + postId + "/reviews.json?language=kor&request_count=100&sort_by=2&start_index=0")
                json_var = json.loads(res_obj.text)
                
                for i in json_var:
                    comment = i["comment"]["comment"].replace('\n', ' ')

                    if comment == '.' or '':
                        continue
                    
                    temp = {
                        "id" : postId,
                        "user" : i["user"]["user_info"]["member_first_name"],
                        "comment" : comment,
                        "gender" : randint(0, 1)
                    }
                    print(temp)
                    self.evaluateList.append(temp)
        
    def getStoreList(self):
        return self.storeList
    
    def getEvaluateList(self):
        return self.evaluateList
                    

