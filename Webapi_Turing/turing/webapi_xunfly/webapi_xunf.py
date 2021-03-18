#-*- coding: utf-8 -*-
import urllib
import json

class WebapiXunfei(object):
    def __init__(self, api_url='', json_path=''):
        self.api_url = api_url
        self.json_path = json_path
        
    def 