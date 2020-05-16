# -*- coding: utf-8 -*-
import scrapy
from scrapy_selenium import SeleniumRequest
from scrapy.selector import Selector
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


class ExampleSpider(scrapy.Spider):
    name = 'example'

    def start_requests(self):
        yield SeleniumRequest(
            url='https://duckduckgo.com',
            wait_time=3,
            screenshot=True,
            callback=self.parse
        )


    def parse(self, response):
        img = response.meta['screenshot']
        # with open('screenshot.png', 'wb') as f:
        #     f.write(img)
        driver = response.meta['driver']
        driver.set_window_size(1980, 1020)
        search_input = driver.find_element_by_xpath("(//input[contains(@class, 'js-search-input')])[1]")
        search_input.send_keys('Hello World')
        driver.save_screenshot("searched.png")
        search_input.send_keys(Keys.ENTER)
        # time.sleep(5)

        html = driver.page_source
        driver.save_screenshot("results.png")

        response_obj = Selector(text=html)

        links = response_obj.xpath("//div[@class='result__extras__url']/a")
        for link in links:
            yield {
                'URL': link.xpath(".//@href").get()
            }