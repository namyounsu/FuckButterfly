import ctypes
import os

import keyboard
import pyautogui


def check_admin_right():
    try:
        return os.getuid() == 0
    except AttributeError:
        return ctypes.windll.shell32.IsUserAnAdmin() != 0


def pressure_key():
    pyautogui.press('enter', interval=0.90)


def fuck_keyboard_events():
    print("----- Start FuckButterfly -----\n----- if press Enter, you doubled! -----")

    if check_admin_right():
        while True:
            if keyboard.is_pressed('enter'):
                pressure_key()
    else:
        print("----- Please Run Root -----")


def print_hi(name):
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


if __name__ == '__main__':
    #print_hi('PyCharm')
    fuck_keyboard_events()

