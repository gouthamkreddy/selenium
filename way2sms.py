#!/usr/bin/env python
import subprocess
from selenium import webdriver
import time
import os
import re
from selenium.webdriver.common.keys import Keys

print('Please Enter 10 Digit Mobile Numeber')
pattern = '[1-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]'
searchstring = raw_input()
match = re.search(pattern, searchstring)

if not match:
	print('Number in Wrong Format')
	exit()

print('Please Enter Message(Should Be less Than 140 Characters)')
send_msg = raw_input()


url = 'http://www.160by2.com/Index'
driver = webdriver.Firefox()
driver.get(url)
time.sleep(10)
driver.find_element_by_tag_name('body').send_keys(Keys.ESCAPE)
time.sleep(3)
uname=driver.find_element_by_name('username')
uname.clear()
uname.send_keys('7752846564')
passwd = driver.find_element_by_name('password')
passwd.clear()
passwd.send_keys('grandgou')
button = driver.find_element_by_xpath("//button[@type='submit']")
button.click()
time.sleep(10)
driver.find_element_by_tag_name('body').send_keys(Keys.ESCAPE)
# [contains(text(), 'My Button')]
send_button = driver.find_element_by_xpath("//*[contains(text(), 'Send Free SMS')]")
send_button.click()
time.sleep(10)
driver.find_element_by_tag_name('body').send_keys(Keys.ESCAPE)
send_sms = driver.find_element_by_xpath("//li[@id='sendSMS']//a")
send_sms.click()
time.sleep(10)
mobile_no = driver.find_element_by_id('ZLJBIV')
mobile_no.clear()
mobile_no.send_keys(searchstring)
message = driver.find_element_by_id('sendSMSMsg')
message.clear()
message.send_keys(send_msg)
send_button = driver.find_element_by_id("btnsendsms")
send_button.click()

#driver.close()
