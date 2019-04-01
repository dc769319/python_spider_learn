#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    siteDomain = 'https://www.biqukan.com'
    target = 'https://www.biqukan.com/1_1094/'
    # 设置请求头
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}
    req = requests.get(url = target, headers = headers)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    
    mainList = soup.find('div', class_ = 'listmain')
    catalogSoup = BeautifulSoup(str(mainList), 'html.parser')
    tagAList = catalogSoup.find_all('a')
    for tagA in  tagAList:
        print(tagA.string, siteDomain + tagA.get('href'))
