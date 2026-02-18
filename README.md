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

## 📌 Quantitative Researcher | Algorithmic Trader | Trading Systems Architect

Quantitative researcher and trading systems engineer with end-to-end ownership of systematic strategies — from research and statistical validation to low-latency execution and production deployment.

Core focus areas:
- Systematic strategy design and validation
- Market microstructure analysis (order book dynamics, volume, delta, liquidity, spread behavior)
- Backtesting framework development (tick-level and historical data)
- Execution engine architecture and order lifecycle management
- Real-time market data processing
- Risk-aware system design
- Production-grade trading infrastructure (24/7 environments)

Experience across crypto (CEX, DEX), FX, and exchange-traded markets.

## Technical Stack

- Languages: Python, C++, MQL5
- Execution & Connectivity: REST, WebSocket, FIX
- Infrastructure: Linux, Docker, Redis, PostgreSQL
- Analytics: NumPy, Pandas, custom backtesting frameworks

## Contact

Email: ryu8777@gmail.com

***

