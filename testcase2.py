# -*- coding: utf-8 -*-
"""
Created on Tue May  5 19:15:19 2020

@author: visha
"""
import HtmlTestRunner
import unittest

l = [["foo", "a", "a",], ["bar", "a", "b"], ["lee", "b", "b"]]

class TestSequense(unittest.TestCase):
    pass

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