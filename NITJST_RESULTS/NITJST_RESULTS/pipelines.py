# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import logging

class NitjstResultsPipeline(object):
    
    @classmethod
    def from_crawler(cls,crawler):
        logging.warning(crawler.settings.get("MONGO_URI"))

    def open_spider(self,spider):
        logging.warning("SPIDER OPENED IN PIPELINES")
    
    def close_spider(self,spider):
        logging.warning("SPIDER CLOSED IN PIPELINES")
    
    def process_item(self, item, spider):
        return item
