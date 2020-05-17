import requests
from bs4 import BeautifulSoup
import json
import os
import sys


class Yonhap:
    def __init__(self):
        self.BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self.req = requests.get('https://www.yna.co.kr/safe/news')
        self.req.encoding = None
        self.html = self.req.content
        self.soup = BeautifulSoup(self.html, 'html.parser')
        self.datas = self.soup.select(
            'div.contents > div.content01 > div > ul > li >article > div >h3'
        )

    def crawling(self):
        print("     Start Crawling news data: [Yonhap]...")
        data = {}

        for title in self.datas:
            name = title.find_all('a')[0].text
            url = 'http:' + title.find('a')['href']
            if "(종합)" in name or "[속보]" in name:
                data[name] = url

        with open(os.path.join(self.BASE_DIR, 'news.json'), 'w+', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent='\t')
        print("    Finish Crawling news data: [Yonhap]...")