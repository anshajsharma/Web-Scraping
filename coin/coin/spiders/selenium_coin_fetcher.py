# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import shutil


class SeleniumCoinFetcherSpider(scrapy.Spider):
    name = 'selenium_coin_fetcher'
    allowed_domains = ['www.livecoin.net/en']
    start_urls = ['https://www.livecoin.net/en']

    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless") 
        driver = webdriver.Chrome('G:/Web Scrapping/coin/coin/spiders/chromedriver.exe')
        driver.get("https://www.livecoin.net/en")

        rur_tab = driver.find_elements_by_class_name("filterPanelItem___2z5Gb")
        rur_tab[4].click()
        self.html = driver.page_source
        driver.close()

    def parse(self, response):
        resp = Selector(text=self.html)
        for currency in resp.xpath("//div[contains(@class, 'ReactVirtualized__Table__row tableRow___3EtiS ')]"):
            yield {
                'currency pair': currency.xpath(".//div[1]/div/text()").get(),
                'volume(24h)': currency.xpath(".//div[2]/span/text()").get()
            }

# # -*- coding: utf-8 -*-
# import scrapy
# from scrapy.selector import Selector
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from shutil import which



# class CoinSpiderSelenium(scrapy.Spider):
#     name = 'selenium_coin_fetcher'
#     allowed_domains = ['www.livecoin.net/en'] 
#     start_urls = [
#         'https://www.livecoin.net/en'
#     ]

#     def __init__( self ):
#         chrome_options = Options()
#         chrome_options.add_argument("--headless")

#         # chrome_path = which("chromedriver")


#         driver = webdriver.Chrome('G:/Web Scrapping/coin/coin/spiders/chromedriver.exe')
#         # driver.set_window_size(1920, 1080)
#         driver.get("https://www.livecoin.net/en")

#         rur_tab = driver.find_elements_by_class_name("filterPanelItem___2z5Gb")
#         rur_tab[4].click()

#         self.html = driver.page_source
#         driver.close()

#     def parse(self, response):
#         resp = Selector(text=self.html)
#         for currency in resp.xpath("//div[contains(@class, 'ReactVirtualized__Table__row tableRow___3EtiS ')]"):
#             yield {
#                 'currency pair': currency.xpath(".//div[1]/div/text()").get(),
#                 'volume(24h)': currency.xpath(".//div[2]/span/text()").get()
#             }
#         pass


        
