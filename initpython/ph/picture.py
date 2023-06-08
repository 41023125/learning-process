import cv2
import numpy as np
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
"""
LeNet-5模型並使用GPU加速進行訓練和預測
並使用訓練好的模型進行預測
"""
# 設置GPU加速
gpus = tf.config.experimental.list_physical_devices('GPU')
if gpus:
    try:
        tf.config.experimental.set_virtual_device_configuration(
            gpus[0],
            [tf.config.experimental.VirtualDeviceConfiguration(memory_limit=1024)]
        )
    except RuntimeError as e:
        print(e)



def create_model():
    model = Sequential()
    model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(95, 95, 1)))
    model.add(MaxPooling2D((2, 2)))
    model.add(Conv2D(64, (3, 3), activation='relu'))
    model.add(MaxPooling2D((2, 2)))
    model.add(Conv2D(128, (3, 3), activation='relu'))
    model.add(MaxPooling2D((2, 2)))
    model.add(Flatten())
    model.add(Dense(128, activation='relu'))
    model.add(Dense(31, activation='softmax'))  # 將輸出層改為31個神經元
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    return model


# 訓練模型
def train_model():
    data = []
    labels = []
    label_map = {}
    with open("label_map.txt", "r", encoding="utf-8") as f:   
        for line in f:
            label, value = line.strip().split(":")
            label_map[label] = int(value)
    with open("C:/initpython/ph/dictionary.txt", "r", encoding="utf-8") as f:
        for line in f:
            filename, label = line.strip().split()
            img = cv2.imread(f"C:/initpython/ph/jpg/{filename}.png", 0)  # 讀取灰度圖像
            img = cv2.resize(img, (95, 95))  # 調整圖像大小
            data.append(img.reshape((95, 95, 1)))  # 將圖像數據轉換為3D數組
            if label in label_map:
                labels.append(label_map[label])  # 將答案添加到標籤列表中
            else:
                print(f"Invalid label: {label}. Skipping this data.")

    data = np.array(data)
    labels = np.array(labels)

    model = create_model()
    model.fit(data, labels, epochs=10, batch_size=32)

    return model

# 預測圖像
def predict_image(filename1, model):
    img = cv2.imread(filename1, 0)  # 讀取灰度圖像
    img = cv2.resize(img, (95, 95))  # 調整圖像大小
    data = img.reshape((1, 95, 95, 1))  # 將圖像數據轉換為4D數組

    prediction = model.predict(data)

    return np.argmax(prediction)

# 訓練模型
model = train_model()

# 預測圖像
result = predict_image("C:/initpython/ph/jpg/2.png", model)
print(f"This image belongs to class {result}.")