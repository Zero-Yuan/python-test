# -*- coding: utf-8 -*-
"""
Created on Thu May  9 22:46:44 2019

2.0增加功能：用列表替换元组
3.0增加功能：将月份划分为不同的集合再操作
4.0增加功能：将月份及其对应天数通过字典表示
@author: yuan
"""

from time import gmtime, strftime

strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())

print(strftime)