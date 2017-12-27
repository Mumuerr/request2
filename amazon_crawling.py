#coding=utf-8
#亚马逊商品的爬取--通过修改headers字段，模拟浏览器向网站发起请求

import requests

url = "https://www.amazon.cn/gp/product/B01M8L5Z3Y"
try:
    kv = {'user-agent': 'Mozilla/5.0'}
    r = requests.get(url, headers=kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.status_code)
    print(r.text[:1000])
except:
    print("爬取失败")