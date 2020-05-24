# -*- coding: utf-8 -*-
"""
Created on Sun May 10 00:27:32 2020

@author: visha
"""


import HtmlTestRunner
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

l = [["foo", "a", "a",], ["bar", "a", "b"], ["lee", "b", "b"]]

class TestSequense(type):
    testset = { 0: '0', 10: 'a', 61: 'Z', 62: '10', 3844: '100'}
    
    @classmethod
    def __prepare__(mcls, name, bases):
        
      d = dict()
      #d['testme'] = 5
      for b10, b62 in mcls.testset.items():
        fname = "test_base62_value_{}".format(b10)
        d[fname] = mcls.build_test_generator(b10, b62)
      return d

    @classmethod
    def build_test_generator(cls,a, b):
        def test_search_by_text(self):
            # get the search textbox
            self.search_field = self.driver.find_element_by_name("q")
    
            # enter search keyword and submit
            self.search_field.send_keys("Selenium WebDriver Interview questions")
            self.search_field.submit()
    
            #get the list of elements which are displayed after the search
            #currently on result page usingfind_elements_by_class_namemethod
    
            lists = self.driver.find_elements_by_class_name("r")
            self.assertEqual(14, len(lists))
        return test_search_by_text
    
    

def main():
    unittest.main()

class Test_base62(unittest.TestCase, metaclass=TestSequense):
    @classmethod
    def setUp(self):
        # create a new Firefox session
        self.driver = webdriver.Chrome(r'chromedriver.exe')
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        print(self.driver.title)
        # navigate to the application home page
        self.driver.get("http://www.google.com/")

    def test_nothing(self):
        pass
    
    @classmethod
    def tearDown(self):
        # close the browser window
        self.driver.quit()
        

if __name__ == '__main__':
    main()