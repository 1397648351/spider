# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ==================================================
# @Time   : 2019/4/10 11:25
# @Author : WuZe
# @Desc   : 
# ==================================================
import ast
import json
import re
from common.spider import Spider
from pyquery import PyQuery as pq
import requests


class Weather:
    def __init__(self):
        self.url = 'http://wthrcdn.etouch.cn/weather_mini'

    def get_html(self):
        html = Spider.get_content(self.url).decode('utf-8', 'ignore')
        with open('file/weather.html', mode='w', encoding='utf-8') as f:
            f.write(html)
        doc = pq(html)

    def run(self):
        data = {'city': '南京'}
        res = requests.get('http://wthrcdn.etouch.cn/weather_mini', params=data).json()
        print(json.dumps(res, ensure_ascii=False))
        # res = ast.literal_eval(res)
        data = res.get('data')
        print(data)
        forecast = data.get('forecast')
        r_fl = re.compile(r'<!\[CDATA\[(.*)\]\]>')
        r_wd = re.compile(r'.* (.*)')
        r_date = re.compile(r'(.{1,2}日).*')
        print('城  市：%s' % data.get('city'))
        print('天  气：%s' % forecast[0].get('type'))
        print('温  度：%s' % data.get('wendu'))
        print('风  向：%s' % forecast[0].get('fengxiang'))
        print('风  力：%s' % r_fl.match(forecast[0].get('fengli')).group(1))
        print('最  高：%s' % r_wd.match(forecast[0].get('high')).group(1))
        print('最  低：%s' % r_wd.match(forecast[0].get('low')).group(1))
        print('空  气：%s' % data.get('aqi'))
        print('舒适度：%s' % data.get('ganmao'))
