from flask import Flask,render_template,request,Response
from getcaptchaimg import login_to_website
from htm2json import Attendance2JSON
from htm2json import attendanceJSON
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from pyvirtualdisplay import Display
from json import dumps

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("index.html")
@app.route('/json')
def jsonfinal():
    return attendanceJSON

@app.route("/displaySLCM",methods=["POST"])
def getAttendance():
    print(request.form['username'],request.form['password'])
    AttendanceHTML = login_to_website(request.form['username'],request.form['password'])
    attendanceJSON = Attendance2JSON(AttendanceHTML)
    return render_template("index.html",attd=attendanceJSON)

@app.route("/api/v1/get",methods=["POST"])
def handleRequest():
    request_body = dict(request.get_json())
    username = request_body['request']['credentials']['username']
    password = request_body['request']['credentials']['password']
    tpe =request_body['request']['type']
    if(tpe == "ATTENDANCE"):
        attd,_=login_to_website(username,password)
        jsn = Attendance2JSON(attd)
        resp = Response(jsn,200)
        resp.headers['Content-Type'] = "application/json"
        return resp
    elif(tpe == "ALL"):
        attd,marks = login_to_website(username,password)
        jsn2 = Attendance2JSON(attd)
        jsn = dict()
        jsn['attendance'] = jsn2
        resp = Response(dumps(jsn),200)
        resp.headers['Content-Type'] = "application/json"
        return resp
    else:
        resp = Response("Error",501)
        return resp
    return "Error Occured"

if __name__ == "__main__":
    app.run()