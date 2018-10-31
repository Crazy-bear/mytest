# -*- coding: utf-8 -*-
# @Time    : 2018/10/30 17:46
# @Author  : Alex
# @Site    : 
# @File    : count.py
# @Software: PyCharm
# 用于判断质数


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
