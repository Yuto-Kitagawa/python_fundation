"""
pythonで通信するためのプログラム
基本的にgetだけです。
"""

import requests

url = 'http://yutons.com/'
url = "http://daimaru-shinsaibashi.resv.jp/"
res = requests.get(url=url)
print(res) 
#ステータスコード200番なら正常に通信できている
#404などエラーステータスならURLが間違えているか、ページが削除されている可能性がある
#500番代はサーバーエラーなどが多いのでアプリやサイトにエラーが出ている

#########おまけ###########
print(res.history[0].status_code)

#http headerを表示
print(res.headers)

#クッキーを取得
cookie = res.cookies
print(cookie)