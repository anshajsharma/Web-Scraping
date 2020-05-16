# -*- coding: utf-8 -*-
import scrapy
from scrapy_selenium import SeleniumRequest
from scrapy.selector import Selector
from selenium import webdriver
import time
import os
import urllib.request
from selenium.webdriver.common.keys import Keys

class AllResultsSpider(scrapy.Spider):
    name = 'all_results'
    # allowed_domains = ['nilekrator.pythonanywhere.com']
    # start_urls = ['https://nilekrator.pythonanywhere.com']

    def start_requests(self):
        yield SeleniumRequest(
            url='https://nilekrator.pythonanywhere.com',
            wait_time=3,
            # screenshot=True,
            callback=self.parse
        )

    def parse(self, response):

        keys = [ 
            '2018ugpi089','2015ugcs089'
          ]
        # driver = response.meta['driver']
        
        for key in keys:
            driver = response.meta['driver']
            driver.get("https://nilekrator.pythonanywhere.com")
            year = key[:4]
            if "cs".upper() in key.upper():
                branch = "CSE"
            else:
                branch = "Other"
            filename = key + '.png'
            screen_shotLocation = f"G:/Web Scrapping/NITJST_RESULTS/ScreenShots/{year}/{branch}/{filename}"
            StudentImagesLocation = f"G:/Web Scrapping/NITJST_RESULTS/StudentsImages/{year}/{branch}/{filename}"
            isExist = os.path.exists(f"G:/Web Scrapping/NITJST_RESULTS/ScreenShots/{year}/{branch}")
            if(isExist):
                pass
            else:
                os.makedirs(f"G:/Web Scrapping/NITJST_RESULTS/ScreenShots/{year}/{branch}") 

            isExist = os.path.exists(f"G:/Web Scrapping/NITJST_RESULTS/StudentsImages/{year}/{branch}")
            if(isExist):
                pass
            else:
                os.makedirs(f"G:/Web Scrapping/NITJST_RESULTS/StudentsImages/{year}/{branch}")  
            # height = driver.execute_script("return document.body.scrollHeight")
            # time.sleep(5)
            inp = driver.find_element_by_xpath("//input")
            inp.click()
            inp.send_keys(key)
            inp.send_keys(Keys.ENTER)
            time.sleep(3)

            html = driver.page_source


            response_obj = Selector(text=html) # //div[@class="ui column"]/pre
            imageUrl = response.urljoin(response_obj.xpath('//div[@class="column"]/img/@src').get())
            print(imageUrl)
            name = response_obj.xpath('//div[@class="ui column"]/pre[1]/text()').get()
            rollno = response_obj.xpath('//div[@class="ui column"]/pre[2]/text()').get()
            branch = response_obj.xpath('//div[@class="ui column"]/pre[3]/text()').get()
            # imageUrl = response_obj.xpath('//div[@class="column"]/img/@src/text()').get()
            # imageUrl = response_obj.xpath('//div[@class="column"]/img/@src/text()').get()
            
            if(name):
                # //div[@class="ui attached orange message"][position()>1]   -- single semester
                sem_headings = response_obj.xpath('//div[@class="ui attached orange message"][position()>1]')
                marks_container = response_obj.xpath('//div[@class="ui attached segment"][position()>1]')
                b = marks_container.__len__()  
                rank = response_obj.xpath('//div[@class="ui column"]/pre[4]/text()').get() + response_obj.xpath('//div[@class="ui column"]/pre[4]/span/text()').get()
                headings = []
                exam_result_release_dates = response_obj.xpath('//div[@class="ui attached orange message"][position()>1]/h4/span/text()').getall()
               
                driver.set_window_size(1400,390 + 490*b)
                driver.save_screenshot(screen_shotLocation)
                # driver.get_screenshot_as_file(key +".png")

                # TO CAPTURE WHOLE BODY TAG
                # S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
                # driver.set_window_size(S('Width'),S('Height')) # May need manual adjustment                                                                                                                
                # driver.find_element_by_tag_name('body').screenshot(screen_shotLocation)
                
                for curr_heading_container in sem_headings:
                    headings.append(curr_heading_container.xpath("normalize-space(.//h4/text())").get())
                    
                c=0
                data = {}
                for curr_marks_container in marks_container:
                    # print('curr_marks_container')
                    # print(curr_marks_container) #//div[@class="ui attached segment"][position()>1]/table[1]/tbody/tr[3]/td[1]
                    SGPA = curr_marks_container.xpath(".//table[1]/tbody/tr[3]/td[1]/text()").get()
                    CGPA = curr_marks_container.xpath(".//table[1]/tbody/tr[3]/td[2]/text()").get()
                    STATUS = curr_marks_container.xpath(".//table[1]/tbody/tr[3]/td[3]/span/text()").get()
                    result = {}
                    SEMESTER = headings[c]

                    #/table[2]/tbody/tr[1]/th

                    result_headings = curr_marks_container.xpath(".//table[2]/tbody/tr/th/text()").getall()

                    rows = curr_marks_container.xpath(".//table[2]/tbody[2]/tr")   #/table[2]/tbody/tr

                    for row in rows:
                        row_data = row.xpath(".//td/text()").getall()
                        single_subject = {}
                        for i in range(9):
                            single_subject[result_headings[i]] = row_data[i]
                        result[row_data[0]] = single_subject

                    result_date = exam_result_release_dates[c]
                    data[SEMESTER] = (  {
                        "SGPA" : SGPA,
                        'CGPA' : CGPA,
                        "STATUS" : STATUS,
                        'SEMESTER' : SEMESTER,
                        'result_date' : result_date,
                        'result': result,
                    } ) 
                    c= c+1
                driver.get(imageUrl)
                time.sleep(1)
                # get the image source
                img = driver.find_element_by_xpath('//img')
                if(img):
                    src = img.get_attribute('src')
                    # download the image
                    urllib.request.urlretrieve(src, StudentImagesLocation)
                
               
                
                yield { key : {
                    'imageUrl': imageUrl,
                    'name': name,
                    'semester_wise_data': data,
                    'rollno': rollno,
                    'branch': branch,
                    'rank': rank
                }
                }
            else:
                driver.set_window_size( 1980 , 1020 )
                driver.save_screenshot(screen_shotLocation)
