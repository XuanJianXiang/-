# _*_ coding:utf-8 _*_
# 开发团队：宣建祥
# 开发人员：xuanjianxiang
# 开发时间：2022/4/29 12:32
# 文件名称：罚息.py
# 开发工具：PyCharm
import time
import pyautogui
pyautogui.PAUSE = 0.2
pyautogui.FAILSAFE = True
i = 0
while i<10:
    pyautogui.moveTo(100,50)
    pyautogui.leftClick()
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.moveTo(660,180)
    time.sleep(0.2)
    pyautogui.leftClick()
    pyautogui.moveTo(370,485)
    time.sleep(0.2)
    pyautogui.leftClick()
    pyautogui.press("space")
    pyautogui.moveTo(360,640)
    pyautogui.leftClick()
    pyautogui.moveTo(555,50)
    pyautogui.leftClick()
    i+=1