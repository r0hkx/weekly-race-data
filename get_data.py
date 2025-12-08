import requests
import datetime
import os

week_1 = datetime.datetime(2024, 9, 30, 0, 0, 0, tzinfo=datetime.timezone.utc)
current_time = datetime.datetime.now(datetime.timezone.utc)
current_week = ((current_time - week_1).days // 7) + 1

url = "https://mcsrranked.com/api/weekly-race/" + str(current_week)

response = requests.get(url)

if response.status_code == 200:
    timestamp = current_time.strftime("%Y-%m-%d_%H-%M-%S")
    
    folder_name = "data/week_" + str(current_week) + "/"
    os.makedirs(folder_name, exist_ok=True)
    
    file_name = folder_name + timestamp + ".json"
    
    with open(file_name, "w") as f:
        f.write(response.text)
else:
    print(str(response.status_code) + " bad response")
