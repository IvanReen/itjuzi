# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ItjuziItem(scrapy.Item):
    name = scrapy.Field()
    slogan = scrapy.Field()
    info = scrapy.Field()
    home_page = scrapy.Field()
    tag_list = scrapy.Field()

    company_info = scrapy.Field()
    company_fullname = scrapy.Field()
    company_time = scrapy.Field()
    company_size = scrapy.Field()
    company_status = scrapy.Field()

    financing = scrapy.Field()

    team = scrapy.Field()

    product = scrapy.Field()

    company_url = scrapy.Field()

    crawl_time = scrapy.Field()

    crawl_spider = scrapy.Field()