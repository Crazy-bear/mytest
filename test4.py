# -*- coding: utf-8 -*-
# @Time    : 2018/10/30 17:56
# @Author  : Alex
# @Site    : 
# @File    : test4.py
# @Software: PyCharm


from count import is_prime
import unittest


class Test(unittest.TestCase):
    def setUp(self):
        print('test start')

    def test_case(self):
        self.assertTrue(is_prime(7), '不是质数！')

    def tearDown(self):
        print('test end!')


if __name__ == '__main__':
    unittest.main()
