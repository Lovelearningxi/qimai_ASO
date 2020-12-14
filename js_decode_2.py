import requests
from js_decode_1 import DecodeEncry
import pandas as pd
from test import get_id
import csv
from string import digits
import re
from bs4 import BeautifulSoup as bs


def indexshow(a,country,printnub):
    base_url = 'https://api.qimai.cn/app/keywordDetail?analysis='
    synct = 1606910808.015  # 从服务器返回的set-cookie获取
    url = "/app/keywordDetail"
    s1 = get_id().get_id(a)
    appid = s1
    params = {
        'country': '{}'.format(country),
        "version": 'ios12',
        'appid': "{}".format(appid),
    }
    his = DecodeEncry().get_analysis(synct, url, params) + '&country={}&appid={}&version=ios12'.format(country,appid)
    if a == 'qq':
        his = 'diBlBi5kfQB%2BWmkCYVYCSAYHexl9Vw0NcBMfWRRHFw9RTxZfQlR0VURRUQh3G10GBVEDBAgJAQIGeEcG&country=cn&appid=444934666&version=ios12'
    url = base_url + his
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
    #获取数据
    respose = requests.get("{}".format(url), headers=header)
    js_data = respose.json()
    list_data = js_data['data']

    #app指数显示
    flag = 0
    count = 0
    file_obj = open('doc/showdata.txt', 'w', encoding="gbk")
    file_obj1 = open('doc/countdata.txt', 'w', encoding="gbk")
    show = []
    count = []
    for i in list_data:
        show.append([i['1'],i['5']])
        count.append(i['1'])
        flag += 1
        if flag == printnub:
            break
    name = str(show)
    hint = str(count)
    file_obj.write(name)
    file_obj1.write(hint)
    file_obj.close()
    file_obj1.close()
    index = show
    return index 


#高频字分析
def opentext():
    result = open("doc/countdata.txt").read()
    counts = {}
    for i in result:
        m = i.replace(",","")
        m = i.replace("'","")
        removed = str.maketrans("","",digits)
        res = m.translate(removed)
        for word in res:
            counts[word] = counts.get(word,0) + 1
            if word == "\n":
                counts.pop("\n")
            if word == ",":
                counts.pop(",")
            if word == " ":
                counts.pop(" ")
            if word == "[":
                counts.pop("[")
            if word == "]":
                counts.pop("]")
    items = list(counts.items())
    items.sort(key=lambda x: x[1], reverse=True)
    return items






