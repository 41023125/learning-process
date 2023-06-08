from concurrent import futures
import cv2
from database import check,pag,output
from main import timer
from picture import predict_image 


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
            # print(check(image1))
            print(predict_image(image1))
            my_array[yy][xx] = predict_image(image1)
    my_array = my_array[::-1]
    outpu = output(my_array)
    print(outpu)
    return my_array

JPG1 = "screenshot2.png"
image = cv2.imread(JPG1,0)
ass = check_all(image)
'''
JPG1 = "screenshot2.png"
image = cv2.imread(JPG1,0)
image1 = pag(image, 195+(9+95)*0, 1090-(5+95)*0)
result = predict_image(image1)
print(result)
image = cv2.imread(JPG1)
image1 = pag(image, 195+(9+95)*0, 1090-(5+95)*0)
result = check(image1)
print(result)'''