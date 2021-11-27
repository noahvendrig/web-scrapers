from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.common.exceptions
import time

import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import os
import random
import string


def path():
    global chrome
    # Starts new chrome session
    chrome = webdriver.Chrome(
        '..\\92_chromedriver_win32\\chromedriver.exe')  # Add path if required

def url_name(url):
    chrome.get(url)
    # Adjust sleep
    time.sleep(0.5)


def login(username, password):
    # time.sleep(0.5)
    open_login_parent = chrome.find_elements_by_class_name("user-portal")[0]
    open_login_btn =open_login_parent.find_elements_by_xpath(".//*")[0]
    open_login_btn.click()


    time.sleep(10)
    # frm_login_parent = chrome.find_element_by_css_selector("#frmLogin")
    # usern = frm_login_parent.find_element_by_xpath("//input[@cname='user']")[0]
    # usern = chrome.find_element(By.NAME, "user")
    # usern[0].send_keys(username)
    # # sends the entered username
    # # usern.send_keys(username)
    # usern.send_keys(Keys.RETURN)
    # time.sleep(1.5)
    # # finds the password box
    # passw = chrome.find_elements_by_name("passwrd")

    # # sends the entered password box
    # passw.send_keys(password)

    # # press enter after sending password
    # passw.send_keys(Keys.RETURN)
    # time.sleep(3)
    

def download(dir_name, url):
    # os.mkdir(f'./{dir_name}')
    # os.mkdir(f'./{dir_name}/raw')
    # os.mkdir(f'./{dir_name}/cropped')
    
    time.sleep(0.2)
    number_bar_parent = chrome.find_element(By.CLASS_NAME, "pagination")
    number_bar_elements = number_bar_parent.find_elements(By.XPATH, "child::*")
    num_pages = len(number_bar_elements) - 2

    current_page_num = int(chrome.find_element(By.CLASS_NAME, "active").text)
    print(current_page_num)
    print(num_pages)

    # chrome.find_element_by_xpath("//input[@type='text'][position()=1]")

    time.sleep(0.4)
    # note_modal = chrome.find_element(By.ID, 'note-modal')
    # first_child = chrome.find_element(By.XPATH, "//div[@id='note-modal']/following-sibling::div")
    # second_child = first_child.find_element(By.XPATH, "following-sibling::div") # working

    # total_elements = first_child.find_elements(By.XPATH, ".//ename")
    all_siblings = chrome.find_elements(By.XPATH, "//div[@class='note_item col-sm-6 col-md-6 col-lg-4']")
    total_children = len(all_siblings)

    print(total_children,"\n -----------------")

    

    while current_page_num <= num_pages:
        # for sibling in all_siblings:
        print(current_page_num)
        try:
            for n in range(total_children):
                #'''
                all_siblings = chrome.find_elements(By.XPATH, "//div[@class='note_item col-sm-6 col-md-6 col-lg-4']")
                sibling = all_siblings[n]
                # if sibling == all_siblings[1]:
                #     continue
                sibling.click()
                parent = chrome.find_elements(By.XPATH, "//div[@class='js_content_left col-sm-9 col-xs-12 vce__desc']")[0]
                download_btn = parent.find_element(By.XPATH, "a[@class='btn btn-atar']")
                download_btn.click()
                # chrome.get(url)
                chrome.execute_script("window.history.go(-1)")
                time.sleep(0.1)
                # '''
                # print(n)
        except Exception as e:
            # print(e.message, e.args)
            print("Finished!")
            break

        time.sleep(0.5)
        number_bar_parent = chrome.find_element(By.CLASS_NAME, "pagination")
        number_bar_elements = number_bar_parent.find_elements(By.XPATH, "child::*")
        next_page_btn = number_bar_elements[-1]
        
        next_page_btn.click()
        time.sleep(0.5)
        # click on the next page button and do it again lol
        # need click on last child of ul class="pagination" to change the page number
        current_page_num = int(chrome.find_element(By.CLASS_NAME, "active").text)
        


def main(url):
    dir_name = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    username = 'NoahV11'
    password  = 'n6Zea.kx.!GeN9G'
    path()
    # time.sleep(1)
    url_name(url)
    login(username, password)
    download(dir_name, url)
    # crop_images(dir_name)
    # make_pdf(dir_name)
    time.sleep(5)
    # chrome.close()
    print("closed")

url = "https://atarnotes.com/notes/?pag=1&state=3719&subject=4862&unit=0&key=&sort=download"
# url = "https://www.nelsonnet.com.au/login"

main(url)

# crop_images('BjF3qJcsnakJ3jDI')
# make_pdf('BjF3qJcsnakJ3jDI')