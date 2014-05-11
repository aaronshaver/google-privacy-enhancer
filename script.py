from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
import random
import time

class Preferences:
    click_on_results = True # set to False if you don't want to follow links
    email = "" # leave empty if you don't wish to sign in
    max_delay_time = 10 # in seconds
    password = "" # leave empty if you don't wish to sign in
    total_searches = 1000 # so script won't run forever if you forget about it

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
        driver.find_element_by_xpath("//*[@id='rso']//h3/a").click()
        random_delay(options)
        press_back(driver, options)
    else:
        random_delay(options)

def login_to_google_account(driver, options):
    if options.email != "" and options.password != "":
        driver.find_element_by_id("gb_70").click()
        driver.find_element_by_id("Email").send_keys(options.email)
        driver.find_element_by_id("Passwd").send_keys(options.password)
        driver.find_element_by_id("signIn").click()

def main():
    options = Preferences()
    driver = setup_browser()
    i = 0
    go_to_google_main_page(driver)
    login_to_google_account(driver, options)

    while(i < options.total_searches):
        search_terms = str(i)
        perform_search(driver, search_terms, options)
        click_on_result(driver, options)
        i+=1

if __name__ == "__main__":
    main()
