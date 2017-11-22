# coding: utf-8
from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get('http://www.google.com/xhtml');
sleep(5) # Let the user actually see something!
driver.quit()
