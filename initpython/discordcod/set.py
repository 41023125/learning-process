import cv2
import numpy as np

# 讀取輸入圖像和模板圖像
img = cv2.imread('1234.jpg')
template = cv2.imread('cropped_image1.png')

# 定義多個尺度比例
scales = [0.2, 0.4, 0.6, 0.8, 1.0]

# 定義閾值
threshold = 0.8

# 迭代不同比例下的模板匹配
for scale in scales:
    # 調整模板圖像的大小
    resized_template = cv2.resize(template, None, fx=scale, fy=scale)

    # 取得模板圖像的寬高
    h, w = resized_template.shape[:2]

    # 使用模板匹配算法進行匹配
    res = cv2.matchTemplate(img, resized_template, cv2.TM_CCOEFF_NORMED)

    # 取得匹配的位置
    loc = np.where(res >= threshold)

    # 畫出匹配的位置
    for pt in zip(*loc[::-1]):
        # 計算矩形框的大小
        rect_w = int(w * (1 / scale))
        rect_h = int(h * (1 / scale))

        # 計算矩形框的位置
        rect_x = int(pt[0] * (1 / scale))
        rect_y = int(pt[1] * (1 / scale))

        #測試框選
        # rect_w = 115
        # rect_h = 30
        # print((rect_w, rect_h))
        rect_x = 250
        # 繪製矩形框
        cv2.rectangle(img, (rect_x, rect_y), (rect_x + rect_w, rect_y + rect_h), (0, 0, 255), 2)
        # print((rect_x, rect_y))

# 顯示輸入圖像

cv2.imwrite('set.png', img)
