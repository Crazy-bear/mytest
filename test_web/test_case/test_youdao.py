# -*- coding: utf-8 -*-
# @Time    : 2018/10/31 15:22
# @Author  : Alex
# @Site    : 
# @File    : test_youdao.py
# @Software: PyCharm
# 测试有道搜索
from selenium import webdriver
import unittest
import time


class MyTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.base_url = 'http://www.youdao.com'

    def test_baidu(self):
        driver = self.driver
        driver.get(self.base_url + '/')
        # driver.find_element_by_id('query').clear()
        driver.find_element_by_id('translateContent').clear()
        driver.find_element_by_id('translateContent').send_keys('webdriver')

        # driver.find_element_by_xpath('//*[@id="translateContent"]').send_keys('webdriver')
        driver.find_element_by_id('form').click()
        time.sleep(2)
        title = driver.title
        self.assertEqual(title, '有道首页')

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main
