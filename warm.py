#!/usr/bin/python
# -*- coding: utf-8 -*-
import json, urllib
import requests
from lxml import etree
from io import StringIO

def do_request():
    params = urllib.urlencode({'type': 'lsjz', 'code': 233009, 'page': 1, 'per': 5000})
    init_page = requests.get("http://fund.eastmoney.com/f10/F10DataApi.aspx?%s" % params).text
    parser = etree.HTMLParser()
    html = etree.parse(StringIO(init_page), parser)
    tr_nodes = html.xpath('//tbody/tr')
    for tr in tr_nodes:
        tdc = tr.xpath('td')
        print tdc[0].text,tdc[1].text,tdc[2].text,tdc[3].text,tdc[4].text,tdc[5].text

def main():
    do_request()


if __name__ == '__main__':
    main()
