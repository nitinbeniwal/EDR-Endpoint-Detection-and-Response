Sure, here is the complete `README.md` file in Markdown format for your EDR Endpoint Security project.

```markdown
# EDR Endpoint Security System

## Overview

The EDR Endpoint Security System is designed to monitor, detect, and respond to security threats on endpoints within an organization's network. This project includes an endpoint agent that collects system information and a centralized management console that displays the collected data and alerts on a web-based dashboard.

## Project Structure

```






EDR-Endpoint-Security/
│
├── endpoint_agent/
│   └── agent.py
│
├── management_console/
│   ├── app.py
│   ├── templates/
│   │   └── dashboard.html
│   ├── requirements.txt
│   └── edr.db
│
└── README.md
```







## Components

### Endpoint Agent

The endpoint agent collects system information such as CPU usage, memory usage, disk usage, and sends it to the centralized management console.

#### `agent.py`

```python
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
    url = "http://localhost:5000/api/endpoint-data"  # Ensure this matches the Flask server URL
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data=json.dumps(data), headers=headers)
    return response

# Collect and send data periodically
while True:
    data = collect_system_info()
    response = send_data(data)
    print(f"Data sent: {response.status_code}")
    time.sleep(60)  # Wait for 60 seconds before sending the next data
```

### Centralized Management Console

The centralized management console receives data from the endpoint agents and displays it on a web-based dashboard.

#### `app.py`

```python
from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

# Initialize database
def init_db():
    conn = sqlite3.connect('edr.db')  # Connect to (or create) the database file
    c = conn.cursor()  # Create a cursor object to interact with the database
    # Create the endpoint_data table if it doesn't already exist
    c.execute('''CREATE TABLE IF NOT EXISTS endpoint_data (
                    id INTEGER PRIMARY KEY,
                    hostname TEXT,
                    os TEXT,
                    cpu_usage REAL,
                    memory_usage REAL,
                    disk_usage REAL,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )''')
    conn.commit()  # Save (commit) the changes to the database
    conn.close()  # Close the database connection

init_db()

# Route to render the dashboard
@app.route('/')
def dashboard():
    conn = sqlite3.connect('edr.db')
    c = conn.cursor()
    c.execute("SELECT hostname, os, cpu_usage, memory_usage, disk_usage, timestamp FROM endpoint_data")
    data = c.fetchall()
    conn.close()
    return render_template('dashboard.html', data=data)

# Route to receive endpoint data
@app.route('/api/endpoint-data', methods=['POST'])
def receive_data():
    data = request.get_json()
    conn = sqlite3.connect('edr.db')
    c = conn.cursor()
    c.execute("INSERT INTO endpoint_data (hostname, os, cpu_usage, memory_usage, disk_usage) VALUES (?, ?, ?, ?, ?)",
              (data['hostname'], data['os'], data['cpu_usage'], data['memory_usage'], data['disk_usage']))
    conn.commit()
    conn.close()
    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(debug=True)
```

#### `dashboard.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>EDR Dashboard</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h1 class="mt-5">Endpoint Detection and Response Dashboard</h1>
        <table class="table mt-3">
            <thead>
                <tr>
                    <th>Hostname</th>
                    <th>OS</th>
                    <th>CPU Usage (%)</th>
                    <th>Memory Usage (%)</th>
                    <th>Disk Usage (%)</th>
                    <th>Timestamp</th>
                </tr>
            </thead>
            <tbody>
                {% for row in data %}
                <tr>
                    <td>{{ row[0] }}</td>
                    <td>{{ row[1] }}</td>
                    <td>{{ row[2] }}</td>
                    <td>{{ row[3] }}</td>
                    <td>{{ row[4] }}</td>
                    <td>{{ row[5] }}</td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
    </div>
</body>
</html>
```

### Requirements

#### `requirements.txt`

```
Flask
psutil
requests
```

### Setup and Running

#### 1. Clone the Repository

```sh
git clone <repository_url>
cd EDR-Endpoint-Security
```

#### 2. Set Up the Management Console

Navigate to the `management_console` directory and install the required packages:

```sh
cd management_console
pip install -r requirements.txt
```

#### 3. Initialize the Database and Start the Flask Server

Run the Flask application:

```sh
python app.py
```

Ensure the server is running on `http://127.0.0.1:5000`.

#### 4. Run the Endpoint Agent

Open a new terminal window, navigate to the `endpoint_agent` directory, and run the agent script:

```sh
cd ../endpoint_agent
python agent.py
```

The agent will collect system information and send it to the Flask server every 60 seconds.

#### 5. Access the Dashboard

Open a web browser and go to `http://127.0.0.1:5000` to view the dashboard displaying the endpoint data.

### Troubleshooting

- **Flask Server Issues:** Ensure the Flask server is running without errors. Check for any stack traces or error messages in the terminal where `app.py` is running.
- **Agent Connection Issues:** Ensure the agent is pointing to the correct URL and port of the Flask server. Verify there are no network issues.
- **Database Issues:** Ensure the `edr.db` file is in the correct location and the `endpoint_data` table exists.

## Contributing

Contributions are welcome! Please fork this repository and submit pull requests for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
```

This `README.md` file provides an overview of the project, explains the project structure, and gives detailed instructions on setting up, running, and troubleshooting the EDR Endpoint Security System.
