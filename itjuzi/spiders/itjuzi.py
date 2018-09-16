#coding:utf-8

import scrapy
from itjuzi.items import ItjuziItem

from bs4 import BeautifulSoup

class ItjuziSpider(scrapy.Spider):
    name = 'itjuzi'
    allowed_domains = ['itjuzi.com']

    base_url = "https://www.itjuzi.com/company/"
    
    cookies = {
        "platform_id" : "5261fe124e0b793a75a0a0a6b83de3d9",
        "enter acw_tc" : "781bad2515370229218681203e05a6ef315811e5809205ca3e798a640fb32b",
        " _ga" : "GA1.2.999077577.1537022924",
        " _gid" : "GA1.2.283492398.1537022924",
        " gr_user_id" : "10a2bda2-1397-447f-9609-1832cc8801a6",
        " session" : "78ad048d4d1b8d52c32b28f73262eeac1809babb",
        " gr_session_id_eee5a46c52000d401f969f4535bdaa78" : "8ed6ce88-b9a1-49fc-ae37-5eca4971a12e",
        " Hm_lvt_1c587ad486cdb6b962e94fc2002edf89" : "1537022924,1537070542",
        " gr_session_id_eee5a46c52000d401f969f4535bdaa78_8ed6ce88-b9a1-49fc-ae37-5eca4971a12e" : "true",
        " MEIQIA_VISIT_ID" : "1AH5Ahx2TjoqYOmTr24yzGNNWPn",
        " MEIQIA_EXTRA_TRACK_ID" : "1AH5ActR2XfkZjzum0VibvyOetF",
        " _gat" : "1",
        " Hm_lpvt_1c587ad486cdb6b962e94fc2002edf89" : "1537070777",
    }

    headers = {
        "Host" : "www.itjuzi.com",
        "Connection" : "keep - alive",
        "Content - Length" : "58",
        "Cache - Control" : "max - age = 0",
        "Origin" : "https:// www.itjuzi.com",
        "Upgrade - Insecure - Requests" : "1",
        "Content - Type" : "application / x - www - form - urlencoded",
        "User - Agent" : "Mozilla / 5.0(Windows NT 10.0; WOW64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 69.0.3472.3Safari / 537.36",
        "Accept" : "text / html, application / xhtml + xml, application / xml; q = 0.9, image / webp, image / apng, * / *;q = 0.8",
        "Referer" : "https:// www.itjuzi.com / user / login",
        "Accept - Encoding" : "gzip, deflate, br",
        "Accept - Language" : "zh - CN, zh; q = 0.9",
    }

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, headers=self.headers, cookies=self.cookies, callback=self.parse)

    def parse(self, response):
        if response.status == 200:
            # xpath的模糊查询，只要包含任意属性值的字符串，即可全部匹配
            # cpy1 = response.xpath("//*[contains(@class,'infoheadrow-v2')]")[0].xpath("")
            soup = BeautifulSoup(response.body, 'lxml')

            item = ItjuziItem()
            cpy1 = soup.find(class_="infoheadrow-v2")

            if cpy1:
                item['name'] = cpy1.find(class_='seo-important-title').get_text().strip().split('\t')[0]