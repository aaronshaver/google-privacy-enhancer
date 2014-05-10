from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
import time

class Preferences:
    total_searches = 1000

def setup_browser():
    firefoxProfile = FirefoxProfile()
    # Disable images
    firefoxProfile.set_preference('permissions.default.image', 2)
    # Disable Flash
    firefoxProfile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so',
                                  'false')
    # Set the modified profile while creating the browser object 
    self.browserHandle = webdriver.Firefox(firefoxProfile)
    driver = webdriver.Firefox()
    return driver

def perform_search(driver, search_terms):
    search_box = driver.find_element_by_id("gbqfq")
    search_box.clear()
    search_box.send_keys(search_terms)
    search_box.send_keys(Keys.RETURN)

def click_on_result(driver):
    time.sleep(1)
    result_number = 1
    selector = "li.g:nth-child("+ result_number + ") > div:nth-child(1) >" \
        " h3:nth-child(1) > a:nth-child(1)"
    result = driver.find_element_by_css_selector(selector)
    result.click()

def go_to_google(driver):
    driver.get("https://www.google.com/")

def main():
    preferences = Preferences()
    driver = setup_browser()
    i = 0
    
    while(i < preferences.total_searches): # so the script won't run forever
        go_to_google(driver)
        search_terms = str(i)
        perform_search(driver, search_terms)
        click_on_result(driver)
        i+=1
        time.sleep(5)

if __name__ == "__main__":
    main()
