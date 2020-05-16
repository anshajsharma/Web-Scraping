# -*- coding: utf-8 -*-
import scrapy


class SpecialOffersSpider(scrapy.Spider):
    name = 'special_offers'
    allowed_domains = ['www.tinydeal.com']
    # start_urls = ['https://www.tinydeal.com/specials.html']

    def start_requests(self):
        yield scrapy.Request(url='https://www.tinydeal.com/specials.html',callback=self.parse,headers={
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
        })

    def parse(self, response):
       products = response.xpath('//ul[@class="productlisting-ul"]/div/li')
       
       for product in products:
           product_name = product.xpath('.//a[2]/text()').get()
           product_url = response.urljoin( product.xpath('.//a[2]/@href').get())
           actual_price = product.xpath('.//div[@class="p_box_price"]/span[2]/text()').get()
           discount_price = product.xpath('.//div[@class="p_box_price"]/span[1]/text()').get()
           
           yield {
               'product_name':product_name,
               'product_url':product_url,
               'actual_price':actual_price,
               'discount_price':discount_price,
               'User-Agent':response.request.headers['User-Agent']
           }
       next_page = response.xpath('//a[@class="nextPage"]/@href').get()

       if(next_page):
            yield scrapy.Request(url=next_page,callback=self.parse,headers={
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'})