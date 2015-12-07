#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'NewTown'

'''
主程序入口
'''
import GrabPage

if __name__ == '__main__':
    gp = GrabPage.GrabPage("http://www.sina.com")
    gp.DownHtml("mySina.html")