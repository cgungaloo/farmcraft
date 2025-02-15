from datetime import datetime
import time
import csv

file_name = "app_data/water_log.csv"
flag = True
while flag:
    try:
        print("reading_temperature....")
        now = datetime.now()
        seconds = now.second
        if seconds % 5 ==0:
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