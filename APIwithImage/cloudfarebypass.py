
from webdriver_manager.chrome import ChromeDriverManager

import pyperclip
from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains 
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent


from selenium.webdriver.common.by import By
chrome_options = Options()
ua = UserAgent()
userAgent = ua.random
print(userAgent)
chrome_options.add_argument(f'user-agent={userAgent}')
    #chrome_options.add_argument('--window-size=800,800')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-infobars")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_argument("--user-data-dir=chrome-data")
driver = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)
chrome_options.add_argument('--no-sandbox')
finaltext =''
driver.maximize_window()
driver.get("https://ezgif.com/image-to-datauri")
time.sleep(10)
urlinput = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="upload-form"]/fieldset/p[2]/input')))
time.sleep(10)
urlinput.click()
time.sleep(10)
pyperclip.paste()
pyperclip.copy(pyperclip.paste())
webdriver.ActionChains(driver).key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
time.sleep(10)
element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[3]/div[2]/form/fieldset/p[4]/input')))
time.sleep(10)
element.click()
time.sleep(10)
WebDriverWait(driver, 5)
select = Select(driver.find_element_by_xpath("""//*[@id="method"]"""))
select.select_by_index(3)
time.sleep(10)
driver.find_element_by_xpath('/html/body/div/div[3]/div[2]/form/p[2]/input').click() 
time.sleep(10)
driver.find_element_by_xpath('/html/body/div/div[3]/div[2]/div[2]/input').click() 
time.sleep(10)
element = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[3]/div[2]/div[2]/input')))
actionChains = ActionChains(driver)
actionChains.double_click(element).perform()
time.sleep(10)
webdriver.ActionChains(driver).key_down(Keys.CONTROL).send_keys("c").perform()
time.sleep(10)
finaltext = pyperclip.paste()
print(finaltext)

