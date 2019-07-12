#! /usr/bin/env python
# -*- coding:utf-8 -*-

# 封装请求方法，直接进行请求，传入 方法、路径、请求头、请求数据

import requests
import json

def choose_wyy(method, url, headers, data):
    if method.upper() == "POST":
        data = json.dumps(data)
        res = requests.post(url, headers, data)

    elif method.upper() == "GET":
        # data = json.dumps(data)
        res = requests.get(url, headers)

    elif method.upper() == "PUT":
        data = json.dumps(data)
        res = requests.put(url, headers, data)

    elif method.upper() == "DELETE":
        data = json.dumps(data)
        res = requests.delete(url, headers, data)

    else:
        print("暂不支持此请求方式")


    return res


def assert_wyy(ass_content,ass_code,res):
    res_content = res.text
    res_code = res.status_code
    if ass_code == res_code:
        print("状态码信息正确：实际返回状态码为%s" % res_code, "与预期状态码%s 一致" % ass_code)
        if ass_content in res_content:
            print("-----True-----")
            print("断言信息正确:实际返回信息为%s，与预期信息 %s 一致", (res_content, ass_content))
            return 0


        else:
            print("-----False-----")
            print("断言信息不正确:实际返回信息为%s，与预期信息 %s 不一致", (res_content, ass_content))
            return 1

    else:
        print("-----False-----")
        print("状态码信息不正确：实际返回状态码为%s" %res_code, "与预期状态码%s 不符" %ass_code)
        return 1




