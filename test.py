# -*- coding: utf-8 -*-
# @Time    : 2018/10/30 16:04
# @Author  : Alex
# @Site    : 
# @File    : test.py
# @Software: PyCharm
# 学习unittest测试框架1
# 由于增加了“减法”，所以在测试用例中相对于的区分“加法”、“减法”的用例

from testpro.calculator import Count
import unittest


# 第三版本，对经常用的“setUp()"、"tearDown"进行封装一个测试用例
class MyTest(unittest.TestCase):
    def setUp(self):
        print('test start!')

    def tearDown(self):
        print('test end!')


class TestAdd(MyTest):
    def test_add(self):
        j = Count(2, 3)
        self.assertEqual(j.add(), 5)


class TestSub(MyTest):
    def test_sub(self):
        j = Count(2, 3)
        self.assertEqual(j.sub(), -1)


if __name__ == '__main__':
    unittest.main()

# 第二版本，“加法”、“减法”用例区分写
# class TestAdd(unittest.TestCase):
#     def setUp(self):
#         print('test start!')
#
#     def test_add(self):
#         j = Count(2, 3)
#         self.assertEqual(j.add(), 5)
#
#     def test_add2(self):
#         j = Count(10, 32)
#         self.assertEqual(j.add(), 42)
#
#     def tearDown(self):
#         print('test end!')
#
#
# “减法”测试用例
# class TestSub(unittest.TestCase):
#     def setUp(self):
#         print('test start!')
#
#     def test_sub(self):
#         j = Count(2, 3)
#         self.assertEqual(j.sub(), -1)
#
#     def test_sub2(self):
#         j = Count(2, 3)
#         self.assertEqual(j.sub(), -1)
#
#     def tearDown(self):
#         print('test end!')
#
#
# if __name__ == '__main__':
#     # 构造测试集
#     suite = unittest.TestSuite()
#     suite.addTest(TestAdd('test_add'))
#     suite.addTest(TestAdd('test_add2'))
#     suite.addTest(TestSub('test_sub'))
#     suite.addTest(TestSub('test_sub2'))
#
#     # 运行测试集合
#     runner = unittest.TextTestRunner()
#     runner.run(suite)


# 第一版本，只有“加法”的用例
# class TestCount(unittest.TestCase):
#     def setUp(self):
#         print('test start')     # setup()方法用来初始化工作
#
#     def test_add(self):
#         j = Count(2, 3)
#         self.assertEqual(j.add(), 5, '计算错误！')       # assertEqual()方法用来做断言，判断值是否相等
#
#     def tearDown(self):
#         print('test end')       # tearDown()方法用来处理用例执行后的善后工作，如：释放资源等
#
#
# if __name__ == '__main__':      # main()方法是unittest提供的全局的方法，使测试模块可以直接运行
#     unittest.main()
