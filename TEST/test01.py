from types import TracebackType

from cv2 import BackgroundSubtractorKNN
import pyautogui
import random
import time
import os

# 定义全局变量:
root_path = os.path.abspath('.') + '\\picture\\'

def sign_in():
    count = 0
    pyautogui.scroll(-100)
    # 点击高校数据，鼠标停留在界面内

    while True:
        try:
            pyautogui.moveTo(pyautogui.center(pyautogui.locateOnScreen(root_path+'yitianxie.png',confidence = 0.8))) 
            print('已找到结尾')
            while True:
                try:
                    pyautogui.moveTo(pyautogui.center(pyautogui.locateOnScreen(root_path+'wanchengqingkunag.png',confidence = 0.8))) #黑龙江健康上报
                    break
                except TypeError:
                    print('未找到[完成情况],继续向上滚动')
                    pyautogui.scroll(100) #向下滚动

            break
        except TypeError:
            print('没有找到[已填写]，继续向下滚动')
            pyautogui.scroll(-100) #向下滚动
            time.sleep(0.2)
            try:
                pyautogui.click(pyautogui.center(pyautogui.locateOnScreen(root_path+'jiazaigengduo.png',confidence = 0.8))) 
            except TypeError:
                print('没有找到[加载更多]，继续向下滚动')
                pyautogui.scroll(-100) #向下滚动
                time.sleep(0.2)
            


    

    time.sleep(0.5)

    first_x, first_y = pyautogui.center(pyautogui.locateOnScreen(root_path+'daitianxie.png', confidence = 0.8))
    width, hight = first_x, first_y

    while True:
        first_x = width
        while first_x <= (width + 3 * 150):
            pyautogui.moveTo(first_x, first_y) #先点击最左侧第一个
            count += 1
            if count == 16:
                count = 1
                pyautogui.scroll(-160) #向下滚动

            first_x += 150
        first_y += 85
    

def main_program():
    flag = 1
    while flag == 1:
        try:
            pyautogui.doubleClick(pyautogui.center(pyautogui.locateOnScreen(root_path+'dingtalk.png', confidence = 0.8)))
            flag += 1
        except TypeError:
            print('未找到[钉钉]图标')
    while flag == 2:
        try:
            pyautogui.doubleClick(pyautogui.center(pyautogui.locateOnScreen(root_path+'gongzuotai.png', confidence=0.9)))
            flag += 1
        except TypeError:
            print('未找到[工作台]图标')
    while flag == 3:
        try:
            pyautogui.click(pyautogui.center(pyautogui.locateOnScreen(root_path+'heilongjianggaoxiao.png', confidence = 0.9)))
            flag += 1
        except TypeError:
            print('未找到[高校数据]')

    # 进入到签到部分：
    sign_in()
    

        




if __name__ == "__main__":
    
    pyautogui.alert('''
        Hey,bro: 
    这是一个钉钉的自动签到程序, 当点击[确定]的时候
    该自动程序将会开始执行
    ''') # 返回OK
    print(root_path)
    # pyautogui.hotkey('winleft', 'd') # 快捷键,返回桌面

    # main_program()
    sign_in()