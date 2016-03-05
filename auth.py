#!/usr/bin/env python

from selenium import webdriver
from pync import Notifier
from selenium.common.exceptions import NoSuchElementException
# from pyvirtualdisplay import Display
import requests
import time
import re

# display = Display(visible=0, size=(800, 600))
# display.start()

browser = webdriver.Firefox()
pattern = ".*google.*"
pattern_gateway = ".*gateway.*"


while True:
    browser.get("https://google.com")
    searchstring = browser.current_url
    match = re.search(pattern, searchstring)
    if match:
    	try:
			status_code = requests.get('https://google.com').status_code
			Notifier.notify('Already Logged In', title='Auth Script')
			time.sleep(60)
			continue
        except:
       		Notifier.notify('No Internet Idiot', title='Auth Script')
       		break
	match = re.search(pattern_gateway, searchstring)
    if match:
    	username = browser.find_element_by_name('username')
    	username.clear()
    	username.send_keys('guestvh')
    	password = browser.find_element_by_name('password')
    	password.clear()
    	password.send_keys('vhguest')
    	button = browser.find_element_by_xpath("//input[@type='submit'][@value='Continue']")
    	button.click()
    	Notifier.notify('Login Successfull', title='Auth Script')
    	time.sleep(60)      
    

time.sleep(5)
browser.quit()

