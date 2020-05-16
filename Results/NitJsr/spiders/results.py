# -*- coding: utf-8 -*-
import scrapy
import time
from scrapy.selector import Selector
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import shutil


class SeleniumCoinFetcherSpider(scrapy.Spider):
    name = 'results'
    allowed_domains = ['nilekrator.pythonanywhere.com']
    start_urls = ['https://nilekrator.pythonanywhere.com']

    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless") 
        driver = webdriver.Chrome(executable_path='G:/Web Scrapping/coin/coin/spiders/chromedriver.exe',options=chrome_options)
        
        keys = ['2018UGCS001' , '2018UGCS002' , '2018UGCS003' ]
        for key in keys:
            driver.get("https://nilekrator.pythonanywhere.com")
            inp = driver.find_element_by_xpath("//input")
            print("HERRRRRRRRRRRREEEEEEE")
            print(inp)
            inp.click()
            inp.send_keys(key)
            inp.send_keys(Keys.ENTER)
            time.sleep(5)
            driver.save_screenshot(key+".png")
            self.html = driver.page_source
            print(driver.page_source)
            # resp = Selector(text=html)
            # imageUrl = resp.xpath('//div[@class="column"]/img/@src/text()').get()



            # yield {
            #     "rollNo" : key,
            #     # "imageUrl": imageUrl
            # }
            
            # self.html = driver.page_source
        driver.close()

    def parse(self, response):
        resp = Selector(text=self.html)
        imageUrl = resp.xpath('//div[@class="column"]/img/@src/text()').get()

        for currency in resp.xpath("//div[contains(@class, 'ReactVirtualized__Table__row tableRow___3EtiS ')]"):
            yield {
                'currency pair': "vfiuoh",
                'image_url':imageUrl
            }
        # pass