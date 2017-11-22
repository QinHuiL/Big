# coding: utf-8
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(chromedriver)
chromedriver = "/usr/local/Cellar/chromedriver/2.33/bin"
driver.get("https://www.baidu.com")
sleep(3)
driver.quiet()
