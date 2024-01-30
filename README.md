# RemoteDesktop-SessionLogger-Activity-Tracker
PowerShell script for monitoring user login/logout activities and working hours in Windows 10/11, particularly focused on Remote Desktop session tracking. It captures and logs session details, providing insights into user activity patterns for system administrators and IT professionals. Ideal for auditing and security monitoring purposes.
## Features

- Tracks user login and logout times.
- Focuses on Remote Desktop sessions.
- Exports the activity logs to a CSV file for easy analysis.

## Getting Started

These instructions will help you set up and run the script on your local machine for development and testing purposes.

### Prerequisites

- Windows 10/11 operating system.
- PowerShell 5.0 or higher.

### Installation

No additional installation is required. Just clone the repository or download the script file to your local machine.

### Usage

To run the script, navigate to the script's directory in PowerShell and enter:

```powershell
.\UserActivityTracking.ps1 -dateParam 'YYYY-MM-DD'
