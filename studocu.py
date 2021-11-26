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
        '.\\95_chromedriver_win32\\chromedriver.exe')  # Add path if required


def ScrapeText():
    container = chrome.find_element_by_class_name(
        'c')
    # name = container.find_element_by_xpath('.//div[@class="t"]')
    # print(name.text)
    # persons = []
    # for person in chrome.find_elements_by_class_name('person'):
    #     title = person.find_element_by_xpath('.//div[@class="title"]/a').text
    #     company = person.find_element_by_xpath(
    #         './/div[@class="company"]/a').text

    #     persons.append({'title': title, 'company': company})


def url_name(url):
    chrome.get(url)
    # Adjust sleep
    time.sleep(3)


def main(url):
    path()
    time.sleep(1)
    url_name(url)

    time.sleep(1)
    ScrapeText()

    chrome.close()
    print("closed")


url = "https://www.studocu.com/en-au/document/higher-school-certificate-new-south-wales/software-design-and-development/sdd-hsc-full-notes/10676503"

main(url)
