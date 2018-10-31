# -*- coding: utf-8 -*-
# @Time    : 2018/10/31 15:22
# @Author  : Alex
# @Site    : 
# @File    : runtest.py
# @Software: PyCharm

import unittest

# 利用TestLoader类中提供的discover（）方法
# 定义测试用例的目录为当前目录
test_dir = './test_case'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(discover)
