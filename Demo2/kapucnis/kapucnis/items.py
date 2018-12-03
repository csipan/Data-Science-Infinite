# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class KapucinusItem(scrapy.Item):
    brewery = scrapy.Field()
    beer_name = scrapy.Field()
    beer_type = scrapy.Field()
    alcohol_vol = scrapy.Field()
    bitterness = scrapy.Field()
    color = scrapy.Field()
    ingredients = scrapy.Field()
    description = scrapy.Field()
