#-*- coding: utf-8 -*-
#开发团队: ELSTP Studio
#开发人员: Wolf 
#联系方式: QQ:1465217851 emal:1465217851qq.com
#开发时间: 2019/12/25 14:42
#文件名称: main.py
#开发工具: PyCharm

import os
import sys
import requests
import re
from urllib import request as reqs

def down(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
    }
    req = reqs.Request(url, headers=headers)
    result = reqs.urlopen(req)
    res = result.read()
    os.remove('D:/GET/temp.mp4')
    with open(r'D:\GET\temp.mp4', 'ab') as file:  # 保存到本地的文件名
        file.write(res)
        file.flush()

def get_url(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
    }
    req = requests.get(url=url, headers=headers)
    text = req.text
    url = re.findall(r'playAddr: "(.*?)"', text)
    url = url[0]
    down(url=url)
url = 'https://v.douyin.com/VRsohS/'
t = get_url(url)