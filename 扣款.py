import time
import pyautogui
pyautogui.PAUSE = 0.2
pyautogui.FAILSAFE = True
i = 0
while i<200:
    pyautogui.moveTo(100,50)
    pyautogui.leftClick()
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.moveTo(370,410)
    time.sleep(0.2)
    pyautogui.leftClick()
    pyautogui.moveTo(370,650)
    time.sleep(0.2)
    pyautogui.leftClick()
    pyautogui.moveTo(555,50)
    time.sleep(0.2)
    pyautogui.leftClick()
    i+=1













