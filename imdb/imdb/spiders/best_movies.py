# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BestMoviesSpider(CrawlSpider):
    name = 'best_movies'
    allowed_domains = ['www.imdb.com']
    start_urls = ['https://www.imdb.com/search/title/?groups=top_250&sort=user_rating']

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//h3[@class='lister-item-header']/a"), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths='//a[@class="lister-page-next next-page"][1]')) #After rule2 rule1 automatically call
    )  # allow , deny , rectrict_xpath() , restrict_css() are also available

    def parse_item(self, response):
        # print(response.url)    # TODO: Url kaise aaya

        yield {
            'title': response.xpath('//div[@class="title_wrapper"]/h1/text()').get(),
            'rating': response.xpath('//span[@itemprop="ratingValue"]/text()').get(),
            'release_year': response.xpath('//span[@id="titleYear"]/a/text()').get(),
            'duration': response.xpath('normalize-space(//div[@class="subtext"]/time/text())').get(),
            'release_date': response.xpath('normalize-space(//a[@title="See more release dates"]/text())').get(),
            'movie_url': response.url,
            # 'user_agent':response.request.headers['User-Agent']
        }
