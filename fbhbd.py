#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pync import Notifier
import time
import os

chromedriver = "/Users/gouthamkreddy/Documents/web/git/selenium/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver

browser = webdriver.Chrome(chromedriver)

browser.get("https://www.facebook.com")
time.sleep(5)
username=browser.find_element_by_name('email')
username.clear()
username.send_keys('gouthamkreddy@gmail.com')
password = browser.find_element_by_name('pass')
password.clear()
password.send_keys('asd!@#123')
button = browser.find_element_by_xpath("//input[@value='Log In']")
button.click()
time.sleep(10)
browser.get("https://www.facebook.com/events/birthdays")
textarea = browser.find_elements_by_xpath("//textarea[@title='Write a birthday wish on his Timeline...']")

if len(textarea):
    for text in textarea:
        text.clear()
        text.send_keys('Happy Birthday :)')
        text.send_keys(Keys.ENTER)
    time.sleep(2)
    Notifier.notify('Birthdays Wishing Done', title='Birthday Script')
else:
    time.sleep(2)
    Notifier.notify('No Birthdays Today', title='Birthday Script')

time.sleep(10)
browser.quit()

