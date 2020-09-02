from flask import Flask,render_template,request,Response
from getcaptchaimg import login_to_website
from htm2json import Attendance2JSON,Internals2JSON,Calendar2JSON,name_scrape,image_scrape
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from json import dumps
import time

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/displaySLCM",methods=["POST"])
def getAttendance():
    print(request.form['username'],request.form['password'])
    login_to_website(request.form['username'],request.form['password'])
    calendarJSON = Calendar2JSON()
    respo = Response(calendarJSON,200)
    respo.headers['Content-Type'] = "application/json"
    return respo

@app.route("/api/v1/post",methods=["POST"])
def handleRequest():
    request_body = request.get_json()
    username = request_body['username']
    password = request_body['password']
    tpe =request_body['type']
    if(tpe == "ATTENDANCE"):
        login_to_website(username,password)
        jsn = Attendance2JSON()
        jsonfinal = dumps(jsn,indent=4, sort_keys=True)
        resp = Response(jsonfinal,200)
        resp.headers['Content-Type'] = "application/json"
        return resp
    elif(tpe == "MARKS"):
        login_to_website(username,password)
        jsn = Internals2JSON()
        jsonfinal = dumps(jsn,indent=4, sort_keys=True)
        resp = Response(jsonfinal,200)
        resp.headers['Content-Type'] = "application/json"
        return resp
    elif(tpe == "CALENDAR"):
        login_to_website(username,password)
        jsn = Calendar2JSON()
        jsonfinal = dumps(jsn,indent=4, sort_keys=True)
        resp = Response(jsonfinal,200)
        resp.headers['Content-Type'] = "application/json"
        return resp
    elif(tpe == "ALL"):
        login_to_website(username,password)
        jsn1 = Internals2JSON()
        jsn2 = Attendance2JSON()
        jsn3 = Calendar2JSON()
        name = name_scrape()
        image = image_scrape()
        imagescrape = {'imageurl': image}
        namescrape = {'name': name}
        jsn = {**namescrape,**imagescrape,**jsn2 , **jsn1,**jsn3}
        jsonfinal = dumps(jsn,indent=4, sort_keys=True)
        resp = Response(jsonfinal,200)
        resp.headers['Content-Type'] = "application/json"
        return resp
    else:
        resp = Response("Error",501)
        return resp
    return "Error"

if __name__ == "__main__":
    app.run(threaded=True)