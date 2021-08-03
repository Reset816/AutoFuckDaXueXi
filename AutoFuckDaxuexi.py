import requests
from urllib import parse

data = {
    "Level1options": "直属高校团委",
    "Level2options": "兰州大学",
    "Level3options": "信息科学与工程学院团委",
    "Level4options": "",
    "name": ""
}

url = "http://gsqndxx.gsjiahua.com.cn/inserts?" + parse.urlencode(data)

res = requests.post(
    url, headers={"Content-Type": "application/x-www-form-urlencoded"})

print(res.text)