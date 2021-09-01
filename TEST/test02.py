import pyautogui
import time
import os

# 定义全局变量:
root_path = os.path.abspath('.') + '\\picture\\'
time.sleep(1)
while True:
    try:
        pyautogui.click(pyautogui.center(pyautogui.locateOnScreen(root_path+'jiazaigengduo.png',confidence = 0.8))) #打开钉钉
    except TypeError:
        print('没有找到加载，继续向下滚动')
        
        pyautogui.scroll(-100) #向下滚动

        time.sleep(0.2)