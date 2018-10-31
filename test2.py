# -*- coding: utf-8 -*-
# @Time    : 2018/10/30 16:19
# @Author  : Alex
# @Site    : 
# @File    : test2.py
# @Software: PyCharm
# 学习unittest测试框架，增加测试集1

from testpro.calculator import Count
import unittest


class TestCount(unittest.TestCase):

    # setup()方法用来初始化工作
    def setUp(self):
        print('test start')

    # assertEqual()方法用来做断言，判断值是否相等
    def test_add(self):
        j = Count(2, 3)
        self.assertEqual(j.add(), 5, '计算错误！')

    def test_add2(self):
        j = Count(5, 6)
        self.assertEqual(j.add(), 11, '计算错误！')

    # tearDown()方法用来处理用例执行后的善后工作，如：释放资源等
    def tearDown(self):
        print('test end')


# main()方法是unittest提供的全局的方法，使测试模块可以直接运行
if __name__ == '__main__':

    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(TestCount("test_add2"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)
