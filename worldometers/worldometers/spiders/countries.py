# -*- coding: utf-8 -*-
import scrapy
import logging


class CountriesSpider(scrapy.Spider):
    name = 'countries'
    allowed_domains = ['www.worldometers.info']  # Never add http:// in begining of domains
    start_urls = ['https://www.worldometers.info/world-population/population-by-country/']
    country_name = ''
    def parse(self, response):
        # title = response.xpath("//h1/text()").get()
        countries = response.xpath("//td/a")

        for country in countries:
            name = country.xpath(".//text()").get()# as we are not using xpath in response
                                         # we should use "." in begining
            link = country.xpath(".//@href").get()
            self.country_name = name   # not synced with below callback
            # absolute_url = f"https://www.worldometers.info{link}"

            # absolute_url = response.urljoin(link)

            # yield scrapy.Request(url=absolute_url)
            yield response.follow(url=link,callback=self.parse_country,meta={'country_name':name}) #predefined follow relative path

            # yield {
            # "country_name": name,
            # "country_link": link
            # }


    def parse_country(self, response):
        logging.info(response.url)
        name = response.request.meta['country_name']
        rows = response.xpath('(//table[@class="table table-striped table-bordered table-hover table-condensed table-list"])[1]/tbody/tr')
        for row in rows:
            year = row.xpath(".//td[1]/text()").get()
            population = row.xpath(".//td[2]/strong/text()").get()
            yield {
                'country_name':name,
                'year': year,
                'population': population
            }