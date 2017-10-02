#!/usr/bin/env python
# -*- coding:utf-8 -*-

from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.close()

    def test_can_start_homepage(self):
        # 打开目标页面
        self.browser.get('http://localhost:8000')
        self.browser.implicitly_wait(3)

        # 通过title验证页面
        self.assertIn('To-Do', self.browser.title)
        print("Finish the test!")

        # 页面包含‘待办事项’输入框

if __name__ == '__main__':
    unittest.main(warnings='ignore')