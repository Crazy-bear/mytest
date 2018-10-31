# -*- coding: utf-8 -*-
# @Time    : 2018/10/30 16:08
# @Author  : Alex
# @Site    : 
# @File    : calculator.py
# @Software: PyCharm
# 计算器类1
# 增加“减法”计算


class Count:
    def __init__(self, a, b):
        self.a = int(a)
        self.b = int(b)

    # 计算加法
    def add(self):
        return self.a + self.b

    # 计算减法
    def sub(self):
        return self.a - self.b
