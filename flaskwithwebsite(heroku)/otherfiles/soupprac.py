import requests
from bs4 import BeautifulSoup
from json import dumps
url = r'D:\WEBDEV\SLCM API\page.html'
soup = BeautifulSoup(open(url).read(),features='lxml')
textheader = soup.find_all('div',{'class':'event-header-even table-responsive'})
calendarJson = list()
    #Get Table Headers
headers = list()
headers = ['date','notice','startdate','enddate','totaldays']
print(len(headers))
i=0
while(i<5):
    span = textheader[i].find_all('span')
    j=0
    temp = dict()
    for k in range(0,len(headers)):
        temp[headers[k]] = span[k].text
    calendarJson.append(temp)
    i+=1
toret = dict({"calendar":calendarJson})
print(toret)
