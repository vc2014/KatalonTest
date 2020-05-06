# -*- coding: utf-8 -*-
"""
Created on Tue May  5 19:15:19 2020

@author: visha
"""
import HtmlTestRunner
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

l = [["foo", "a", "a",], ["bar", "a", "b"], ["lee", "b", "b"]]

class TestSequense(unittest.TestCase):
    @classmethod
    def setUp(self):
        # create a new Firefox session
        self.driver = webdriver.Chrome(r'chromedriver.exe')
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        print(self.driver.title)
        # navigate to the application home page
        self.driver.get("http://www.google.com/")

    def test_search_by_text(self):
        # get the search textbox
        self.search_field = self.driver.find_element_by_name("q")

        # enter search keyword and submit
        self.search_field.send_keys("Selenium WebDriver Interview questions")
        self.search_field.submit()

        #get the list of elements which are displayed after the search
        #currently on result page usingfind_elements_by_class_namemethod

        lists = self.driver.find_elements_by_class_name("r")
        self.assertEqual(11, len(lists))
    
    @classmethod
    def tearDown(self):
        # close the browser window
        self.driver.quit()

def test_generator(a, b):
    def test(self):
        self.assertEqual(a,b)
    return test

if __name__ == '__main__':
    for t in l:
        test_name = 'test_%s' % t[0]
        test = test_generator(t[1], t[2])
        setattr(TestSequense, test_name, test)
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner())