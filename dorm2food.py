from bs4 import BeautifulSoup
import requests
import json

class Dorm2Food:
    def __init__(self):
        with requests.Session() as session:
            request_data = {'locgbn': 'K1', 'sch_date': '', 'fo_gbn': 'stu'}
            res = session.post('https://dorm2.khu.ac.kr/dorm2/food/getWeeklyMenu.kmc', request_data)
            self.res_json = json.loads(res.text)['root'][0]
            if len(self.res_json['WEEKLYMENU']) == 0:
                self.check = False
            else:
                self.check = True
            

    def getTodayMenu(self):
        if self.check == False:
            return {}

        weeklymenu = self.res_json['WEEKLYMENU'][0]
        today = weeklymenu['today']

        dict_var = {}

        for i in range(1,8):
            si = str(i)

            if weeklymenu['fo_date'+si] == today:
                dict_var['lun_main'] = weeklymenu['fo_menu_lun'+si]
                dict_var['eve_main'] = weeklymenu['fo_menu_eve'+si]

                if i >= 1 and i <= 5:
                    dict_var['mor_main'] = weeklymenu['fo_menu_mor'+si]
                    dict_var['mor_sub'] = weeklymenu['fo_sub_mor'+si]
                    dict_var['lun_sub'] = weeklymenu['fo_sub_run'+si]
                    dict_var['eve_sub'] = weeklymenu['fo_sub_eve'+si]
                    dict_var['special'] = weeklymenu['fo_sub_menu'+si]
                
                break

        return dict_var

    def getSpecialMenu(self):
        if self.check == False:
            return {}

        dict_var = {}
        dict_var['special'] = self.res_json['WEEKLYMENU'][0]['fo_sub_menu1']
        return dict_var

    def getDayMenu(self, num):
        if self.check == False:
            return {}
        
        if num < 1 or num > 7:
            return {}

        weeklymenu = self.res_json['WEEKLYMENU'][0]

        dict_var = {}
        si = str(num)

        dict_var['lun_main'] = weeklymenu['fo_menu_lun'+si]
        dict_var['eve_main'] = weeklymenu['fo_menu_eve'+si]

        if num >= 1 and num <= 5:
            dict_var['mor_main'] = weeklymenu['fo_menu_mor'+si]
            dict_var['mor_sub'] = weeklymenu['fo_sub_mor'+si]
            dict_var['lun_sub'] = weeklymenu['fo_sub_lun'+si]
            dict_var['eve_sub'] = weeklymenu['fo_sub_eve'+si]
            dict_var['special'] = weeklymenu['fo_sub_menu'+si]

        return dict_var

    def getNextDayMenu(self):
        if self.check == False:
            return {}

        weeklymenu = self.res_json['WEEKLYMENU'][0]
        today = weeklymenu['today']

        dict_var = {}

        for i in range(1,8):
            si = str(i)

            if weeklymenu['fo_date'+si] == today:
                if i == 7:
                    return {}
                
                si = str(i+1)

                dict_var['lun_main'] = weeklymenu['fo_menu_lun'+si]
                dict_var['eve_main'] = weeklymenu['fo_menu_eve'+si]

                if i >= 0 and i <= 4:
                    dict_var['mor_main'] = weeklymenu['fo_menu_mor'+si]
                    dict_var['mor_sub'] = weeklymenu['fo_sub_mor'+si]
                    dict_var['lun_sub'] = weeklymenu['fo_sub_run'+si]
                    dict_var['eve_sub'] = weeklymenu['fo_sub_eve'+si]
                    dict_var['special'] = weeklymenu['fo_sub_menu'+si]
                
                break

        return dict_var

