#-*- coding: utf-8 -*-
#开发团队: ELSTP Studio
#开发人员: Wolf 
#联系方式: QQ:1465217851 emal:1465217851qq.com
#开发时间: 2019/12/25 14:42
#文件名称: main.py
#开发工具: PyCharm
import os, sys
import request
from urllib import request as reqs


def down(url):
    http_str = url
    url = http_str + '/machine_info'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
    }
    req = reqs.Request(url, headers=headers)
    result = reqs.urlopen(req)
    res = result.read()
    with open(r'F:\GET\temp.mp4', 'ab') as file:  # 保存到本地的文件名
        file.write(res)
        file.flush()

def get_url(url):
    page = reqs.urlopen(url=url)
    text = page.read()
    print(text)