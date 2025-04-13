# python background_tasks/watering_manager.py & python app.py &
truncate -s 0 watering.log && nohup python background_tasks/watering_manager.py > watering.log 2>&1 &
truncate -s 0 app.log && nohup python app.py > app.log 2>&1 &