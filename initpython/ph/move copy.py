import subprocess
from database import check_all
import cv2
from main import update,allpa
from check_move import *
import time
from test_move2 import get_next_position
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
    #print(xy_4)
    #print(ass)
    pos_dict = get_next_position(ass)
    if pos_dict['first_pos'] is not None and pos_dict['second_pos'] is not None:
        print(f"合成：{ass[pos_dict['first_pos'][0]][pos_dict['first_pos'][1]]} + {ass[pos_dict['second_pos'][0]][pos_dict['second_pos'][1]]}")
        print(f"位置：{pos_dict['first_pos']}, {pos_dict['second_pos']}")
    else:
        print("找不到符合條件的位置")
    break
    #movede(uu[0],uu[1],uu[2],uu[3])
   
   
    
    #time.sleep(2)


    