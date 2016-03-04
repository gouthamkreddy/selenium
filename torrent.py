#!/usr/bin/env python

from selenium import webdriver
from pync import Notifier
import time
import os
import re

chromedriver = "/Users/gouthamkreddy/Documents/web/git/selenium/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver

browser = webdriver.Chrome(chromedriver)

print("Enter the Search term:")
userinput = raw_input()
browser.get("https://kat.cr/usearch/"+userinput)

time.sleep(5)

pattern = ".*720p.*"

torrents = browser.find_elements_by_xpath("//div[@class='torrentname']//a[@class='cellMainLink']")
magnets = browser.find_elements_by_xpath("//div[@class='iaconbox center floatright']//a[@title='Torrent magnet link'][@class='icon16']")

i = 0

for magnet in magnets:
    print(magnet.get_attribute('href'))

# for torrent in torrents:
#     searchstring = torrent.text
#     match = re.search(pattern, searchstring)
#     if match:
#         print(torrent.text+" "+magnets[i])
#     i=i+1

time.sleep(5)
browser.quit()


