from flask import Flask, render_template, jsonify
from datetime import datetime
import csv

app = Flask(__name__)
file_name = "app_data/water_log.csv"

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/water_log")
def temp():
    with open(file_name,'r',newline='') as file:
        reader = list(csv.reader(file))
        
    response =  jsonify({"readings": reader})
    response.headers.add('Access-Control-Allow-Origin', '*')
    print(response)
    return response


if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0',port=5000)