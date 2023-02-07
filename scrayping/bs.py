from bs4 import BeautifulSoup
import requests

url = "http://yutons.com/"
if __name__ == "__main__":
    res = requests.get(url=url)
    soup = BeautifulSoup(res.content,'html.parser')
    
    with open("./sample.html",mode="w",encoding='utf-8') as f:
        f.write(str(soup))
    