from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
import io
import random
import time

class Preferences:
    click_on_results = True # set to False if you don't want to follow links
    email = "" # leave empty if you don't wish to sign in
    max_delay_time = 15 # in seconds
    max_search_terms = 4
    password = "" # leave empty if you don't wish to sign in
    total_searches = 1000 # so script won't run forever if you forget about it

def setup_browser():
    firefox_profile = FirefoxProfile()
    # Reduce bandwidth consumption and increase speed by disabling images, Flash
    firefox_profile.set_preference('permissions.default.image', 2)
    firefox_profile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so',
                                  'false')
    return webdriver.Firefox(firefox_profile)

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
            # sometimes get element not visible; not sure why
            if all_results[result_to_click].is_displayed():
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

def get_search_terms(word_list, options):
    return random.sample(word_list, options.max_search_terms)

def perform_search(driver, search_terms, options):
    if "www.google.com" not in driver.current_url:
        go_to_google_main_page(driver) # sites like Twitter break back button

    search_locator = "gbqfq"
    search_box = driver.find_element_by_id(search_locator)
    search_box.clear()

    terms_string = ""
    max_terms = random.randrange(2, options.max_search_terms + 1)
    for i in xrange(max_terms):
        terms_string += search_terms[i] + " "
    terms_string = terms_string.rstrip()

    search_box.send_keys(terms_string)
    search_box.send_keys(Keys.RETURN)
    random_delay(options)

def read_word_list_file():
    with io.open('word_list.txt', 'r') as text_file:
        text = text_file.read().split('\n')
    return text

def setup_google(driver, options):
    go_to_google_main_page(driver)
    login_to_google_account(driver, options)

def main():
    options = Preferences()
    driver = setup_browser()
    word_list = read_word_list_file()
    setup_google(driver, options)

    i = 0
    while(i < options.total_searches):
        search_terms = get_search_terms(word_list, options)
        perform_search(driver, search_terms, options)
        click_on_result(driver, options)
        i+=1

if __name__ == "__main__":
    main()
