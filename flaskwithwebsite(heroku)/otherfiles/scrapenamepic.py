import requests
from bs4 import BeautifulSoup
from json import dumps
import urllib.request  
url = r'D:\WEBDEV\SLCM API\homepage.html'
soup = BeautifulSoup(open(url).read(),features='lxml')
name = soup.find('span',{'id':'lblUserName'})
image = soup.find('img',{'id':'Repeater1_Image2_0'})
urlfinal = image['src']
print(name.text)
print(urlfinal)