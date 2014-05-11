from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
import random
import time

class Preferences:
    click_on_results = True # set to False if you don't want to follow links
    email = "" # leave empty if you don't wish to sign in
    max_delay_time = 15 # in seconds
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
        all_results = driver.find_elements_by_xpath("//div/h3/a")
        number_of_results = len(all_results)
        if(number_of_results > 0):
            result_to_click = random.randrange(0, number_of_results)
            all_results[result_to_click].click()
            press_back(driver, options)
        random_delay(options)
    else:
        random_delay(options)

def login_to_google_account(driver, options):
    if options.email != "" and options.password != "":
        driver.find_element_by_id("gb_70").click()
        driver.find_element_by_id("Email").send_keys(options.email)
        driver.find_element_by_id("Passwd").send_keys(options.password)
        driver.find_element_by_id("signIn").click()

def get_search_terms(word_list):
    return word_list[0]

def read_word_list_file():
    text_file = open("word_list.txt", "r")
    text = text_file.read().split('\n')
    text_file.close()
    return text

def main():
    options = Preferences()
    driver = setup_browser()
    word_list = read_word_list_file
    i = 0

    go_to_google_main_page(driver)
    login_to_google_account(driver, options)

    while(i < options.total_searches):
        perform_search(driver, get_search_terms(word_list), options)
        click_on_result(driver, options)
        i+=1

if __name__ == "__main__":
    main()
