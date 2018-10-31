# -*- coding: utf-8 -*-
# @Time    : 2018/10/31 11:48
# @Author  : Alex
# @Site    : 
# @File    : runtest.py
# @Software: PyCharm
# 运用了2种运行测试用例的方法，分别是：
# 1.构造测试集，运用testsuite（）
# 2.运用TestLo类中提供的discover（）方法

import unittest
# 加载测试文件
# from testpro import testadd
# from testpro import testsub


# 利用TestLoader类中提供的discover（）方法
# 定义测试用例的目录为当前目录
test_dir = './'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(discover)

# # 构造测试集
# suite = unittest.TestSuite()
#
# suite.addTest(testadd.TestAdd('test_add'))
#
# suite.addTest(testsub.TestSub('test_sub'))
#
# if __name__ == '__main__':
#     runner = unittest.TextTestRunner()
#     runner.run(suite)
