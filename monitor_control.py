#!/usr/bin/env python3
import subprocess
import sys
import re


def get_monitors():
    """
    Returns a list of connected monitors using xrandr.
    Output example:
        ["HDMI-1", "DP-1", "eDP-1"]
    """
    result = subprocess.run(["xrandr"], capture_output=True, text=True)
    lines = result.stdout.splitlines()

    monitors = []
    for line in lines:
        # match: HDMI-1 connected, DP-1 connected, etc.
        match = re.match(r"^([A-Za-z0-9\-\_]+) connected", line)
        if match:
            monitors.append(match.group(1))

    return monitors


def turn_off(monitor):
    print(f"Turning OFF: {monitor}")
    subprocess.run(["xrandr", "--output", monitor, "--off"])


def turn_on(monitor, mode="auto"):
    print(f"Turning ON: {monitor}")
    if mode == "auto":
        # Auto-select resolution
        subprocess.run(["xrandr", "--output", monitor, "--auto"])
    else:
        # Set specific resolution
        subprocess.run(["xrandr", "--output", monitor, "--mode", mode])


def print_usage(monitors):
    print("Usage:")
    print("  python monitor_control.py list")
    print("  python monitor_control.py off <monitor_name>")
    print("  python monitor_control.py on <monitor_name> [resolution]")
    print("")
    print("Detected monitors:")
    for m in monitors:
        print(f"  {m}")
    print("")


if __name__ == "__main__":
    monitors = get_monitors()

    if len(sys.argv) < 2:
        print_usage(monitors)
        sys.exit(1)

    command = sys.argv[1]

    if command == "list":
        print("Connected monitors:")
        for m in monitors:
            print(m)
        sys.exit(0)

    if command == "off":
        if len(sys.argv) != 3:
            print("Error: please specify monitor name.")
            print_usage(monitors)
            sys.exit(1)

        mon = sys.argv[2]
        if mon not in monitors:
            print(f"Monitor '{mon}' not detected.")
            print_usage(monitors)
            sys.exit(1)

        turn_off(mon)
        sys.exit(0)

    if command == "on":
        if len(sys.argv) < 3:
            print("Error: please specify monitor name.")
            print_usage(monitors)
            sys.exit(1)

        mon = sys.argv[2]
        mode = sys.argv[3] if len(sys.argv) == 4 else "auto"

        turn_on(mon, mode)
        sys.exit(0)

    print("Unknown command.")
    print_usage(monitors)
    sys.exit(1)
