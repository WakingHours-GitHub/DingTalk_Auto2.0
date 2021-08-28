import pyautogui
import random
import time
import os

# 定义全局变量:
root_path = os.path.abspath('.') + '\\picture\\'


def program():
    while True:
        try:
            pyautogui.doubleClick(pyautogui.center(pyautogui.locateOnScreen(root_path+'dingtalk.png', confidence=0.9)))
            break
        except TypeError:
            print('未找到[钉钉]图标')




if __name__ == "__main__":
    
    pyautogui.alert('''
        Hey,bro: 
    这是一个钉钉的自动签到程序, 当点击[确定]的时候
    该自动程序将会开始执行
    ''') # 返回OK
    print(root_path)
    # pyautogui.hotkey('winleft', 'd') # 快捷键,返回桌面

    program()