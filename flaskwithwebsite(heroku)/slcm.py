from flask import Flask,render_template,request,Response,redirect
from getcaptchaimg import login_to_website
from htm2json import Attendance2JSON,Internals2JSON,Calendar2JSON,name_scrape,image_scrape
from json import dumps
from json2html import *
import requests
from PIL import Image
import io
import base64
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")
@app.route("/login")
def loginpage():
    return render_template("loginpage.html")
@app.route("/authors")
def authorspage():
    return render_template("authors.html")
@app.route("/livestatus")
def livestatus():
    return render_template("livestatus.html")
@app.route("/results",methods=["POST"])
def getAttendance():
    print(request.form['username'],request.form['password'])
    login_to_website(request.form['username'],request.form['password'])
    attendanceJSON = Attendance2JSON()
    marksJSON = Internals2JSON()
    calendarJSON = Calendar2JSON()
    name = name_scrape()
    namescrape = {'name': name}
    calendarfinal = json2html.convert(json = calendarJSON['calendar'])
    attendancefinal = json2html.convert(json = attendanceJSON['attendance'])
    markfinal = json2html.convert(json = marksJSON['marks'])
    url = "https://slcm.manipal.edu/imagereader.aspx"
    imagelink = image_scrape()
    imagepath=imagelink.split("ImagePath=",1)[1]
    querystring = {"FileName":"","ImagePath": "{}".format(imagepath)}
    response = requests.request("GET", url, params=querystring)
    image = Image.open(io.BytesIO(response.content))
    encoded = base64.b64encode(response.content).decode('UTF-8')
    datauri = "data:image/png;base64," + encoded
    return render_template("afterlogin.html",mark=markfinal,greetingname=name,atten = attendancefinal,cal = calendarfinal,datauri = datauri)

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
    app.run(port=5000,debug=True)