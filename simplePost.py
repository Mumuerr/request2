#coding=utf-8
#发送一个 HTTP POST 请求
import requests


payload={"key":"value1","key2":"value2"}

r=requests.post("http://httpbin.org/post",data=payload)

print(r.text)

