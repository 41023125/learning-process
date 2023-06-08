import cv2
import pytesseract

# 加载测试图像
image = cv2.imread('path/to/test/image')

# 将图像转换为灰度图像
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 使用 pytesseract 库从图像中提取文本信息
text = pytesseract.image_to_string(gray_image, config='--psm 13')

# 打印提取的文本信息
print(f"The extracted text is: {text}")
