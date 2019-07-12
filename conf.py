#! /usr/bin/env python
# -*- coding:utf-8 -*-

"""配置文件"""



"""测试数据的文件路径"""

filepath = "../test.xlsx"

"""测试数据在excel文件中的sheet数--！！！注意 从0开始！！！--此处代表第2个sheet页"""
num = 1

"""定义测试套件，可以修改test_suit文件，定义多个测试套件，测试时跟据需要选择对应的套件"""

import test_suite.tsuite
suite = test_suite.tsuite.test_suite1()