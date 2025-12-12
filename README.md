# Monitor Control
Python script that detects all connected monitors on Ubuntu (X11) and allows you to turn specific monitors off/on by name.


## Install requirements
`
sudo apt install python3-pyqt5
`

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
