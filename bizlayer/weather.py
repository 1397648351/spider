# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ==================================================
# @Time   : 2019/4/10 11:25
# @Author : WuZe
# @Desc   : 
# ==================================================

from common.spider import Spider
from pyquery import PyQuery as pq


class Weather:
    def __init__(self):
        self.url = 'http://localhost'

    def get_html(self):
        html = Spider.get_content(self.url).decode('utf-8', 'ignore')
        with open('file/weather.html', mode='w', encoding='utf-8') as f:
            f.write(html)
        doc = pq(html)

    def run(self):
        pass
