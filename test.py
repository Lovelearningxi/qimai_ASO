#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/5 11:30
# @Author  : WangXi
# @File    : test.py
# @Software: PyChar
#!/usr/bin/python3
# encoding: utf-8
"""
@author: fengyinws
@contact: fengyinws@163.com
@software: fengyinws
@file: decrypt_qm.py
@time: 2020/8/15 10:53
@desc: 七麦js加密算法
"""

import re

import requests
from bs4 import BeautifulSoup as bs


class get_id:
    def get_id(self,a):
        url = 'https://www.chandashi.com/search/index?keyword={}&type=store&country=cn&from=input&data_type=kw'.format(
            a)
        res = requests.get(url)  # 发送请求
        html = res.text
        IDs = []
        soup = bs(html, "html.parser")  # 定义一个BeautifulSoup变量
        css_class = soup.find(attrs={'class': 'app-item'})
        css_class = str(css_class)
        s = re.search('\d{9,10}', css_class).group()
        print(s)
        return s