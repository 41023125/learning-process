import cv2
import re
from database import check_all
jpg1 = "screenshot2.png"
image = cv2.imread(jpg1)
ass = check_all(image)

pattern = r"(\D+)(\d+)"
count_sword = 0
count_charge = 0
count_snowball = 0
count_moon = 0
for row in ass:
    for item in row:
        match = re.match(pattern, item)
        if match:
            name = match.group(1)
            if "聖劍" in name:
                count_sword += 1
            elif "充電" in name:
                count_charge += 1
            elif "雪球" in name:
                count_snowball += 1
            elif "月亮" in name:
                count_moon += 1

# 輸出結果
print(f"聖劍出現了{count_sword}次")
print(f"充電出現了{count_charge}次")
print(f"雪球出現了{count_snowball}次")
print(f"月亮出現了{count_moon}次")
if count_snowball == 1:
    print("檢查雪球位置是否正確")
if count_snowball == 0:
    print("先不要管")
if count_sword == 1 or count_charge == 1 or count_moon == 1:
    print("確認位置")
    check_positions = [(0, 2), (1, 0), (1, 4), (2, 2)]
    for i in range(len(ass)):
        for j in range(len(ass[i])):
            # 如果當前元素包含"聖劍"，則檢查座標是否在指定的位置之一
            if "聖劍" in ass[i][j]:
                if (i, j) in check_positions:
                    print(f"聖劍出現在指定位置({i}, {j})")
                else:
                    print(f"聖劍出現在({i}, {j})，但不在指定位置之一")
