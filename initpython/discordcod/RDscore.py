from PIL import Image
import pytesseract
def RDscore(picture,size):
    # 設定第一個位置的圖片路徑和位置
    if size == (900, 1600) :
        x1 = 189
        y1 = 1328
        w1 = 105
        h1 = 40
        x2 = 438
        y2 = 1335
        w2 = 50
        h2 = 50
    elif size == (1170, 2532) :    
        x1 = 230
        y1 = 1950
        w1 = 160
        h1 = 45
        x2 = 552
        y2 = 1960
        w2 = 93
        h2 = 45
    else :
        score = -1
        return score
    score = []
    # 讀取圖片並裁剪出第一個位置的區域
    img1 = Image.open(
        picture)
    crop_img1 = img1.crop((x1, y1, x1+w1, y1+h1))

    # 顯示裁剪出的第一個位置的區域
    # crop_img1.show()
    #sp
    #儲存圖片
    crop_img1.save('cropped_image1.png')

    # 將裁剪出的第一個位置的區域轉換為灰度圖
    gray_img1 = crop_img1.convert('L')

    # 將灰度圖像傳遞給pytesseract庫進行字符識別
    text1 = pytesseract.image_to_string(gray_img1, config='--psm 10')

    # 提取識別出的數字
    numbers1 = []
    for char in text1:
        if char.isdigit():
            numbers1.append(char)

    # 將識別出的數字轉換為字符串並連接起來
    result1 = ''.join([str(num) for num in numbers1])
    print(result1)
    score.append(result1)
    # 設定第二個位置的圖片路徑和位置
   
    #召喚所需
    # 讀取圖片並裁剪出第二個位置的區域
    crop_img2 = img1.crop((x2, y2, x2+w2, y2+h2))

    # 顯示裁剪出的第二個位置的區域
    # crop_img2.show()

    #儲存圖片
    crop_img2.save('cropped_image2.png')

    # 將裁剪出的第二個位置的區域轉換為灰度圖
    gray_img2 = crop_img2.convert('L')

    # 將灰度圖像傳遞給pytesseract庫進行字符識別
    text2 = pytesseract.image_to_string(gray_img2, config='--psm 10')

    # 提取識別出的數字
    numbers2 = []
    for char in text2:
        if char.isdigit():
            numbers2.append(char)

    # 將識別出的數字轉換為字符串並連接起來
    result2 = ''.join([str(num) for num in numbers2])
    print(result2)
    score.append(result2)
    total = 0
    num = 10

    while num <= int(result2):
        total += num
        num += 10
    print(total)
    total = total + int(result1)
    print(total)
    score.append(total) 
    return score

#測試
# print(RDscore("1234.jpg",(1170, 2532)))