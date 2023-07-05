# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import re
from itertools import chain
import html
from itemadapter import ItemAdapter
from items import SokaNewsItem

class SokaNewsPipeline:
    def process_item(self, item, spider):
        article_clean = dict()
        article_clean['newspaper'] = item['newspaper']
        article_clean['url'] = item['url']
        article_clean['title'] = item['title']
        article_clean['summary'] = item['summary']
        article_clean['category'] = item['category']
        article_clean['text'] = item['text']
        article_clean['date_publish'] = item['date_publish']
        article_clean['date_scrape'] = item['date_scrape']
        return item
