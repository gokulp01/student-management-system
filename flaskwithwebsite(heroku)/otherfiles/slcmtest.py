from bs4 import BeautifulSoup
import requests
import urllib
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

tess.pytesseract.tesseract_cmd = r'D:\TESSERACT\tesseract.exe'
headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4.4147.135 Safari/537.36' } 
baseurl = 'https://slcm.manipal.edu/'
url ="https://slcm.manipal.edu/loginForm.aspx"
resp = requests.get(url,headers=headers)
s = BeautifulSoup(resp.content,features="lxml")
images = s.find('img',{'id':'imgCaptcha'})['src']

captchaurl = baseurl + images 
print(captchaurl)
##op = webdriver.ChromeOptions()
##op.add_argument('headless')
driver = webdriver.Chrome(ChromeDriverManager().install()) ##,options=op
driver.get(url)
driver.implicitly_wait(3)
driver.execute_script("window.open()")
driver.switch_to_window(driver.window_handles[1])
driver.get(captchaurl)
time.sleep(8)
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
driver.switch_to.window(driver.window_handles[0])
def login_to_website():
    MarksHTML = None
    AttendanceHTML = None
    user_id = driver.find_element_by_xpath('//*[@id="txtUserid"]')
    user_id.clear()
    user_id.send_keys('180907612')
    passwordfinal = driver.find_element_by_xpath('//*[@id="txtpassword"]')
    passwordfinal.clear()
    passwordfinal.send_keys('Mitaspirant14@')
    time.sleep(2)
    captcha = driver.find_element_by_xpath('//*[@id="txtCaptcha"]')
    captcha.clear()
    captcha.send_keys(captcha_text)
    time.sleep(10)
    driver.find_element_by_xpath('//*[@id="btnLogin"]').click() 
    try:
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'rtpchkMenu_lnkbtn2_1')))
    except:
        print("Invalid Username/Password")
        driver.close()
        return None,None
    print ("Logged In")
    element.click()
    WebDriverWait(driver, 5)
     #Find Attendance Table 
    driver.find_element_by_xpath('//a[@href="#3"]').click();
    element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'tblAttendancePercentage')))
    AttendanceHTML = element.get_attribute('outerHTML')

    # element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'dropdown-toggle')))
    # element.click()
    # element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'Repeater2_lnkbtn_2')))
    # element.click()
    # calendarHTML = element.get_attribute('outerHTML')
    # print(calendarHTML)

    for i in range(4):
       try:
        driver.get('https://slcm.manipal.edu/EventCalendar.aspx')
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ContentPlaceHolder1_divAllRep"]')))
        calendarHTML = element.get_attribute('outerHTML')
        print(calendarHTML)
        break
       except StaleElementReferenceException as e:
            raise e
    #print(outer)
    #Find Internal Mark Table
    #print(marks)
    #Logout of SLCM and close chromewebdriver
    driver.get("https://slcm.manipal.edu/loginForm.aspx")
    driver.quit()
    return AttendanceHTML

if __name__ == "__main__":
    AttendanceHTML = login_to_website()

# response = requests.get('https://slcm.manipal.edu/images/logo.png')
# file = open("captchaimage.jpg", "wb")
# file.write(response.content)
# file.close()