# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ==================================================
# @Time   : 2019/4/8 18:35
# @Author : WuZe
# @Desc   :
# ==================================================

from common.dataHelper import DataHelper
import common.excel as excel
from bizlayer.weather import Weather


def export_excel():
    db = DataHelper()
    data = db.fetchall('select id,name,date,score,introduction from bs_movie order by score desc limit 20')
    fields = list()
    if data and len(data) > 0:
        for index, key in enumerate(data[0]):
            fields.append(key)
    excel.write_info(data, 'movies', 'file/movie.xls', fields)
    print(data[len(data) - 1])


if __name__ == "__main__":
    weather = Weather()
    weather.run()
