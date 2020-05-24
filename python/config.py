# -*- coding: utf-8 -*-
"""
Created on Sun May 24 20:24:09 2020

@author: visha
"""

import configparser
"""
config = configparser.ConfigParser()
config['DEFAULT'] = {'ServerAliveInterval': '45',
                      'Compression': 'yes',
                      'CompressionLevel': '9'}
config['bitbucket.org'] = {}
config['bitbucket.org']['User'] = 'hg'
config['topsecret.server.com'] = {}
topsecret = config['topsecret.server.com']
topsecret['Port'] = '50022'     # mutates the parser
topsecret['ForwardX11'] = 'no'  # same here
config['DEFAULT']['ForwardX11'] = 'yes'
with open('Conf/example.ini', 'w') as configfile:
   config.write(configfile)
"""


###########################################################
######Class to create configuration for test case run######
###########################################################

class ConfigManager():
    
    def __init__(self, selection):
        self.config = configparser.ConfigParser()
        self.baseConfigPath = '/Conf/base.ini'
        if selection is None:
            print("no application selected")
        
        self.selectVar = selection
        
    
    def createTestConfig(self):
        self.
    