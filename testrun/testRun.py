#! /usr/bin/env python
# -*- coding:utf-8 -*-

import os
from HTMLTestRunner import HTMLTestRunner
from conf import suite

if __name__ == "__main__":
    # 定义测试报告存放文件夹
    fpath = '../report'
    # 判断是否存在此文件夹，不存在则创建
    if not os.path.exists(fpath):
        os.makedirs(fpath)
    else:
        pass

    # 定义测试报告文件名
    filename = fpath + "/htmlreport.html"

    # 要测试的用例
    # suite = interface.testwyy.test_suit.test_suite()
    with open(filename, 'wb') as fp:
        runner = HTMLTestRunner(stream=fp, title="my report")
        runner.run(suite)

    # unittest.main()