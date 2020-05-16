# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import logging
import pymongo
import sqlite3


class MongoDBPipeline(object):

    collection_name = "top250movies"

    # @classmethod
    # def from_crawler(cls,crawler):
    #     logging.warning(crawler.settings.get("MONGO_URI"))

    def open_spider(self, spider):
        logging.warning("SPIDER OPENED IN PIPELINES")
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.client["IMDB"]     # Here "IMDB" is database name

    def close_spider(self, spider):
        logging.warning("SPIDER CLOSED IN PIPELINES")
        self.client.close()

    def process_item(self, item, spider):
        # Here collection_name is name of collection in database
        self.db[self.collection_name].insert(item)
        return item


class SqlitePipeline(object):
    # @classmethod
    # def from_crawler(cls,crawler):
    #     logging.warning(crawler.settings.get("MONGO_URI"))

    def open_spider(self, spider):
        logging.warning("SPIDER OPENED IN PIPELINES")
        self.connection = sqlite3.connect("imdb.db")
        self.c = self.connection.cursor()
        try:
          self.c.execute(
            '''CREATE TABLE best_movies(
            title TEXT,
            rating TEXT,
            release_year TEXT,
            duration TEXT,
            release_date TEXT,
            movie_url TEXT
          )'''
          )
          self.connection().commit()
        except sqlite3.OperationalError:
            pass

    def close_spider(self, spider):
        logging.warning("SPIDER CLOSED IN PIPELINES")
        self.connection.close()

    def process_item(self, item, spider):
        self.c.execute('''
        INSERT INTO best_movies(
            title,
            rating,
            release_year,
            duration,
            release_date,
            movie_url
            ) 
            VALUES(?,?,?,?,?,?)
        ''', (
            item.get('title'),
            item.get('rating'),
            item.get('release_year'),
            item.get('duration'),
            item.get('release_date'),
            item.get('movie_url')
        ))
        self.connection.commit()
        return item
