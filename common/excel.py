# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ==================================================
# @Time   : 2019/4/9 14:46
# @Author : WuZe
# @Desc   : 
# ==================================================

import os
import xlrd
import xlwt
import threading
from xlutils.copy import copy

mutex = threading.RLock()  # 创建锁


def new_excel(sheetname, filepath):
    print('发现写入目标不存在，正在创建文件', filepath)
    book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    book.add_sheet(sheetname, cell_overwrite_ok=True)
    book.save(filepath)
    print('已成功创建文件', filepath)


def repeat_excel(word, sheetname, filepath):
    # print u'正在检测', word, u'是否存在于文件中'
    try:
        workbook = xlrd.open_workbook(filepath)
        sheet = workbook.sheet_by_name(sheetname)
        words = sheet.col_values(0)
        if word in words:
            # print u'在excel中已经存在', word, u'跳过'
            return True
        else:
            # print u'在excel中不存在'
            return False
    except IOError as e:
        if 'No such file' in e.strerror:
            print('匹配重复时未找到该文件', filepath)
            new_excel(filepath)
            return False
    return False


def write_to_excel(contents, sheetname, filepath, titles=None):
    if contents:
        if not os.path.exists(filepath):
            new_excel(sheetname, filepath)
        rb = xlrd.open_workbook(filepath)
        wb = copy(rb)
        try:
            sheet_rb = rb.sheet_by_name(sheetname)
            sheet = wb.get_sheet(sheetname)
            row = sheet_rb.nrows
        except ValueError:
            sheet = wb.add_sheet(sheetname, cell_overwrite_ok=True)
            row = 0
        if titles:
            if row == 0:
                if isinstance(titles, str):
                    titles = titles.split(',')
                if isinstance(titles, list):
                    for col, title in enumerate(titles):
                        if isinstance(title, str):
                            text = title
                        elif isinstance(title, dict):
                            text = title['text']
                        else:
                            raise Exception("[titles]参数类型错误！")
                        sheet.write(row, col, text)
                    row = row + 1
        for data in contents:
            for col, key in enumerate(data):
                sheet.write(row, col, data[key])
            row = row + 1
        wb.save(filepath)


def write_info(contents, sheetname, filepath, titles=None):
    mutex.acquire()
    write_to_excel(contents, sheetname, filepath, titles)
    mutex.release()
