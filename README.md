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

```bash
/usr/local/bin/tray_monitor_control.py
```

Make executable:

```bash
sudo chmod +x /usr/local/bin/tray_monitor_control.py
```

## Start the tray automatically on login

Create autostart entry

```bash
mkdir -p ~/.config/autostart
nano ~/.config/autostart/monitor_tray.desktop
```

Paste:

```bash
[Desktop Entry]
Type=Application
Exec=/usr/local/bin/tray_monitor_control.py
Hidden=false
NoDisplay=false
X-GNOME-Autostart-enabled=true
Name=Monitor Control Tray
```

You will now see a monitor icon in your system tray with a context menu:

- Turn Off Monitors
- Turn On Monitors
- Quit

# Notes

This script works on X11 sessions.
Check your session type:

```bash
echo $XDG_SESSION_TYPE
```


***

## 📞 Contact Me

I develop trading bots of any complexity, dashboards, and indicators for crypto exchanges, forex, and stocks. 🚀

To contact me, please send a message:

*   **Telegram:** [https://t.me/ryu8777](https://t.me/ryu8777) ✈️
*   **Discord:** [https://discord.gg/zSw58e9Uvf](https://discord.gg/zSw58e9Uvf) 🤝

***

## 🤝 Become My Crypto Partner

Start your trading journey on Bybit! Join using my referral link below:

**Join Bybit:** [https://www.bybit.com/invite?ref=P11NJW](https://www.bybit.com/invite?ref=P11NJW)

***

## 🖥️ VPS for Your Bots and Scripts

Keep your bots running 24/7! I prefer and recommend using **DigitalOcean**.

[![DigitalOcean Referral Badge](https://web-platforms.sfo2.digitaloceanspaces.com/WWW/Badge%202.svg)](https://www.digitalocean.com/?refcode=3d7f6e57bc04&utm_campaign=Referral_Invite&utm_medium=Referral_Program&utm_source=badge)

**Get $200 in credit over 60 days** by using my referral link:

👉 [https://m.do.co/c/3d7f6e57bc04](https://m.do.co/c/3d7f6e57bc04)

