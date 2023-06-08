# pylint: disable=no-member
"""
此注釋用來禁用警告
"""
# 計算全部種類只用一次
import os
import numpy as np
import cv2
import time
from concurrent import futures
# 查看圖片
def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print("程式運行時間：{:.2f}秒".format(end_time - start_time))
        return result
    return wrapper

def look(aimage):
    """
    用來查看圖片
    :aimage: 選擇顯示的圖片

    """
    cv2.imshow("Cropped Image", aimage)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def pag(aimage, start_x, start_y):
    """
    用來裁剪圖片成指定大小
    :aimage: 選擇的圖片
    :start_x:起始X座標
    :start_y:起始y座標
    """
    end_x = 95
    end_y = 95
    return aimage[start_y:start_y+end_y, start_x:start_x+end_x]


def mse(image1, image2):
    """
    比較兩張圖片相似度
    返回百分比
    """
    err = np.sum((image1.astype("float") - image2.astype("float")) ** 2)
    err /= float(image1.shape[0] * image1.shape[1])
    if err == 0:
        return 100.0
    else:
        psnr = 10 * np.log10(255**2 / err)
        similarity = (psnr / 50) * 100
        return similarity


def read_file(num):
    """
    返回數字在文本對應的內容
    """
    mapping = {}
    with open("dictionary.txt", 'r', encoding='utf-8') as f:
        # 读取文件内容
        lines = f.readlines()
        for line in lines:
            parts = line.split()
            if len(parts) == 2:
                key = int(parts[0])
                value = parts[1]
                mapping[key] = value
    if num in mapping:
        return mapping[num]
    else:
        print('未在dictionary.txt增新'+str(num)+"對應名稱")
        return


def count_files():
    """
    返回圖庫的檔案數量
    """
    folder_path = "jpg"
    files = os.listdir(folder_path)
    return len(files)


def check(image1):
    """
    比較圖庫所有內容並返回最相近的名稱
    if mes < 30:
            # 儲存圖片
            cv2.imwrite('jpg/'+str((count_files()))+".png", image1)
            with open("ph\\dictionary.txt", 'a', encoding='utf-8') as f:
                count = int(count_files()) - 1
                f.write(str(count) + '    '+read_file(ass)+'\n')
            # print(count)
        # 顯示圖片
        look(image1)
    """
    mes = aass = 0
    for i in range(0, count_files()):
        image2 = cv2.imread("jpg\\" + str(i) + ".png")
        # print("相似度: ", mse(image1, image2), "%")
        if mse(image1, image2) >50:
            mes = mse(image1, image2)
            aass = i
            break
        if mes < mse(image1, image2):
            mes = mse(image1, image2)
            aass = i
    # print(aass)
    aass = read_file(aass)
    # print(mes)
    return aass


# 將陣列展示
def output(my_array):
    """
    將陣列合成字串並返回用於展示
    """
    aoutput = ''
    for _, row in enumerate(my_array):
        for _, value in enumerate(row):
            aoutput += str(value) + ' '
        aoutput += '\n'
    return aoutput

# 檢查全部

_='''單線程棄用
@timer
def check_all(aimage):
    """
    檢查全部的圖片並返回成陣列
    單片檢查
    image1 = pag(image, addx+(9+95)*0, addy-(5+95)*2)
    look(image1)
    """
    addx = 195
    addy = 1090
    # x 9 # y 5 # addx = 195 # addy = 1010
    # 创建一个3x5的空二维數组
    my_array = [[0 for j in range(5)] for i in range(3)]
    for xx in range(5):
        for yy in range(3):
            image1 = pag(aimage, addx+(9+95)*xx, addy-(5+95)*yy)
            my_array[yy][xx] = check(image1)
    my_array = my_array[::-1]
    outpu = output(my_array)
    print(outpu)
    return my_array
'''
@timer
def check_all(aimage):
    """
    檢查全部的圖片並返回成陣列
    單片檢查
    image1 = pag(image, addx+(9+95)*0, addy-(5+95)*2)
    look(image1)
    """
    addx = 195
    addy = 1090
    # x 9 # y 5 # addx = 195 # addy = 1010
    # 创建一个3x5的空二维數组
    my_array = [[0 for j in range(5)] for i in range(3)]
    futures_list = []
    with futures.ThreadPoolExecutor() as executor:
        for xx in range(5):
            for yy in range(3):
                image1 = pag(aimage, addx+(9+95)*xx, addy-(5+95)*yy)
                future = executor.submit(check, image1)
                futures_list.append((future, xx, yy))
        for f, xx, yy in sorted(futures_list, key=lambda x: (x[1], x[2])):
            my_array[yy][xx] = f.result()
    my_array = my_array[::-1]
    outpu = output(my_array)
    print(outpu)
    return my_array


# 測試
'''
JPG1 = "screenshot1.png"
image = cv2.imread(JPG1)
ass = check_all(image)
#print(ass)
'''