# RemoteDesktop-SessionLogger-Activity-Tracker

This repository contains a PowerShell script for monitoring user login/logout activities in Windows 10/11, focusing on Remote Desktop sessions, and a Python script to calculate and analyze working hours from the exported activity logs.

## Features

- Tracks user login and logout times, focusing on Remote Desktop sessions.
- Exports the activity logs to a CSV file for easy analysis.
- Calculates total working hours for users from the activity logs.
- Ideal for auditing, security monitoring, and analyzing user activity patterns.

## Prerequisites

- Windows 10/11 operating system.
- PowerShell 5.0 or higher for running the PowerShell script.
- Python 3.x with Pandas library for running the Python script.

## Installation

1. **PowerShell Script**:
   - No additional installation is required for the PowerShell script. 
   - Clone the repository or download the `UserActivityTracking.ps1` script file to your local machine.

2. **Python Script**:
   - Ensure Python is installed on your system. Download and install Python from [python.org](https://www.python.org/downloads/).
   - Install Pandas using pip:
     ```bash
     pip install pandas
     ```

## Usage

### Running the PowerShell Script

To track user activity:

1. Navigate to the script's directory in PowerShell.
2. Run the script with the following command:
   ```powershell
   .\UserActivityTracking.ps1 -dateParam 'YYYY-MM-DD'
Replace YYYY-MM-DD with the target date for tracking.

# Running the Python Script
To calculate working hours from the generated CSV:

Ensure the CSV file is in the same directory as the Python script or update the filename variable in the script to point to the CSV file's location.
```bash
python user_activity_hours_calculator.py
```

# Output
- The PowerShell script will generate a CSV file with detailed user activity logs.
- The Python script will output the total working hours for each user and save a summary CSV and a log file to the specified directory.
  
# Contributing
  Contributions are welcome. Feel free to fork the repository and submit pull requests to improve the scripts.

# License
  This project is licensed under the MIT License - see the LICENSE file for details.
