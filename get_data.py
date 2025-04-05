import requests
import datetime
import os

url = "https://mcsrranked.com/api/weekly-race/0"

response = requests.get(url)

week_1 = datetime.datetime(2024, 9, 29, 0, 0, 0, tzinfo=datetime.timezone.utc)

if response.status_code == 200:
    current_time = datetime.datetime.now(datetime.timezone.utc)
    current_week = ((current_time - week_1).days // 7) + 1
    timestamp = current_time.strftime("%Y-%m-%d_%H-%M-%S")
    
    folder_name = "data/week_" + str(current_week) + "/"
    os.makedirs(folder_name, exist_ok=True)
    
    file_name = folder_name + timestamp + ".json"
    
    with open(file_name, "w") as f:
        f.write(response.text)
