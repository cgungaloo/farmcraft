from flask import Flask, render_template, jsonify, session
from flask_httpauth import HTTPBasicAuth
from datetime import datetime
import csv
import os

app = Flask(__name__)
file_name = "app_data/water_log.csv"
temp_file = "app_data/temperature_log.txt"
app.secret_key = os.environ.get("SUPER_SECRET_KEY")  # Required for sessions

auth = HTTPBasicAuth()

PWD = os.environ.get("FARMCRAFT_PWD")
print(PWD)

@auth.verify_password
def verify_password(username,password):
    if PWD == password:
        session['user'] = username
        return "AUTH Confirmed"
    return None

@app.route("/")
@auth.login_required
def home():
    return render_template('index.html')

@app.route("/water_log")
def waterlog():
    if 'user' not in session:
        return jsonify({'error': 'Unauthorized'}), 401
    
    with open(file_name,'r',newline='') as file:
        reader = list(csv.reader(file))
        
    response =  jsonify({"readings": reader})
    response.headers.add('Access-Control-Allow-Origin', '*')
    print(response)
    return response

@app.route("/temp_log")
def get_temp():
    if 'user' not in session:
        return jsonify({'error': 'Unauthorized'}), 401
    
    with open(temp_file,'r',newline='') as f:
        temperature = f.readline().strip()
        print(temperature)
        response = jsonify({"temperature": temperature})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

@app.route('/logout')
def logout():
    session.pop('user', None)
    return jsonify({'message': 'Logged out'})
    
if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0',port=5000)