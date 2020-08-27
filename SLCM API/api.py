from flask import Flask
from flask import jsonify
from htm2json import attendanceJSON
import json 
app = Flask(__name__)


@app.route('/json')
def hello():
    return attendanceJSON

if __name__ == '__main__':
    app.run()