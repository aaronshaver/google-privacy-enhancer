from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def setup_browser():
    driver = webdriver.Firefox() # can easily be switched to other browsers, e.g. webdriver.Chrome()
    go_to_google(driver)
    return driver

def perform_search(driver, search_terms):
    search_box = driver.find_element_by_id("gbqfq")
    search_box.clear()
    search_box.send_keys(search_terms)
    search_box.send_keys(Keys.RETURN)

def click_on_result(driver):
	time.sleep(1)
	first_result = driver.find_element_by_css_selector("li.g:nth-child(3) > div:nth-child(1) > h3:nth-child(1) > a:nth-child(1)")
	first_result.click()

def go_to_google(driver):
    driver.get("https://www.google.com/")

def main():
    driver = setup_browser()
    i = 0
    number_of_searches_total = 1000
    while(i < number_of_searches_total): # so the script won't run forever
        go_to_google(driver)
        search_terms = str(i)
        perform_search(driver, search_terms)
        click_on_result(driver)
        i+=1
        time.sleep(5)

if __name__ == "__main__":
    main()
