import pyautogui
import time
while True:
    time.sleep(1)
    pyautogui.typewrite("hey world")
    time.sleep(0.5)
    pyautogui.press('enter')
