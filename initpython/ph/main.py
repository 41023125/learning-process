import cv2

# 開啟夜神模擬器的視訊鏡頭
cap = cv2.VideoCapture(2)  # 使用編號0開啟第一個視訊鏡頭

# 持續讀取視訊鏡頭影像
while True:
    ret, frame = cap.read()  # 讀取一幀影像
    if ret:
        # 顯示影像
        cv2.imshow('Game Capture', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # 按下 'q' 鍵結束迴圈
        break

# 釋放資源
cap.release()
cv2.destroyAllWindows()
