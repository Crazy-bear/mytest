# -*- coding: utf-8 -*-
# @Time    : 2018/10/31 14:16
# @Author  : Alex
# @Site    : 
# @File    : mytest.py
# @Software: PyCharm

import unittest


class MyTest(unittest.TestCase):
    def setUp(self):
        print('test start')

    def tearDown(self):
        print('test end')
