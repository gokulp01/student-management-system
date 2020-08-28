from bs4 import BeautifulSoup
import requests
import urllib.request
import pytesseract
from PIL import Image
import time
import urllib.request
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains 
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def get_captcha_text(location, size):
    pytesseract.pytesseract.tesseract_cmd = r'D:\TESSERACT\tesseract.exe'
    im = Image.open('screenshot.png') # uses PIL library to open image in memory

    left = location['x']
    top = location['y']
    right =location['x'] + size['width']
    bottom = location['y'] + size['height']


    im = im.crop((left, top, right, bottom)) # defines crop points
    im.save('screenshot.png')
    captcha_text = pytesseract.image_to_string(Image.open('screenshot.png'))
    return captcha_text

def login_to_website():
    url = 'https://slcm.manipal.edu/'
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(url)
    element = driver.find_element_by_xpath('//*[@id="imgCaptcha"]') # find part of the page you want image of
    location = element.location
    size = element.size
    driver.save_screenshot('screenshot.png')
    user_id = driver.find_element_by_xpath('//*[@id="txtUserid"]')
    user_id.clear()
    user_id.send_keys('user-id')
    password = driver.find_element_by_xpath('//*[@id="txtpassword"]')
    password.clear()
    password.send_keys('password')
    time.sleep(2)
    actionChains = ActionChains(driver) 
    actionChains.context_click(element).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
    time.sleep(15)
    captcha = driver.find_element_by_xpath('//*[@id="txtCaptcha"]')
    captcha.clear()
    captcha_text = get_captcha_text(location, size)
    captcha.send_keys(captcha_text)
    print(captcha_text)
    time.sleep(6)
    driver.find_element_by_xpath('//*[@id="btnLogin"]').click()  
    driver.close()
login_to_website()