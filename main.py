# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ==================================================
# @Time   : 2019/4/8 18:35
# @Author : WuZe
# @Desc   :
# ==================================================

from common.dataHelper import DataHelper

if __name__ == "__main__":
    db = DataHelper()
    rows = db.callproc('InitServer', (1,))
    print(rows)
    # print(DataHelper.instance().)
    # DataHelper.instance()
