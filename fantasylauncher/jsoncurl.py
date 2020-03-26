#!/user/local/bin/python
# -*- coding:utf-8 -*-
import json
import sys

import urllib3
from urllib3.contrib.socks import SOCKSProxyManager


def resolveJson(path):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
    }
    proxy = SOCKSProxyManager('socks5://localhost:1080/', headers=headers)
    response = proxy.request('get', "https://storage.googleapis.com/fantasylauncer/wallpaper/wallpaperOnline.json")
    with open("wallpaperOnline.json", 'wb+') as f:
        f.write(response.data)
        f.close()



if __name__ == '__main__':
    # print '输入参数列表:'
    if len(sys.argv) > 1:
        for index in range(len(sys.argv)):
            if index == 1:
                currentProjectFilePath = sys.argv[index]
    resolveJson(currentProjectFilePath)
