# -*- coding: utf-8 -*-
# @Time    : 2018/10/30 17:31
# @Author  : Alex
# @Site    : 
# @File    : test3.py
# @Software: PyCharm
# 用户前端输入数据，进行判断是否相等

import unittest


class Test(unittest.TestCase):
    def setUp(self):
        number = input('输入一个数字:')
        self.number = int(number)

    def test_case(self):
        self.assertEqual(self.number, 1, '你输入的数字不是10')

    def teardown(self):
        pass


if __name__ == '__main__':
    unittest.main()
