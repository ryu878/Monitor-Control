# Monitor Control

A lightweight Python utility for Ubuntu/Zorin OS (X11) that detects connected monitors and provides a system tray icon to quickly turn specific monitors ON or OFF using xrandr.

Useful for multi-monitor setups (e.g., laptops with external displays) where you want quick control without navigating system settings.

---

## Features

- System tray icon with:
  - **Turn Off Monitors**
  - **Turn On Monitors**
  - **Quit**
- Uses **PyQt5** for reliable tray support on Ubuntu/X11.
- Works with any number of monitors (set names inside the script).
- Optional autostart on login.


Uses PyQt5 for stable tray integration on Ubuntu/X11.

Works with any number of monitors (configure names inside the script).

Autostart support.

## Install requirements
```bash
sudo apt install python3-pyqt5
```

## Create tray_monitor_control.py and save it as

`
/usr/local/bin/tray_monitor_control.py
`

Make executable:

`
sudo chmod +x /usr/local/bin/tray_monitor_control.py
`

## Start the tray automatically on login

Create autostart entry

`
mkdir -p ~/.config/autostart

nano ~/.config/autostart/monitor_tray.desktop
`

Paste:

`
[Desktop Entry]

Type=Application

Exec=/usr/local/bin/tray_monitor_control.py

Hidden=false

NoDisplay=false

X-GNOME-Autostart-enabled=true

Name=Monitor Control Tray
`

You will now see a monitor icon in your system tray with a context menu:

- Turn Off Monitors

- Turn On Monitors

- Quit
