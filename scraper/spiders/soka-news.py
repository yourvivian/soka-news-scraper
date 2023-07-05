import scrapy
from scrapy import Request
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from datetime import datetime

class NewsSpider(CrawlSpider):
    name = "soka-news"
    allowed_domains = ['soka.edu']
    start_urls = ["https://www.soka.edu/news-events/news"]

    rules = (
        # Match URLs for topics
        Rule(LinkExtractor(allow='\/news\?'), follow = True), # no callback argument
        # Match URLs for article
        Rule(LinkExtractor(allow='\/news\/',), 
                           callback='parse_article', follow = True),)
        #Rule(LinkExtractor(allow='https:\/\/www\.soka\.edu\/news-events\/news\/[a-z0-9-]+',), 
        #                   callback='parse_article', follow = True),)
#deny = '\\?pg=[0-9]+')
    def parse_article(self, response):
        article = dict()
        article['newspaper'] = "soka-news"
        article['url'] = response.url
        article['title'] = response.css('h1.news__title::text').get(default='').strip() # 
        article['text'] = " ".join([ele.strip() for ele in response.css('.news__body p ::text').getall() if ele.strip()])
        #article['text'] = response.css('meta[name="description"]::attr(content)').get(default='').replace('\n', '').replace('\t', '').strip()
        article['categories'] = response.css('.tags__list.news__tags-list li.tags__tag a::text').getall()
        article['date_publish'] = response.css('.news__pub-date::text').get(default='').strip()
        article['date_scrape'] = datetime.now().strftime("%Y-%m-%d %H:%M")

        return article