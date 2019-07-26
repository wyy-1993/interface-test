#! /usr/bin/env python
# -*- coding:utf-8 -*-

# 复制原接口文件的内容，并将接口返回的结果信息保存到文件中

import xlwt
import xlrd
from conf import filepath,newfile,num
from normal.method_wyy import choose_wyy


# 打开文件，定位到对应的sheet
workbook = xlrd.open_workbook(filepath)
sheet = workbook.sheet_by_index(num)

# 新建文件，创建sheet
workbook_new = xlwt.Workbook()
sheet_new = workbook_new.add_sheet('test')


# 按行读取文件
for i in range(0,sheet.nrows):
    row = sheet.row_values(i)
    # print(row)

    # 将数据按照单元格写入
    for j in range(0,len(row)):
        sheet_new.write(i,j,row[j])

for i in range(1,sheet.nrows):
    row = sheet.row_values(i)
    url = row[3]
    headers = {"Content-Type": "application/json"}
    data = row[5].encode("utf-8")
    method = row[6]
    resp = choose_wyy(method, url, headers, data)

    # 判断有多少列
    n = sheet.ncols
    sheet_new.write(i, n, resp.text)



# 保存文件，复制文件的操作已完成
workbook_new.save(newfile)

