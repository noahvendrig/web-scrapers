from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.common.exceptions
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def path():
    global chrome
    # Starts new chrome session
    chrome = webdriver.Chrome('./chromedriver.exe')  # Add path if required

def login():
    email = 'noahvendrig@gmail.com'
    password = 'Zej-nD39k6GY5wE'
    # chrome.get('https://www.facebook.com/')
    chrome.find_element_by_id('email').send_keys(email)
    chrome.find_element_by_id('pass').send_keys(password)
    chrome.find_element_by_id('loginbutton').click()

def url_name(url):
    chrome.get(url)
    # Adjust sleep
    # time.sleep(3)

def FindPosts():
    all = chrome.find_elements_by_class_name("a8c37x1j")
    all = chrome.findElements(By.xpath("//div[@class='atb-delivery-accordions']"));
    # t = all[1].text + "EE"
    # print(t)
    for listing in all:
        print(listing.text)


def main(url):
    path()
    # time.sleep(1)
    url_name(url)
    time.sleep(0.5)
    login()
    time.sleep(1)
    url_name(url)
    time.sleep(2)
    FindPosts()

    # chrome.close()
    # print("closed")


query = 'celica'
url = f"https://www.facebook.com/marketplace/category/search/?query={query}"

main(url)