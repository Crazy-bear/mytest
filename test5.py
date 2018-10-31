# -*- coding: utf-8 -*-
# @Time    : 2018/10/31 10:52
# @Author  : Alex
# @Site    : 
# @File    : test5.py
# @Software: PyCharm
# 练习断言assertIn的用法,a是否在b中，即b是否包含a

import unittest


class Test5(unittest.TestCase):
    def setUp(self):
        print('test start')

    def test_case(self):
        a = 'hello'
        b = 'hello world'
        self.assertIn(a, b, 'a不在b中！')

    def tearDown(self):
        print('test end')


if __name__ == '__main__':
    unittest.main
