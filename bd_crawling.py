# coding=utf-8
# 百度/360搜索关键词提交--修改params参数提交关键词
# 百度的关键词接口：http://www.baidu.com/s?wd=keyword
# 360的关键词接口：http://www.so.com/s?q=keyword

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