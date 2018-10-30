# -*- coding: utf-8 -*-
# @Time    : 2018/10/30 16:04
# @Author  : Alex
# @Site    : 
# @File    : test.py
# @Software: PyCharm
# 学习unittest测试框架1

from mytest.calculator import Count
import unittest


class TestCount(unittest.TestCase):
    def setUp(self):
        print('test start')     # setup()方法用来初始化工作

    def test_add(self):
        j = Count(2, 3)
        self.assertEqual(j.add(), 5, '计算错误！')       # assertEqual()方法用来做断言，判断值是否相等

    def tearDown(self):
        print('test end')       # tearDown()方法用来处理用例执行后的善后工作，如：释放资源等


if __name__ == '__main__':      # main()方法是unittest提供的全局的方法，使测试模块可以直接运行
    unittest.main()
