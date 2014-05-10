from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
import random
import time

class Preferences:
    total_searches = 1000 # so script won't run forever if you forget about it
    click_on_results = True # set to false if you don't want to follow links
    max_delay_time = 10 # in seconds

def setup_browser():
    firefox_profile = FirefoxProfile()
    # Reduce bandwidth consumption and increase speed by disabling images, Flash
    firefox_profile.set_preference('permissions.default.image', 2)
    firefox_profile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so',
                                  'false')
    return webdriver.Firefox(firefox_profile)

def perform_search(driver, search_terms, options):
    search_box = driver.find_element_by_id("gbqfq")
    search_box.clear()
    search_box.send_keys(search_terms)
    search_box.send_keys(Keys.RETURN)
    random_delay(options)

def randomly_perform_action():
    return random.randrange(2)

def random_delay(options):
    current_delay = random.randrange(1, options.max_delay_time + 1)
    time.sleep(current_delay)

def press_back(driver, options):
    if randomly_perform_action() == True:
        driver.back()
    else:
        go_to_google_main_page(driver)
    random_delay(options)

def go_to_google_main_page(driver):
    driver.get("https://www.google.com/")

def click_on_result(driver, options):
    if randomly_perform_action() == True and options.click_on_results == True:
            result_number = str(1)
        selector = "li.g:nth-child("+ result_number + ") > div:nth-child(1) >" \
            " h3:nth-child(1) > a:nth-child(1)"
        result = driver.find_element_by_css_selector(selector)
        result.click()
        random_delay(options)
        press_back(driver, options)
    else:
            random_delay(options)

def main():
    options = Preferences()
    driver = setup_browser()
    i = 0
    go_to_google_main_page(driver)

    while(i < options.total_searches):
        search_terms = str(i)
        perform_search(driver, search_terms, options)
        click_on_result(driver, options)
        i+=1

if __name__ == "__main__":
    main()
