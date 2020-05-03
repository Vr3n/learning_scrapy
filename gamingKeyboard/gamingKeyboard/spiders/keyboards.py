# -*- coding: utf-8 -*-
import scrapy


class KeyboardsSpider(scrapy.Spider):
    name = 'keyboards'
    allowed_domains = ['amazon.in']
    start_urls = ['http://amazon.in/']

    def parse(self, response):
        pass
