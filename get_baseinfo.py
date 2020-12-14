#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/5 15:53
# @Author  : WangXi
# @File    : get_baseinfo.py
# @Software: PyCharm


import requests

from js_decode_1 import DecodeEncry

base_url = 'https://api.qimai.cn/app/appinfo?analysis='

synct = 1607154653.090

url = "/app/appinfo"

country = str(input("请输入要分析的国家（如中国就输入：cn）："))

appid = str(input("请输入要分析的软件id 432274380 ："))

params = {
    'country': '{}'.format(country),
    'appid': "{}".format(appid),
}

his = DecodeEncry().get_analysis(synct, url, params) + '&appid={}&country={}'.format(appid, country)

url = base_url + his
print(url)

header = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
    'accept': 'application/json, text/plain, */*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cookie': 'PHPSESSID=j6i6nbmfi7pm0af1hfibeig0td; '
              'qm_check=SxJXQEUSChd+XERcXBRxQllDEH9AVVtwfhB8XlNRXlUSHBJTWFBUWRIDEgQUABwAHAAcABdK; '
              'gr_user_id=0ad7c2d8-c7cf-414c-ae8f-2b542843d223; '
              'ada35577182650f1_gr_session_id=f103a0e5-daa0-4590-a64d-0a8415ab0916; '
              'grwng_uid=75748ee6-e2f4-4f01-867c-e3289ca29b0d; '
              'ada35577182650f1_gr_session_id_f103a0e5-daa0-4590-a64d-0a8415ab0916=true; '
              'USERINFO=v0LNjoU9Mno9ER%2FOZgUutLRbPmBxMG%2FU6WdiNrcsHh4fCeg'
              '%2Fc33sPoB9UmOeXBw0o5Dv6h1H5R6oaFmG9iV7oCBvlS49kXxHIfHgN40yWpgZCmlJYxHVhSTO1KuQSN%2F8'
              '%2FNZRfTFt3KkJeLkToGQ%2BoQ%3D%3D; '
              'ada35577182650f1_gr_last_sent_sid_with_cs1=f103a0e5-daa0-4590-a64d-0a8415ab0916; '
              'ada35577182650f1_gr_last_sent_cs1=qm10678472433; '
              'aso_ucenter=c11dsGDQmHF9iPWZAvZFvdGEQPxeCiiuvNq6WTGjei7xawBeMGEkV11W3vnk7rXNcw; '
              'ada35577182650f1_gr_cs1=qm10678472433; synct={}; syncd=-1803; '
              'tgw_l7_route=1ed618a657fde25bb053596f222bc44a'.format(synct),
    'origin': 'https://www.qimai.cn',
    'refeer': 'https://www.qimai.cn/',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site'
}

respose = requests.get("{}".format(url), headers=header)

js_data = respose.json()

list_data = js_data['appInfo']

# 这里就不写入csv了   因为具体的都有写直接按照list_data['xxxxx']这样的格式就可以了如下并且还有很多的信息没有写完按照list_data后面的写就好了

print(list_data)
print('应用全程:', list_data['appname'])
print('主标题:', list_data['subname'])
print('副标题:', list_data['subtitle'])
print('应用id:', list_data['appid'])
if list_data["is_game"] == 0:
    print('是否为游戏: 否')
    if list_data["is_game"] == 1:
        print('是否为游戏: 是')
print('图标:', list_data['icon'])

