# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ConifersItem(scrapy.Item):
    common_name = scrapy.Field()
    latin_name = scrapy.Field()
    height = scrapy.Field()
