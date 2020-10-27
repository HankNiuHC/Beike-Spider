# -*- coding: utf-8 -*-
from scrapy.exporters import CsvItemExporter
# # Define your item pipelines here
# #
# # Don't forget to add your pipeline to the ITEM_PIPELINES setting
# # See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#
#
class BeikespiderPipeline(object):

    def open_spider(self, spider):
        self.file = open('beike.csv', 'wb')
        self.exporter = CsvItemExporter(self.file, fields_to_export=["region", "detail_url", "house_name",
                                                                     "total_price", "unit_price", "build_level",
                                                                     "build_year", "build_size", "build_square",
                                                                     "build_oriented"])

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

# import pymssql
#
# class BeikespiderPipeline(object):
#     def __init__(self):
#         self.conn = pymssql.connect(host='192.168.1.88', user='sa', password='pass@word1', database='Property data')
#         self.cursor = self.conn.cursor()
#         print('连接ok')
#
#     def process_item(self, item, spider):
#         try:
#             # sql = 'INSERT INTO dbo.beike ( region, detail_url, house_name, total_price, unit_price, build_level, build
#             # _year, build_size, build_square, build_oriented ) VALUES ( N%s, %s, N%s, %s,  %s, N%s, %s, N%s, %s, N%s)'
#
#             self.cursor.execute(
#                 "INSERT INTO dbo.beike (region,detail_url,house_name,total_price,unit_price,build_level,build_year,build_size,build_square,build_oriented) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" ,(item['region'], item['detail_url'], item['house_name'],item['total_price'], item['unit_price'], item['build_level'], item['build_year'], item['build_size'], item['build_square'], item['build_oriented']))
#             self.conn.commit()
#         except Exception as ex:
#             print(ex)
#         return item
#
#     def close_spider(self, spider):
#         self.cursor.close()
#         self.conn.close()
