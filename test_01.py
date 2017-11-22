# coding: utf-8
from selenium import webdriver
import selenium.webdriver.chrome.service as service

service = service.Service('/usr/local/Cellar/chromedriver/2.33/bin')
service.start()
capabilities = {'chrome.binary': '/Applications/Google Chrome.app/Contents/MacOS'}
driver = webdriver.Remote(service.service_url, capabilities)
driver.get('http://www.google.com/xhtml');
time.sleep(5) # Let the user actually see something!
driver.quit()
