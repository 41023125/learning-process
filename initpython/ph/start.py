# pylint: disable=no-member
"""
此注釋用來禁用警告
"""
# 檢查造骰按鈕狀態
import numpy as np
import cv2


def pushbutton(aimage):
    """
    檢查按鈕狀態
    """
    addx = 195
    addy = 1090
    aimage1 = pag(aimage, addx+(9+95)*2, addy-(5+95)*-2)
    aimage1 = check(aimage1)
    return aimage1


def pag(aimage, start_x, start_y):
    """
    裁剪圖片
    """
    end_x = 95
    end_y = 20
    return aimage[start_y:start_y+end_y, start_x:start_x+end_x]


def mse(image1, image2):
    """
    比對兩張圖片相似度
    """
    err = np.sum((image1.astype("float") - image2.astype("float")) ** 2)
    err /= float(image1.shape[0] * image1.shape[1])
    if err == 0:
        return 100.0
    else:
        psnr = 10 * np.log10(255**2 / err)
        similarity = (psnr / 50) * 100
        return similarity


def check(image1):
    """
    返回對應狀態
    """
    mes = ass = 0
    for i in range(1, 4):
        if i == 1:
            x = "open"
        elif i == 2:
            x = "closure"
        else:
            x = "error"
        image2 = cv2.imread("summon\\" + x + ".png")
        # print("相似度: ", mse(image1, image2), "%")
        if mes < mse(image1, image2):
            mes = mse(image1, image2)
            ass = x
    _ = '''
    #檢查圖片
    from database import look
    look(image1)'''

    return (ass)

'''
# 測試
JPG1 = "screenshot1.png"
image = cv2.imread(JPG1)
print(pushbutton(image))
'''