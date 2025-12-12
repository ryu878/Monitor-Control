#!/usr/bin/env python3

import sys
import subprocess
from PyQt5 import QtWidgets, QtGui


MONITORS_OFF = ["DP-4", "HDMI-0"]
MONITORS_ON = ["DP-4", "HDMI-0"]


def run_cmd(cmd):
    subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def turn_off():
    for m in MONITORS_OFF:
        run_cmd(["xrandr", "--output", m, "--off"])


def turn_on():
    for m in MONITORS_ON:
        run_cmd(["xrandr", "--output", m, "--auto"])


class TrayApp(QtWidgets.QSystemTrayIcon):
    def __init__(self):
        super().__init__()

        self.setIcon(QtGui.QIcon.fromTheme("video-display"))
        self.setToolTip("Monitor Control")

        menu = QtWidgets.QMenu()

        off_action = menu.addAction("Turn Off Monitors")
        off_action.triggered.connect(turn_off)

        on_action = menu.addAction("Turn On Monitors")
        on_action.triggered.connect(turn_on)

        menu.addSeparator()

        quit_action = menu.addAction("Quit")
        quit_action.triggered.connect(QtWidgets.qApp.quit)

        self.setContextMenu(menu)
        self.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    tray = TrayApp()
    sys.exit(app.exec_())