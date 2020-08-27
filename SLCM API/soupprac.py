import requests
from bs4 import BeautifulSoup
from json import dumps
url = r'D:\WEBDEV\SLCM API\page.html'
headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36' } 
soup = BeautifulSoup(open(url).read(),features='lxml')
table = soup.find_all('table')[0]
attendanceJson = list()
    #Get Table Headers
header2 = list()
header = table.find_all('tr')[0]
for h in header.find_all('th'):
    header2.append(h.text.strip())
data = table.find_all('tr')[1:]
for row in data:
    cells = row.find_all('td')
    temp = dict()
    for i in range(0,len(header2)):
        temp[header2[i]] = cells[i].text.strip()
    attendanceJson.append(temp)
toret = dict({"attendance":attendanceJson})
print(toret)