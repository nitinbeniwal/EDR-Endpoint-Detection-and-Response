import os
import psutil
import requests
import json
import time

# Function to collect system information
def collect_system_info():
    system_info = {
        "hostname": os.getenv('COMPUTERNAME') or os.uname()[1],
        "os": os.name,
        "cpu_usage": psutil.cpu_percent(interval=1),
        "memory_usage": psutil.virtual_memory().percent,
        "disk_usage": psutil.disk_usage('/').percent,
    }
    return system_info

# Function to send data to the server
def send_data(data):
    url = "http://localhost:5000/api/endpoint-data"
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data=json.dumps(data), headers=headers)
    return response

# Collect and send data periodically
while True:
    data = collect_system_info()
    response = send_data(data)
    print(f"Data sent: {response.status_code}")
    time.sleep(60)  # Wait for 60 seconds before sending the next data
