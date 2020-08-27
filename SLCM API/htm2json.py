from getcaptchaimg import AttendanceHTML
from bs4 import BeautifulSoup
from json import dumps
attendance = AttendanceHTML
def Attendance2JSON(attendance):
    print(attendance)
    attendanceJson = list()
    headers = list()
    soup = BeautifulSoup(attendance,'html.parser')
    table = soup.find_all('table')[0]
    #Get Table Headers
    header = table.find_all('tr')[0]
    for h in header.find_all('th'):
        headers.append(h.text.strip())
    data = table.find_all('tr')[1:]
    for row in data:
        cells = row.find_all('td')
        temp = dict()
        for i in range(0,len(headers)):
            temp[headers[i]] = cells[i].text.strip()
        attendanceJson.append(temp)
    toret = dict({"attendance":attendanceJson})
    return dumps(toret,indent=4, sort_keys=True)

attendanceJSON = Attendance2JSON(attendance)
print(attendanceJSON)