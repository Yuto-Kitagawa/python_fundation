import requests

url  = "http://yutons.com"
data = "HelloWorld"
res = requests.post(url=url,data=data)
print(res)