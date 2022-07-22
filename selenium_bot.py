#selenium bot
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
#from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
import time
#import glob
#import os.path

def authorize_bot():

    s = Service("/Users/armaanhirani/Desktop/selenium bot/chromedriver")
    browser = webdriver.Chrome(service=s)
    url = 'https://account.authorize.net/ui/themes/anet/merch.aspx?page=search&sub=batchlist'
    browser.get(url)

    time.sleep(2)

    username = browser.find_element(By.NAME, "input-username")
    username.send_keys("conf.asst5")


    password = browser.find_element(By.NAME, "input-password")
    password.send_keys("Br1ngmemymoney$")
    password.send_keys(Keys.RETURN)

    time.sleep(3)

    transaction_search = browser.find_element(By.LINK_TEXT, "TRANSACTION SEARCH")
    transaction_search.click()

    from_batch = Select(browser.find_element(By.NAME, 'StartBatch'))

    from_batch.select_by_index(2)

    to_batch = Select(browser.find_element(By.NAME, 'EndBatch'))

    to_batch.select_by_index(2)

    to_batch_return = browser.find_element(By.NAME, 'EndBatch')
    to_batch_return.send_keys(Keys.RETURN)


    download = browser.find_element(By.NAME, "Download")
    download.send_keys(Keys.RETURN)

    #popup
    main_page = browser.current_window_handle
    
    # changing the handles to access login page
    main_page = browser.current_window_handle

    for handle in browser.window_handles:
        if handle != main_page:
            download_popup = handle

    browser.switch_to.window(download_popup)

    submit = browser.find_element(By.NAME, "submit")
    submit.click()
    time.sleep(5)
    browser.close()
    browser.switch_to.window(main_page)
    
    # print_button = browser.find_element(By.NAME, "Print")
    # print_button.click()
    # print(browser.window_handles)

    # for handle2 in browser.window_handles:
    #     if handle2 != main_page:
    #     print_popup = handle2
    #     browser.switch_to.window(print_popup)
    #     print = browser.find_element(By.CLASS_NAME, "action-button")
    #     print.click()
    
    

    time.sleep(5)


