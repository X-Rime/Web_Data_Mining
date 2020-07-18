import csv
import re
import requests
from lxml import html


def get_html(url):
    # 设置请求头
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
        # 'Cookie':'37cs_user=37cs15499733283; 37cs_pidx=4; cscpvrich5041_fidx=4; 37cs_show=253%2C75%2C76%2C77; UM_distinctid=1735c411607c-061b20363f4599-3962420d-e1000-1735c41160823b; CNZZDATA1260535040=988885086-1594975578-https%253A%252F%252Fblog.csdn.net%252F%7C1594975578'
    }
    # 请求网页链接
    res = requests.get(url=url, headers=headers)
    # 设置编码格式为网页源代码的编码格式
    res.encoding = 'GBK'
    # 返回网页信息
    return res.text
url='https://www.ygdy8.net/html/gndy/dyzz/20200626/60145.html'
htmls = get_html(url)
# get_data(htmls)
print(htmls)