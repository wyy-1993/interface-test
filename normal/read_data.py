#! /usr/bin/env python
# -*- coding:utf-8 -*-

# 读取数据，从excel表格，读取测试数据，并保存在列表中

import xlrd

def read_file(filepath, num):
    book = xlrd.open_workbook(filepath)  # 打开文件
    sheet2 = book.sheet_by_index(num)  # 操作sheet

    # 获取列表有多少行数据
    num = sheet2.nrows
    # 定义一个空的列表，将表格的数据按行读取，每行的数据也是存在列表中，最后的形式为[[xx,xx,xx],[xx,xx],[xx,xx]]
    data = []
    # 从1开始，表头数据不读取，只读取列表数据内容
    for i in range(1, num):
        line = sheet2.row_values(i)
        data.append(line)

    # 返回列表数据
    return data


# read_file('../testwyy.xlsx')


