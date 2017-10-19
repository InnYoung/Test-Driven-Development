# !/usr/bin/env python
# -*- coding:utf-8 -*-

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import unittest


class NewVisitorTest(StaticLiveServerTestCase):
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
        self.browser.get(self.live_server_url)
        # sleep(3)

        # 检查页面是否正确
        self.assertIn('To-Do', self.browser.title)
        head_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', head_text)

        # 页面提示输入待办事项
        input_box = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(input_box.get_attribute('placeholder'), 'Enter a to-do item')

        # 输入待办事项，回车确认
        input_box.send_keys('Buy peacock feathers')
        input_box.send_keys(Keys.ENTER)
        sleep(2)

        # 转到新url
        user_1_list_url = self.browser.current_url
        self.assertRegex(user_1_list_url, '/lists/.+')

        # 刷新显示已输入事项
        self.check_row_in_table('1 : Buy peacock feathers')

        # 继续输入待办事项,并显示
        input_box = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(input_box.get_attribute('placeholder'), 'Enter a to-do item')
        input_box.send_keys('Make a fly')
        input_box.send_keys(Keys.ENTER)
        sleep(1)
        self.check_row_in_table('1 : Buy peacock feathers')
        self.check_row_in_table('2 : Make a fly')

        # 页面显示新的待办事项输入框

        # 用户2访问网站
        self.browser.quit()
        sleep(2)
        self.browser = webdriver.Firefox()
        self.browser.get(self.live_server_url)

        # 显示初始页面无用户1数据
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('Make a fly', page_text)

        # 用户2创建新清单
        input_box = self.browser.find_element_by_id('id_new_item')
        input_box.send_keys('Buy milk')
        input_box.send_keys(Keys.ENTER)
        sleep(1)

        # 生成新url
        user_2_list_url = self.browser.current_url
        self.assertRegex(user_2_list_url, '/lists/.+')
        self.assertNotEqual(user_1_list_url, user_2_list_url)

        # 再次确认没有用户1的数据
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('Make a fly', page_text)