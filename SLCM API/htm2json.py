from getcaptchaimg import login_to_website
from bs4 import BeautifulSoup
from json import dumps
def Attendance2JSON(AttendanceHTML):
    print(AttendanceHTML)
    attendanceJson = list()
    headers = list()
    soup = BeautifulSoup(AttendanceHTML,'html.parser')
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

if __name__ == "__main__":
    attendanceJSON = Attendance2JSON('AttendanceHTML')