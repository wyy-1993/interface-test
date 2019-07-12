#! /usr/bin/env python
# -*- coding:utf-8 -*-

# 维护测试用例

import unittest
from normal.method_wyy import choose_wyy
from normal.read_data import read_file
from ddt import data, ddt
from conf import filepath, num

# 通过read_file方法，读取测试数据，存储在test中
test = read_file(filepath, num)


# ddt数据驱动
@ddt
class Testrun(unittest.TestCase):

    # data(*testwyy) 数据驱动，将test中的数据依次传入，达到一条用例执行多条数据的目的
    @data(*test)
    def test_interface(self, testdata):
        url = testdata[3]
        headers = testdata[4]
        data = testdata[5]
        method = testdata[6]
        # ass_content = testdata[7]
        ass_code = testdata[8]
        # 调用choose_wyy方法，获取测试结果
        res = choose_wyy(method, url, headers, data)
        # 预期结果和测试结果进行对比，判断运行结果是否正确
        self.assertEqual(ass_code, res.status_code)


