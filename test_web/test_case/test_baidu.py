# -*- coding: utf-8 -*-
# @Time    : 2018/10/31 15:22
# @Author  : Alex
# @Site    : 
# @File    : test_baidu.py
# @Software: PyCharm
# 测试百度搜索

from selenium import webdriver
import unittest
import time
# from HtmlTestRunner import HTMLTestRunner


class MyTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.base_url = 'http://www.baidu.com'

    def test_baidu(self):
        driver = self.driver
        driver.get(self.base_url + '/')
        driver.find_element_by_id('kw').clear()
        driver.find_element_by_id('kw').send_keys('unittest')
        driver.find_element_by_id('su').click()
        time.sleep(2)
        title = driver.title
        self.assertEqual(title, 'unittest_百度搜索')

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()

