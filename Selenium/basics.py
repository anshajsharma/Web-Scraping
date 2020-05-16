from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
 
chrome_options = Options()
# chrome_options.add_argument("--headless")     #To stop opening chrome

driver = webdriver.Chrome(executable_path="./chromedriver.exe",options=chrome_options)
driver.get("https://duckduckgo.com")


# driver.find_elements_by_class_name()
# driver.find_elements_by_tag_name()
# driver.find_elements_by_xpath()
# driver.find_element_by_css_selector()

search_inp =  driver.find_element_by_id("search_form_input_homepage")
search_inp.send_keys("My User Agent")

# METHOD 1:
search_btn = driver.find_element_by_id("search_button_homepage")
search_btn.click()

# METHOD 2:
# search_inp.send_keys(Keys.ENTER)

print(driver.page_source)

driver.close()

