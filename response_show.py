import requests

url = "http://www.baidu.com/s"
r=requests.get(url)

print "r.status_code:"
print(r.status_code)
print "r.text:"
print(r.text[500:1000])
print "r.encoding:"
print(r.encoding)
print "r.apparent_encoding:"
print(r.apparent_encoding)