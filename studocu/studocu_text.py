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


def ScrapeText():
    # container = chrome.find_element(By.CLASS_NAME, 'c')
    # container = chrome.find_elements_by_css_selector(".c")
    # print(container)


    # name = container.find_element_by_xpath('.//div[@class="t"]')
    # print(name.text)
    # text = chrome.find_element_by_tag("body").text
    # print(text)
    # text= (chrome.find_element(By.ID, 'page-container')).text
    # text = (chrome.find_element(By.ID, 'document-wrapper'))

    text = chrome.find_element(By.XPATH, "/html/body")
    # text = chrome.find_element(By.ID, 'page-container')
    text = text.text
    path = './res.txt'
    with open(path, 'a', encoding="utf-8") as results:
        results.write(text)
        results.close()


def url_name(url):
    chrome.get(url)
    # Adjust sleep
    # time.sleep(3)












def main(url):
    path()
    # time.sleep(1)
    url_name(url)

    time.sleep(10)
    ScrapeText()

    # chrome.close()
    print("closed")


# url = "https://www.studocu.com/en-au/document/higher-school-certificate-new-south-wales/software-design-and-development/sdd-hsc-full-notes/10676503"
url = "https://schoolsnsw-my.sharepoint.com/personal/carlo_famularo1_education_nsw_gov_au/_layouts/15/Doc.aspx?sourcedoc={731bb122-357f-4530-a0d7-c52c89821a86}&action=view&wd=target%289.1.1%20Social%20and%20Ethical%20Issues.one%7Cba8093f8-bcde-496d-8b7b-725909ca2104%2FSyllabus%7C5895d399-dbd5-43a5-8276-81b21e06a28e%2F%29"

main(url)
