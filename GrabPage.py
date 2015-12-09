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
from urllib import error

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
            # print(d)
            self.SetInfo(d)
            print(self._info_)
            print(self._info_.get('Content-Encoding'))
            if self._info_.get('Content-Encoding') == 'gzip':
                print('Content_Encoding : gzip')
                buf = StringIO(str(res.read()))
                rf = gzip.GzipFile(fileobj=buf)
                data = rf.read()
            else:
                data = res.read()
            with open(filePath,'w') as wf:
                wf.write(str(data))

    def GetHtml(self,filePath):
        data = None
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        headers = { 'User-Agent' : user_agent }
        req = request.Request(self._url_,headers = headers)
        try:
            resp = request.urlopen(req)
        except error.URLError as e:
            raise "some error"
            print("URLError:",e.errno)
        finally:
            if resp:
                print(resp.info())
                data = resp.read().decode('utf-8')
        with open(filePath,'w',encoding='utf-8') as wf:
                wf.write(data)