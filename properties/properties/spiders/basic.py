# -*- coding: utf-8 -*-
import scrapy

from properties.items import PropertiesItem


class BasicSpider(scrapy.Spider):
    name = 'basic'
    # allowed_domains = ['gumtree']
    start_urls = ['https://www.magicbricks.com/property-for-sale/residential-real-estate?proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment&cityName=Mumbai']

    def parse(self, response):
        item = PropertiesItem()
        item['title'] = response.xpath(
            '//*[contains(@class, "m-srp-card__title")]/text()')[0].extract()
        # self.log("title: %s" % response.xpath(
        #     '//*[contains(@class, "m-srp-card__title")]/text()').extract()[1])
        item['location'] = response.xpath(
            '//*[contains(@class, "m-srp-card__title")]/text()').extract()
        # self.log("location: %s" % response.xpath(
        #     '//*[contains(@class, "m-srp-card__title")]/text()').extract()[2])
        item['price'] = response.css(
            '.m-srp-card__price').xpath('text()').extract()
        # self.log("price: %s" % response.css(
        #     '.m-srp-card__price').xpath('text()').extract()[0])
        item['carpet_area'] = response.css(
            '.m-srp-card__summary__info').xpath('text()').extract()
        # self.log('carpet area: %s' % response.css(
        #     '.m-srp-card__summary__info').xpath('text()').extract()[0])
        item['status'] = response.css(
            '.m-srp-card__summary__info').xpath('text()').extract()
        # self.log('status: %s' % response.css(
        #     '.m-srp-card__summary__info').xpath('text()').extract()[1])
        item['transaction'] = response.css(
            '.m-srp-card__summary__info').xpath('text()').extract()
        # self.log('transaction: %s' % response.css(
        #     '.m-srp-card__summary__info').xpath('text()').extract()[2])
        item['furnishing'] = response.css(
            '.m-srp-card__summary__info').xpath('text()').extract()
        # self.log('furnishing: %s' % response.css(
        #     '.m-srp-card__summary__info').xpath('text()').extract()[3])
        item['society'] = response.css(
            '.m-srp-card__summary__link').xpath('text()').extract()
        # self.log('society: %s' % response.css(
        #     '.m-srp-card__summary__link').xpath('text()').extract()[0])
        item['description'] = response.css(
            '.m-srp-card__description').xpath('text()').extract()
        # self.log("description: %s" % response.css(
        #     '.m-srp-card__description').xpath('text()').extract()[0])
