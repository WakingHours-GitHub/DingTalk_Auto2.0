import pyautogui
import random
import time
import os

# 定义全局变量:
root_path = os.path.abspath('.') + '\\picture\\'
errorFlag = 0 # 标记出现了[我知道了]

# 点击x号, 关闭界面
def clickX():
    while True:
        try:
            tx,ty = pyautogui.center(pyautogui.locateOnScreen(root_path+'OAgongzuotai.png',confidence=0.8))
            pyautogui.click(tx+370, ty)
            break
        except TypeError:
            print('未找到[OA标识],正在继续寻找')

def submit():
    global errorFlag
    time.sleep(0.2)
    while True:
        try:
            pyautogui.moveTo(pyautogui.center(pyautogui.locateOnScreen(root_path + 'heilongjiang.png',confidence=0.9)))
            break
        except:
            print('没有定位')
    
    overtime  = 1
    countFlag = 0 # 表示出现[我知道了]的次数
    
    while overtime <= 25:
        try:
            # pyautogui.moveTo(pyautogui.center(pyautogui.locateOnScreen(root_path + 'tijiao.png',confidence=0.9))) # 测试提交

            pyautogui.doubleClick(pyautogui.center(pyautogui.locateOnScreen(root_path + 'tijiao.png',confidence=0.9))) # 点击提交
            
            # 当操作速度过快时： 出现[我知道了]这个提示
            try:
                time.sleep(0.5)
                pyautogui.doubleClick(pyautogui.center(pyautogui.locateOnScreen(root_path+'wozhidaole.png',confidence=0.8))) #点击我知道了
                countFlag += 1 # 出现[我知道了]
                errorFlag = 1 # 标记, 如果出现了.则x,y都不变,继续点击这个块
            except: # 没出现[我知道了]
                countFlag = 0 # 归零
                break

            countFlag = 0 # 重置
                
        except: # 没有找到[提交]
            time.sleep(0.05)
            pyautogui.scroll(-200) # 滚动
            overtime += 1 # 累计加时
    if countFlag >= 25:
        countFlag = 1 # 重置
        print('没有找到[提交]，所以点击[X]继续下一步')

    time.sleep(0.2)

    clickX()
    
    time.sleep(0.2)

    if countFlag == 2:
        countFlag = 0 # 重置
        print('随机生成2~5s的延迟')
        time.sleep(random.randint(2,5))


def sign_in():
    global errorFlag # 声明全局变量
    count = 0
    pyautogui.scroll(-100)
    # 点击高校数据，鼠标停留在界面内

    # 浏览界面
    while True:
        try:
            pyautogui.moveTo(pyautogui.center(pyautogui.locateOnScreen(root_path+'yitianxie.png',confidence = 0.8))) # 已填写
            print('已找到结尾')
            while True:
                try:
                    pyautogui.moveTo(pyautogui.center(pyautogui.locateOnScreen(root_path+'wanchengqingkunag.png',confidence = 0.8))) # 我知道了
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
                pyautogui.click(pyautogui.center(pyautogui.locateOnScreen(root_path+'jiazaigengduo.png',confidence = 0.8))) # 加载更多
            except TypeError:
                print('没有找到[加载更多]，继续向下滚动')
                pyautogui.scroll(-100) #向下滚动
                time.sleep(0.2)
            


    

    time.sleep(0.2)

    first_x, first_y = pyautogui.center(pyautogui.locateOnScreen(root_path+'daitianxie.png', confidence = 0.8))
    width, hight = first_x, first_y

    while True:
        first_x = width
        while first_x <= (width + 3 * 150):
            errorFlag = 0 # 重置
            
            try:
                # pyautogui.moveTo(first_x, first_y) #先点击最左侧第一个
                pyautogui.doubleClick(first_x, first_y) #先点击最左侧第一个
            except:
                pyautogui.scroll(-100) # 若没有找到则向下滚动.
            

            # 点击进入提交界面
            submit()

            # 继续进行向下滚动，重新定位的操作
            # time.sleep(0.3)
            # 定位在框内，所以需要点击中间的定位
            while True:
                try:
                    pyautogui.moveTo(pyautogui.center(pyautogui.locateOnScreen(root_path+'daitianxie.png', confidence = 0.8)))
                    break
                except:
                    print('提交完未定位')

            count += 1 # 计数

            if count == 16:
                count = 1
                pyautogui.scroll(-100) #向下滚动
                first_y = hight

            if errorFlag == 1: # 如果出现了我知道了,表示该块没有提交
                continue
            
            first_x += 150

        if errorFlag == 1:
            continue

        first_y += 80
    

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