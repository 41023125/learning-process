# pylint: disable=no-member
"""
此注釋用來禁用警告
"""
# 測試圖片
import cv2
from database import look
from main import update


def pag(aimage):
    """"
    裁剪圖片
    """
    addx = 195
    addy = 1090
    start_x = addx+(9+95)*0
    start_y = addy-(5+95)*2
    end_x = (9+95)*4+95
    end_y = 95+(5+95)*2
    return aimage[start_y:start_y+end_y, start_x:start_x+end_x]


# 測試
# 用實戰要改成1010
# 訓練場1090
image = update(3)
#JPG1 = "screenshot1.png"
#image = cv2.imread(JPG1)
look(pag(image))
