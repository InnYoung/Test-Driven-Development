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

    def check_row_in_table(self, input_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('td')
        self.assertIn(input_text, [row.text for row in rows],
                      '\n expected:\n %s\n now:\n %s' % (input_text, table.text))
    # 必须以test_开头
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
        sleep(1)
        self.check_row_in_table('1 : By peacock feathers')

        # 继续输入待办事项,并显示
        input_box = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(input_box.get_attribute('placeholder'), 'Enter a to-do item')
        input_box.send_keys('Make a fly')
        input_box.send_keys(Keys.ENTER)
        sleep(1)
        self.check_row_in_table('1 : By peacock feathers')
        self.check_row_in_table('2 : Make a fly')

        # 页面显示新的待办事项输入框
        print('finish the test!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
