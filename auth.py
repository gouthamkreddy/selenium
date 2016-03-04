#!/usr/bin/env python

from selenium import webdriver
from pync import Notifier
# from pyvirtualdisplay import Display
import time

#display = Display(visible=0, size=(800, 600))
#display.start()

browser = webdriver.Firefox()

while True:
    try:
        browser.get("https://google.com")
        username = browser.find_element_by_name('username')
        username.clear()
        username.send_keys('guestvh')
        password = browser.find_element_by_name('password')
        password.clear()
        password.send_keys('vhguest')
        button = driver.find_element_by_xpath("//input[@type='submit'][@value='Continue']")
        button.click()
        Notifier.notify('Login Successfull', title='Auth Script')
        time.sleep(60)
    except:
		Notifier.notify('Already Logged In', title='Auth Script')    	
		time.sleep(60)

