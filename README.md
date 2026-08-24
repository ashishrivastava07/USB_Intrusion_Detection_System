# USB Intrusion Detection System (USB-IDS)

A Python-based cybersecurity tool that monitors USB device activity on Windows, identifies connected devices, verifies authorization status, logs security events, and alerts users about unauthorized USB devices.

## Features

* Real-time USB device monitoring
* USB device identification
* Authorized/unauthorized device detection
* Security alerts
* SQLite-based event logging
* Tkinter monitoring dashboard

## Technologies

`Python` · `SQLite` · `Tkinter` · `WMI` · `PyWin32`

## Project Structure

```text
usb-intrusion-detection-system/
├── src/
│   ├── database.py
│   ├── usb_detector.py
│   ├── usb_monitor.py
│   └── dashboard.py
├── data/
├── docs/
├── screenshots/
├── README.md
├── requirements.txt
└── .gitignore
```

## Installation

```bash
git clone https://github.com/ashishrivastava07/usb-intrusion-detection-system.git
cd usb-intrusion-detection-system

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt
```

## Run

```bash
python src/dashboard.py
```

## Workflow

```text
USB Connected
      ↓
Detect Device
      ↓
Extract Device Information
      ↓
Check Authorization
      ↓
 ┌───────────────┐
 │               │
Authorized    Unauthorized
 │               │
 ↓               ↓
Log Event     Alert User
 │               │
 └───────┬───────┘
         ↓
   SQLite Database
         ↓
      Dashboard
```

## Database

USB events are stored in SQLite with information including:

* Timestamp
* Device name
* Device ID
* Manufacturer
* Authorization status
* Event type

## Future Scope

* Automatic blocking of unauthorized devices
* Device fingerprinting
* ML-based anomaly detection
* Email/SMS notifications
* SIEM integration
* Centralized monitoring

## Disclaimer

Developed for educational and authorized cybersecurity research purposes. The current implementation is designed for Windows systems.

## Author

**Ashi Shrivastava**
B.Tech – Computer Science & Engineering (Cyber Security)
Lakshmi Narain College of Technology & Science, Bhopal
