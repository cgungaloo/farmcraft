from datetime import datetime
import time
import csv
import RPi.GPIO as GPIO
import Adafruit_DHT
import json

file_name = "app_data/water_log.csv"
temperature_file_name = "app_data/temperature_log.txt"
flag = True

# Pin configuration
DO_PIN = 17  # Digital output connected to GPIO17
PUMP_PIN = 14

# Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(DO_PIN, GPIO.IN)
GPIO.setup(PUMP_PIN, GPIO.OUT)

while flag:
    try:
        moisture_status = GPIO.input(DO_PIN)
        print(f"Moisture Status : {moisture_status}")
        now = datetime.now()
        humidity, temperature = Adafruit_DHT.read_retry(11, 27)
        with open(temperature_file_name, 'w') as tempf:
            tempf.write(f"{temperature}\n")

        print('Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity))
        
        if moisture_status == 1:
            print("watering...")
            GPIO.output(PUMP_PIN, GPIO.HIGH)
            time.sleep(3)
            GPIO.output(PUMP_PIN, GPIO.LOW)
            with open(file_name,'r',newline='') as file:
                reader = list(csv.reader(file))
            entry = [now,temperature,humidity,'auto']

            reader.insert(0, entry)

            with open(file_name, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(reader)
            file.close()
            print('watering_finished')
            
        time.sleep(3)
    except KeyboardInterrupt:
        print("\nProcess interrupted. Exiting gracefully.")
        flag = False
        GPIO.cleanup()
