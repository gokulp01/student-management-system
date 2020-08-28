from bs4 import BeautifulSoup
from json import dumps
def Attendance2JSON():
    attendanceJson = list()
    headers = list()
    url = r'attendance.html'
    soup = BeautifulSoup(open(url).read(),features='lxml')
    table = soup.find_all('table')[0]
    #Get Table Headers
    header = table.find_all('tr')[0]
    for h in header.find_all('th'):
        headers.append(h.text.strip())
    print(headers)
    data = table.find_all('tr')[1:]
    for row in data:
        cells = row.find_all('td')
        temp = dict()
        for i in range(0,len(headers)):
            temp[headers[i]] = cells[i].text.strip()
        attendanceJson.append(temp)
    toret = dict({"attendance":attendanceJson})
    return dumps(toret,indent=4, sort_keys=True)
def Internals2JSON():
    subjectsJSON = dict()
    headers = list()
    marksJSON = list()
    url = r'marks.html'
    soup = BeautifulSoup(open(url).read(),features='lxml')
    maindiv = soup.find("div",{"id":"accordion1"})
    subjects = maindiv.find_all_next("div",{"class":"panel panel-default"})
    for subject in subjects:
        sub_name = subject.find("a").text
        sub_name = sub_name.strip().strip("Subject Code:").strip()
        sub_name = sub_name.split("  ")
        code = sub_name[0]
        name = sub_name[1]
        subjectsJSON[code] = name
        tables = subject.find_all("table")
        for table in tables:
            #Get Table Headers
            headers = list()
            header = table.find_all('tr')[0]
            for h in header.find_all('th'):
                headers.append(h.text.strip())
            #Get Table Content And Conver It To Json
            data = table.find_all('tr')[1:]
            for row in data:
                cells = row.find_all('td')
                temp = dict()
                temp["type"] = headers[0]
                temp["sub_code"] = code
                temp["sub_name"] = name
                for i in range(0,len(headers)):
                    temp[""+headers[i]+""] = cells[i].text.strip()
                marksJSON.append(temp)
    marksJSON = dict({"marks":marksJSON})
    return dumps(marksJSON,indent=4, sort_keys=True)
def Calendar2JSON():
    url = r'calendar.html'
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
    calendar2JSON = dict({"calendar":calendarJson})
    return dumps(calendar2JSON,indent=4, sort_keys=True)


if __name__ == "__main__":
    attendanceJSON = Attendance2JSON('AttendanceHTML')
    subjectJSON,marksJSON = Internals2JSON('MarksHTML')
    calendar2JSON = Calendar2JSON('calendarHTML')
    print(calendar2JSON)