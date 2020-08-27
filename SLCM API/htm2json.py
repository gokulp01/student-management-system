from getcaptchaimg import login_to_website
from bs4 import BeautifulSoup
from json import dumps

def Attendance2JSON(AttendanceHTML):
    attendanceJson = list()
    headers = list()
    soup = BeautifulSoup(AttendanceHTML,'html.parser')
    table = soup.find_all('table')[0]
    #Get Table Headers
    header = table.find_all('tr')[0]
    for h in header.find_all('th'):
        headers.append(h.text.strip())
    #Get Table Content And Conver It To Json
    data = table.find_all('tr')[1:]
    for row in data:
        cells = row.find_all('td')
        temp = dict()
        for i in range(0,len(headers)):
            temp[headers[i]] = cells[i].text.strip()
        attendanceJson.append(temp)
    toret = dict({"attendance":attendanceJson})
    return dumps(toret,indent=4, sort_keys=True)

def Internals2JSON(MarksHTML):
    subjectsJSON = dict()
    headers = list()
    marksJSON = list()
    soup = BeautifulSoup(MarksHTML,"html.parser")
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


if __name__ == "__main__":
    subjectJSON,marksJSON = Internals2JSON("MarksHTML")
    attendanceJSON = Attendance2JSON("AttendanceHTML")
    print(subjectJSON)
    print(marksJSON)
    print(attendanceJSON)