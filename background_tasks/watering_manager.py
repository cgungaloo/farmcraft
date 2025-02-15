from datetime import datetime
import time
import csv
import RPi.GPIO as GPIO

file_name = "app_data/water_log.csv"
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
        if moisture_status == 0:
            print("watering...")
            with open(file_name,'r',newline='') as file:
                reader = list(csv.reader(file))
            entry = [now,21,100,'auto']

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


# # Setup
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(DO_PIN, GPIO.IN)
# GPIO.setup(PUMP_PIN, GPIO.OUT)

# try:
#     while True:
#         moisture_status = GPIO.input(DO_PIN)
#         if moisture_status == 0:
#             print("Soil is moist")
#         else:
#             print("Soil is dry")
#             GPIO.output(PUMP_PIN, GPIO.HIGH)
#             time.sleep(3)
#             GPIO.output(PUMP_PIN, GPIO.LOW)
#         time.sleep(5)

# except KeyboardInterrupt:
#     print("Exiting...")
#     GPIO.cleanup()
