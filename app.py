from flask import Flask, render_template, jsonify
from datetime import datetime
import csv

app = Flask(__name__)
file_name = "app_data/water_log.csv"
temp_file = "app_data/temperature_log.txt"

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/water_log")
def waterlog():
    with open(file_name,'r',newline='') as file:
        reader = list(csv.reader(file))
        
    response =  jsonify({"readings": reader})
    response.headers.add('Access-Control-Allow-Origin', '*')
    print(response)
    return response

@app.route("/temp_log")
def get_temp():
    with open(temp_file,'r',newline='') as f:
        temperature = f.readline().strip()
        print(temperature)
        response = jsonify({"temperature": temperature})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    
if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0',port=5000)