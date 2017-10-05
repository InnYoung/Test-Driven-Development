# !/usr/bin/env python
# -*- coding:utf-8 -*-

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        # self.browser.quit()
        pass

    # 必须以test_开头
    # def test_get_url_with_to_do_list(self):
    #     self.browser.get('http://localhost:8000')
    #     self.assertIn('To-Do', self.browser.title)
    #     self.fail('Finish the test!')

    def test_can_start_a_list_and_retrieve_it_later(self):
        # 打开目标页面
        self.browser.get('http://localhost:8000')

        # 检查页面是否正确
        self.assertIn('To-Do', self.browser.title)
        head_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', head_text)

        # 页面提示输入待办事项
        input_box = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(input_box.get_attribute('placeholder'), 'Enter a to-do item')

        # 输入待办事项，回车确认
        input_box.send_keys('By peacock feathers')
        input_box.send_keys(Keys.ENTER)

        # 刷新显示已输入事项
        sleep(3)
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        for row in rows:
            print('row ' + row)
        self.assertTrue(
            any(row.text == '1: By peacock feathers' for row.text in rows)
        )

        # 页面显示新的待办事项输入框
        print('finish the test!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
