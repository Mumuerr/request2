#coding=utf-8

import requests

url = "http://www.baidu.com/s"
try:
    kv = {'wd': 'Python'}
    r = requests.get(url, params=kv)
    print(r.request.url)
    r.raise_for_status()
    print(len(r.text))
    print(r.text[500:5000])
except:
    print("爬取失败")