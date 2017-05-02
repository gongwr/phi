#!/usr/bin/python
# -*- coding: utf-8 -*-
import json, urllib
from urllib import urlencode


# ----------------------------------
# 基金财务数据调用示例代码 － 聚合数据
# 在线接口文档：http://www.juhe.cn/docs/28
# ----------------------------------

def main():
    # 配置您申请的APPKey
    appkey = "2651966ff7c80ad5006c585cd6ec7373"

    # 1.主要财务指标
    request1(appkey, "GET")

    # 2.基金规模
    request2(appkey, "GET")

    # 3.资产配置
    request3(appkey, "GET")


# 主要财务指标
def request1(appkey, m="GET"):
    url = "http://web.juhe.cn:8080/fund/findata/main"
    params = {
        "key": appkey,  # APPKEY值

    }
    params = urlencode(params)
    if m == "GET":
        f = urllib.urlopen("%s?%s" % (url, params))
    else:
        f = urllib.urlopen(url, params)

    content = f.read()
    res = json.loads(content)
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            # 成功请求
            print res["result"]
        else:
            print "%s:%s" % (res["error_code"], res["reason"])
    else:
        print "request api error"


# 基金规模
def request2(appkey, m="GET"):
    url = "http://web.juhe.cn:8080/fund/findata/size"
    params = {
        "key": appkey,  # APPKEY值

    }
    params = urlencode(params)
    if m == "GET":
        f = urllib.urlopen("%s?%s" % (url, params))
    else:
        f = urllib.urlopen(url, params)

    content = f.read()
    res = json.loads(content)
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            # 成功请求
            print res["result"]
        else:
            print "%s:%s" % (res["error_code"], res["reason"])
    else:
        print "request api error"


# 资产配置
def request3(appkey, m="GET"):
    url = "http://web.juhe.cn:8080/fund/findata/config"
    params = {
        "key": appkey,  # APPKEY值

    }
    params = urlencode(params)
    if m == "GET":
        f = urllib.urlopen("%s?%s" % (url, params))
    else:
        f = urllib.urlopen(url, params)

    content = f.read()
    res = json.loads(content)
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            # 成功请求
            print res["result"]
        else:
            print "%s:%s" % (res["error_code"], res["reason"])
    else:
        print "request api error"


if __name__ == '__main__':
    main()