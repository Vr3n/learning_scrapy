# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field


class PropertiesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # Primary fields
    title = Field()
    location = Field()
    price = Field()
    description = Field()
    carpet_area = Field()
    status = Field()
    transaction = Field()
    furnishing = Field()
    society = Field()
    image_urls = Field()

    # calculated Fields
    images = Field()

    # HouseKeeping Fields.
    url = Field()
    project = Field()
    spider = Field()
    server = Field()
    date = Field()
