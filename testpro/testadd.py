# -*- coding: utf-8 -*-
# @Time    : 2018/10/31 11:48
# @Author  : Alex
# @Site    : 
# @File    : testadd.py
# @Software: PyCharm
# add的测试用例


from testpro.calculator import Count
from testpro.mytest import MyTest
import unittest


class TestAdd(MyTest):
    def test_add(self):
        j = Count(2, 3)
        self.assertEqual(j.add(), 5, '计算错误！')


if __name__ == '__main__':
    unittest.main
