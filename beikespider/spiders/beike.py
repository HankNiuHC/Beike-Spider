# -*- coding: utf-8 -*-
import scrapy
from beikespider.items import BeikespiderItem
import random
import time


class BeikeSpider(scrapy.Spider):
    name = 'beike'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://xa.ke.com/ershoufang/changan4/pg1']
    url = 'https://xa.ke.com/ershoufang/changan4/pg%d'
    page_num = 1

    def parse(self, response):
        li_list = response.xpath('//div[@data-component="list"]/ul//li[@class="clear"]')
        for li in li_list:
            detail_url = li.xpath('./a/@href').extract_first()
            house_name = li.xpath\
                ('./div[@class="info clear"]/div[@class="address"]/div[@class="flood"]/div/a/text()').\
                extract_first()
            house_info = li.xpath('./div[@class="info clear"]/div[@class="address"]/div[@class="houseInfo"]')\
                .extract_first().split('</span>')[-1].replace('</div>','')
            total_price = li.xpath('./div[@class="info clear"]/div[@class="address"]/div[@class="priceInfo"]/div[@cl'
                                   'ass="totalPrice"]/span/text()').extract_first()
            unit_price = li.xpath('./div[@class="info clear"]/div[@class="address"]/div[@class="priceInfo"]/div[@cla'
                                  'ss="unitPrice"]/@data-price').extract_first()
            if len(house_info.split('|')) == 5:
                bulid_level = house_info.split('|')[0].strip()
                build_year = house_info.split('|')[1].strip()[:-2]
                build_size = house_info.split('|')[2].strip()
                build_square = house_info.split('|')[3].strip()[:-2]
                build_oriented = house_info.split('|')[4].strip()
                item = BeikespiderItem()
                item['region'] = '长安'
                item['detail_url'] = detail_url
                item['house_name'] = house_name
                item['total_price'] = total_price
                item['unit_price'] = unit_price
                item['build_level'] = bulid_level
                item['build_year'] = build_year
                item['build_size'] = build_size
                item['build_square'] = build_square
                item['build_oriented'] = build_oriented
                # print(house_name)
                yield item
        if self.page_num < 100:
            self.page_num += 1
            new_url = format(self.url % self.page_num)
            yield scrapy.Request(url=new_url, callback=self.parse)
        time.sleep(random.random())
        print(self.page_num - 1, 'ok')




