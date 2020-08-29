from bs4 import BeautifulSoup
# from slcm import user_name, pass_word
import requests
import time
from PIL import Image
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains 
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import pytesseract as tess
from PIL import Image
import pyautogui as P
from binascii import a2b_base64
import urllib
from json import dumps
from urllib import request
tess.pytesseract.tesseract_cmd = r'D:\TESSERACT\tesseract.exe'
headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4.4147.135 Safari/537.36' } 
baseurl = 'https://slcm.manipal.edu/'
url ="https://slcm.manipal.edu/loginForm.aspx"
resp = requests.get(url,headers=headers)
chrome_options = Options()
    #chrome_options.add_argument('--window-size=800,800')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--remote-debugging-port=9222")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--auto-open-devtools-for-tabs ')
driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=chrome_options)
str=''
def get_capt():
    driver.maximize_window()
    s = BeautifulSoup(resp.content,features="lxml")
    images = s.find('img',{'id':'imgCaptcha'})['src']
    captchaurl = baseurl + images 
    print(captchaurl)
    driver.execute_script("window.open()")
    driver.switch_to_window(driver.window_handles[1])
    driver.get(captchaurl)
    # time.sleep(2)
    element = driver.find_element_by_xpath('/html/body/img') # find part of the page you want image of
    location = element.location
    size = element.size
    driver.save_screenshot('screenshot.png')
    im = Image.open('screenshot.png') # uses PIL library to open image in memory
    left = location['x']
    top = location['y']
    right =location['x'] + size['width']
    bottom = location['y'] + size['height']
    im = im.crop((left, top, right, bottom))
    im = im.convert('L') # defines crop points
    im.save('screenshot.png')
    img = Image.open('screenshot.png')
    captcha_text = tess.image_to_string(img).strip()
    print(captcha_text)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    return captcha_text

# 1603,128 
# 1477,620
# 1751,200
def image_scrape():
    P.click(x=1603, y=128)
    time.sleep(1)
    P.click(x=1477,y=620)
    time.sleep(1)
    P.click(button='right',x=1751, y=200)
    time.sleep(1)
    P.press('down',2)
    P.press('enter')
    time.sleep(1)
    P.hotkey("ctrl", "l")
    time.sleep(1)
    P.hotkey("ctrl","v")
    time.sleep(1)
    P.press("enter")
    str=driver.current_url
    # print(str)
    time.sleep(1)
    response = urllib.request.urlopen(str)
    with open('image.jpg', 'wb') as f:
        f.write(response.file.read())

def login_to_website(username=None,password=None):
    driver.maximize_window()
    # time.sleep(2)
    driver.get(url)
    captcha_text=get_capt()
    MarksHTML = None
    AttendanceHTML = None
    calendarHTML = None
    user_id = driver.find_element_by_xpath('//*[@id="txtUserid"]')
    user_id.clear()
    user_id.send_keys(username)
    passwordfinal = driver.find_element_by_xpath('//*[@id="txtpassword"]')
    passwordfinal.clear()
    passwordfinal.send_keys(password)
    captcha = driver.find_element_by_xpath('//*[@id="txtCaptcha"]')
    captcha.clear()
    captcha.send_keys(captcha_text)
    # time.sleep(10)
    driver.find_element_by_xpath('//*[@id="btnLogin"]').click() 
    time.sleep(1)
    if (driver.current_url == 'https://slcm.manipal.edu/studenthomepage.aspx'):

        print ("Logged In")
        #Find Attendance Table 
        element = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, 'rtpchkMenu_lnkbtn2_1')))
        element.click()
        driver.find_element_by_xpath('//a[@href="#3"]').click();
        element = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, 'tblAttendancePercentage')))
        AttendanceHTML = element.get_attribute('outerHTML')
        with open('attendance.html', 'wb') as f:
            f.write(AttendanceHTML.encode('utf-8'))

        driver.find_element_by_xpath('//a[@href="#4"]').click()
        element = WebDriverWait(driver,1).until(EC.presence_of_element_located((By.ID,'PrintInternal')))
        MarksHTML = element.get_attribute('outerHTML')
        with open('marks.html', 'wb') as f:
            f.write(MarksHTML.encode('utf-8'))
        # WebDriverWait(driver,3)
        driver.get('https://slcm.manipal.edu/EventCalendar.aspx')
        try:
            element = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, 'ContentPlaceHolder1_divAllRep')))   
           
        except StaleElementReferenceException as e:
            raise e
        calendarHTML = element.get_attribute('outerHTML')
        with open('calendar.html', 'wb') as f:
            f.write(calendarHTML.encode('utf-8'))
        page = driver.page_source
        
        with open('homepage.html', 'wb') as f:
            f.write(page.encode('utf-8'))
            # f.close()
        image_scrape()
    else:
        print("Invalid Username/Password/Captcha")
        login_to_website(username, password)

if __name__ == "__main__":
    name = login_to_website("username","password")

