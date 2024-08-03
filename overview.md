## Project Description

### Overview

The EDR (Endpoint Detection and Response) Endpoint Security System is a comprehensive solution designed to enhance the security of endpoints within an organization's network. This system aims to monitor, detect, and respond to security threats on endpoints such as laptops, desktops, and servers. By providing real-time monitoring and a centralized management console, the EDR system ensures that IT administrators can effectively manage and secure their network endpoints.

### Components

The project consists of two main components:

1. **Endpoint Agent**: A lightweight agent installed on each endpoint to collect system information and send it to the management console.
2. **Centralized Management Console**: A web-based application that receives data from endpoint agents, stores it in a database, and displays it on a dashboard for real-time monitoring.

### Key Features

- **Real-Time Monitoring**: The endpoint agent collects critical system metrics such as CPU usage, memory usage, and disk usage, and sends this data to the management console at regular intervals.
- **Centralized Management**: The management console provides a unified dashboard to view and analyze endpoint data, making it easier to monitor the overall health and security status of the network.
- **Security and Compliance**: The system helps ensure that endpoints comply with security policies and standards by continuously monitoring their status and generating alerts for suspicious activities.
- **Scalability**: Designed to scale with the organization, the EDR system can handle multiple endpoints and provide a comprehensive view of the network's security posture.

### Technology Stack

- **Python**: Used for developing the endpoint agent and the backend of the management console.
- **Flask**: A lightweight web framework used to build the management console.
- **SQLite**: A lightweight, file-based database used to store endpoint data.
- **Bootstrap**: A front-end framework used for building a responsive dashboard.
- **psutil**: A Python library used by the endpoint agent to collect system metrics.
- **requests**: A Python library used by the endpoint agent to send data to the management console.

### How It Works

1. **Endpoint Agent**: Installed on each endpoint, the agent script periodically collects system information (hostname, OS type, CPU usage, memory usage, and disk usage) and sends it to the management console via HTTP POST requests.
2. **Management Console**: The Flask application receives data from endpoint agents and stores it in an SQLite database. It also provides a web interface (dashboard) where IT administrators can view the collected data in real-time.
3. **Dashboard**: Displays a tabular view of endpoint data, including hostname, OS, CPU usage, memory usage, disk usage, and the timestamp of the last data received. This allows administrators to monitor the status and performance of endpoints at a glance.

### Benefits

- **Improved Security**: By continuously monitoring endpoint activity, the system helps detect and respond to potential security threats in real-time.
- **Centralized Management**: IT administrators can manage and monitor all endpoints from a single dashboard, reducing the complexity of managing multiple devices.
- **Compliance Monitoring**: Ensures that endpoints adhere to security policies and standards, helping organizations maintain compliance with regulatory requirements.
- **Enhanced Visibility**: Provides detailed insights into the performance and status of endpoints, enabling proactive maintenance and troubleshooting.

### Use Cases

- **Corporate IT Security**: For organizations looking to enhance their endpoint security and ensure compliance with internal security policies.
- **Managed Service Providers (MSPs)**: To monitor and manage the security of client endpoints from a centralized platform.
- **Educational Institutions**: To secure and monitor devices used by students and faculty members across campus networks.

The EDR Endpoint Security System is an essential tool for any organization looking to bolster its endpoint security and maintain a robust security posture in an increasingly complex digital landscape.
