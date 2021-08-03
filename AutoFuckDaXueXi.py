import requests
from urllib import parse
import os

data = {
    "Level1options": os.environ['Level1options'],
    "Level2options": os.environ['Level2options'],
    "Level3options": os.environ['Level3options'],
    "Level4options": os.environ['Level4options'],
    "name": os.environ['name']
}

url = "http://gsqndxx.gsjiahua.com.cn/inserts?" + parse.urlencode(data)

res = requests.post(
    url, headers={"Content-Type": "application/x-www-form-urlencoded"})

print(url)
print(res.text)