from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.common.exceptions
import time

import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import cv2
import os
import random, string

from PIL import Image
def path():
    global chrome
    # Starts new chrome session
    chrome = webdriver.Chrome('.\\92_chromedriver_win32\\chromedriver.exe')# Add path if required

def url_name(url):
    chrome.get(url)
    # Adjust sleep
    time.sleep(3)


def login(username, password):
    time.sleep(1)
    usern = chrome.find_element_by_name("defaultControl$ctl00$place34$ctl00$PreLoginUserName")

    # sends the entered username
    usern.send_keys(username)
    usern.send_keys(Keys.RETURN)
    time.sleep(1.5)
    # finds the password box
    passw = chrome.find_element_by_name("defaultControl$ctl00$place34$ctl00$Password")

    # sends the entered password box
    passw.send_keys(password)

    # press enter after sending password
    passw.send_keys(Keys.RETURN)
    time.sleep(5.5)
    

def grab_images(dir_name):

    

    os.mkdir(f'./{dir_name}')
    os.mkdir(f'./{dir_name}/raw')
    os.mkdir(f'./{dir_name}/cropped')
    
    time.sleep(2)
    

    # zoom_out = chrome.find_element_by_id("minimize-zoom")
    # zoom_out_child = chrome.find_element_by_class_name("fa-arrows-alt-v")
    # # zoom_out = zoom_out_child.find_element_by_xpath("./..")
    # zoom_out = chrome.find_element_by_class_name("_486f7e68d404")
    # zoom_out.click()

    # fullscreen = chrome.find_element_by_id("fulscrnBtn")
    # fullscreen.click()

    # time.sleep(0.4)
    # page_parent = chrome.find_element_by_class_name('_0424a522e781')
    # max_page_element = page_parent.find_element_by_xpath("./div[@class='_b323c9b02ac8']")


    # max_page = max_page_element.get_attribute('value')
    # print(max_page)

    chrome.execute_script("window.scrollTo(0, 1080)") 
    print("1")
    page_num = 1
    counter = 1
    while page_num != 27:
        break
        page_num_element = chrome.find_element_by_id("jumpToPageInput")
        page_num = page_num_element.get_attribute('value')
        # print(page_num)

        content = chrome.find_element_by_id("page-wrap")
        # chrome.execute_script("document.body.style.zoom = '25%'")
        content.screenshot(f'./{dir_name}/raw/{counter}.png')

        # print("screenshotted!")

        next_btn = chrome.find_element_by_id('next-page-button')
        next_btn.click()
        # print("clicked next page")
        counter += 1
        time.sleep(1)

def crop_images(dir_name):#image_path, coords, saved_location
    dir = f"./{dir_name}/raw"
    for filename in os.listdir(dir):
        if filename.endswith('.png'): 
            im = cv2.imread(f'{dir}/{filename}')
            cropped_img = im[27: 860, 520:1165]
            cv2.imwrite(f'./{dir_name}/cropped/{filename}', cropped_img)
    
def make_pdf(dir_name):
    
    dir = f"./{dir_name}/cropped"
    images = [Image.open(f'{dir}/{img}').convert('RGB') for img in os.listdir(dir)]
    im1 = images[0]

    im1.save(f'./{dir}/{dir_name}.pdf',save_all=True, append_images=images[1:])

def main(url):
    dir_name = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    
    path()
    time.sleep(1)
    url_name(url)
    # login(username, password)
    grab_images(dir_name)
    crop_images(dir_name)
    make_pdf(dir_name)
    time.sleep(1)
    # chrome.close()
    print("closed")

url = "https://www.studocu.com/en-au/document/higher-school-certificate-new-south-wales/software-design-and-development/sdd-trial-paper-from-2018/17726306"
# url = "https://www.nelsonnet.com.au/login"

main(url)

# crop_images('BjF3qJcsnakJ3jDI')
# make_pdf('BjF3qJcsnakJ3jDI')