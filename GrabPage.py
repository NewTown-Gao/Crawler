#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'NewTown'

'''
 获取指定url 的html页面
'''
from urllib import request
from urllib import response
from http.client import HTTPMessage
import gzip
from io import StringIO

class GrabPage(object):
    def __init__(self,url):
        self._url_ = url
        self._info_ = {}

    def SetInfo(self,info):
        self._info_ = info
        # httpM = HTTPMessage()
        # print(httpM.get_content_charset())

    def DownHtml(self,filePath):
        data = None
        with request.urlopen(self._url_) as res:
            d = res.info()
            self.SetInfo(d)
            print(self._info_)
            if self._info_.get('Content-Encoding') == 'gzip':
                print('Content_Encoding : gzip')
                buf = StringIO(str(res.read()))
                rf1 = gzip.GzipFile(fileobj=buf)
                # data = rf1.read()
            with open(filePath,'w') as wf:
                wf.write(str(data))
