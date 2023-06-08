import subprocess
from database import check_all
import cv2
from main import update,allpa
from check_move import *
import time
# 定義起始坐標和結束坐標
def movede(arr):
    """
    指定畫面滑動
    """
    # 執行adb命令
    cmd = f"adb shell input swipe {arr[0]} {arr[1]} {arr[2]} {arr[3]}"
    subprocess.call(cmd.split())

def xy(arr):
    """
    將骰子轉換成移動座標
    """
    ax = 250+100*arr[1]
    ay = 900+100*arr[0]
    az = 250+100*arr[3]
    af = 900+100*arr[2]
    dd = [ax,ay,az,af]
    return dd
#JPG1 = 
#image = cv2.imread("screenshot1.png")


while True :
    while True:
        #image = cv2.imread("screenshot1.png")
        image = update(3)
        ass = check_all(image)
        no = allpa(image)
        if no ==  0 :
            break
        subprocess.run("adb shell input tap 450 1300")
        time.sleep(1)
    xy_4 = check_key(ass)
    print(xy_4)
    flag = True
    while True:
        #print(xy_4)
        if flag == False :
            break
        else :
            if  xy_4 == []  :
                    print("好的出事")
                    flag = False  # 設置標誌變量為False
                    break
            else :
                xy_4_move = check_duplicate(xy_4[0],ass)
                while True:
                    if  xy_4 == []  :
                        print("壞的出事")
                        flag = False  # 設置標誌變量為False
                        break
                    else :
                        print(xy_4_move)
                        if xy_4_move == [] :
                            del xy_4[0]
                        else :
                            #print('xy_4[0]:'+xy_4[0])
                            ne = [xy_4[0][0],xy_4[0][1],xy_4_move[0][0],xy_4_move[0][1]]
                            #print(ne)
                            move = xy(ne)
                            #print(move)#[450, 1100, 650, 1100]
                            movede(move)
                            print("OK")
                            
                            break
        break
    if  flag == False : 
        xy_4 = check_key(ass)
        print(xy_4)
        break
    #movede(uu[0],uu[1],uu[2],uu[3])
   
   
    
    #time.sleep(2)


    