# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ==================================================
# @Time   : 2019/4/8 18:35
# @Author : WuZe
# @Desc   :
# ==================================================

import sys
from dataHelper.dataHelper import DataHelper

if __name__ == "__main__":
    db = DataHelper()
    rows = db.fetchall('select t.id from bs_menu t')
    for row in rows:
        print(row)
    # print(DataHelper.instance().)
    # DataHelper.instance()
