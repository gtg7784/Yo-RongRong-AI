import requests
import os
import json
import chromedriver_autoinstaller as driver
from bs4 import BeautifulSoup
from selenium import webdriver

if __name__ == "__main__":
  driver.install()

  options = webdriver.ChromeOptions()
  options.add_argument("start-maximized")
  options.add_argument("lang=ko_KR")
  options.add_argument('headless')
  options.add_argument('window-size=375,900')
  options.add_argument("disable-gpu")
  options.add_argument("--no-sandbox")

  driver = webdriver.Chrome(options=options)
  driver.implicitly_wait(3)