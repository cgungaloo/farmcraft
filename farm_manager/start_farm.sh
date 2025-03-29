# python background_tasks/watering_manager.py & python app.py &
nohup python background_tasks/watering_manager.py > watering.log 2>&1 &
nohup python app.py > app.log 2>&1 &