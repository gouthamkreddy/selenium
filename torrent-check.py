#!/usr/bin/env python

from selenium import webdriver
import time
import os
import re
import subprocess 
from pyvirtualdisplay import Display

display = Display(visible=0, size=(800, 600))
display.start()


direc = '/home/ahuja0007/torrent/'
script = '/home/ahuja0007/torrent/kill.py'

browser = webdriver.Chrome()

print("Enter the Search term:")
userinput = raw_input()

browser.get("https://kat.cr/usearch/"+userinput)
time.sleep(5)

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def isAria2rpcRunning():
    pgrep_process = subprocess.Popen('pgrep -l aria2', shell=True, stdout=subprocess.PIPE)

    if pgrep_process.stdout.readline() == b'':
        return False
    else:
        return True

torrents = browser.find_elements_by_xpath("//div[@class='torrentname']//a[@class='cellMainLink']")
magnets = browser.find_elements_by_xpath("//div[@class='iaconbox center floatright']//a[@title='Torrent magnet link'][@class='icon16']")
seeds = browser.find_elements_by_xpath("//td[@class = 'green center']")
leech = browser.find_elements_by_xpath("//td[@class = 'red lasttd center']")
Size = browser.find_elements_by_xpath("//td[@class = 'nobr center']")

i = 0
if len(torrents):
	for torrent in torrents:
        	print(str(i+1) + ". " + bcolors.FAIL + torrent.text + bcolors.ENDC + " Size: " + bcolors.OKBLUE + Size[i].text + bcolors.ENDC + " Seeds: " + bcolors.OKGREEN + seeds[i].text + bcolors.ENDC + " Leech: " + bcolors.HEADER + leech[i].text + bcolors.ENDC)
		i=i+1
else:
	print('No torrents Found.Please Run the script with New Search Item')
	display.popen.terminate()
	browser.quit()	
	exit()

print('Enter the Number You Wish To Download(Y/N)')
inp = int(raw_input())
try:
	if inp >= 1 and inp < i:
		print('Downloading ' + bcolors.FAIL + '%s' % torrents[inp-1].text)
		cmd = 'aria2c \'%s\'' % magnets[inp-1].get_attribute('href')
		os.chdir(direc) 
		process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
		count = 0
        	while True:
              		if isAria2rpcRunning():
                  		break
              		else:
                  		count += 1
                  		time.sleep(3)
              		if count == 3:
                  		raise Exception('aria2 RPC server started failure.')
        	print('aria2 RPC server is started.')
	else :
		print('Wrong Input')
except :
	print("Exception Raised")	
display.popen.terminate()
browser.quit()
