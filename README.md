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
### Centralized Management Console
#### `dashboard.html`
### Requirements
#### `requirements.txt`
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

Ensure the server is running on `http://localhost:5000`.

#### 4. Run the Endpoint Agent

Open a new terminal window, navigate to the `endpoint_agent` directory, and run the agent script:

```sh
cd ../endpoint_agent
python agent.py
```

The agent will collect system information and send it to the Flask server every 60 seconds.

#### 5. Access the Dashboard

Open a web browser and go to `http://localhost:5000` to view the dashboard displaying the endpoint data.

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
