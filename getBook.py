#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import sys
import requests
import time


class DownloadBook(object):

    def __init__(self):
        self.siteDomain = 'https://www.biqukan.com/'
        self.target = 'https://www.biqukan.com/1_1094/'
        self.urlList = []
        self.titleList = []
        self.nums = 0

    def getChapter(self):
        # 设置请求头
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko)"
                          + "Chrome/72.0.3626.121 Safari/537.36"
        }
        req = requests.get(url=self.target, headers=headers)
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        mainList = soup.find('div', class_='listmain')
        catalogSoup = BeautifulSoup(str(mainList), 'html.parser')
        tagAList = catalogSoup.find_all('a')
        self.nums = len(tagAList[15:])
        for tagA in tagAList[15:]:
            self.urlList.append(self.siteDomain + tagA.get('href'))
            self.titleList.append(tagA.string)

    def getContent(self, target):
        # 设置请求头
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko)"
                          + " Chrome/72.0.3626.121 Safari/537.36"
        }
        req = requests.get(url=target, headers=headers)
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        content = soup.find(id='content')
        return content.text.replace('\xa0' * 8, '\n')

    def write2File(self, title, content, filePath):
        with open(filePath, 'a', encoding='utf-8') as fd:
            fd.write(title + '\n')
            fd.writelines(content)
            fd.write('\n\n')


if __name__ == '__main__':
    downloader = DownloadBook()
    downloader.getChapter()
    print('开始下载...')
    for i in range(downloader.nums):
        downloader.write2File(downloader.titleList[i], downloader.getContent(downloader.urlList[i]), 'book.txt')
        sys.stdout.flush()
        sys.stdout.write('已下载%.3f%%\r' % ((i + 1) / downloader.nums * 100))
        time.sleep(0.03)
    print()
    print('下载完成')
