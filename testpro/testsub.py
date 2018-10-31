# -*- coding: utf-8 -*-
# @Time    : 2018/10/31 11:48
# @Author  : Alex
# @Site    : 
# @File    : testsub.py
# @Software: PyCharm

from testpro.calculator import Count
from testpro.mytest import MyTest
import unittest


class TestSub(MyTest):
    def test_sub(self):
        j = Count(2, 3)
        self.assertEqual(j.sub(), -1, '计算错误！')


if __name__ == '__main__':
    unittest.main
