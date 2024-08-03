from flask import Flask, render_template, request, jsonify
import sqlite3
from datetime import datetime

app = Flask(__name__)

# Initialize database
def init_db():
    conn = sqlite3.connect('edr.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS endpoint_data (
                    id INTEGER PRIMARY KEY,
                    hostname TEXT,
                    os TEXT,
                    cpu_usage REAL,
                    memory_usage REAL,
                    disk_usage REAL,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )''')
    conn.commit()
    conn.close()

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
