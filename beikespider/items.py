# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BeikespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    region = scrapy.Field()
    detail_url = scrapy.Field()
    house_name = scrapy.Field()
    total_price = scrapy.Field()
    unit_price = scrapy.Field()
    build_level = scrapy.Field()
    build_year = scrapy.Field()
    build_size = scrapy.Field()
    build_square = scrapy.Field()
    build_oriented = scrapy.Field()
