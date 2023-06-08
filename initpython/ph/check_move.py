from database import check_all
import cv2
import re

# 只跑指定的座標
def check_key(ass1):
    soc = []
    for x, y in [(0, 2), (1, 0), (1, 4), (2, 2)]:
        #print(ass1[x][y])
        pattern = r"(\D+)(\d+)"
        match = re.match(pattern, ass1[x][y])
        if match:
            name = match.group(1)
            if "月亮" not in name and "小丑" not in name:
                #print("OK") 
                soc.insert(0, (x,y,ass1[x][y]))
                pass
            else:
                #print("not")
                pass
    #print(soc)
    return(soc)




def check_duplicate(x1,ass1):
    """
    掃描(0, 2), (1, 0), (1, 4), (2, 2)以外的
    判斷移動位置
    x3[起始x,起始y,結束x,結束y,骰子名稱]
    """
    if x1[0] == -1 :
        x3 = [(-999,-999,-999,-999,-999)]
    else:
        x3 = [] 
        x2 = [-1,-1]
        for x in range(3):
            for y in range(5):
                if (x, y) not in [(0, 2), (1, 0), (1, 4), (2, 2)]:
                    if x1[2] == ass1[x][y]:
                        x2 = [x, y]
                        x3.insert(0, (x2[0], x2[1], x1[2]))       
    #num_elements = len(x3)
    #print(num_elements)
    #print(x3)
    return x3


def check_joker(num):
    soc = []
    for x, y in [(0, 1), (0, 2), (1, 0), (1, 4), (2, 2)]:
        name = "雪球" + str(num)
        if "小丑" in name:
            soc.append((x, y))
        else:
            pattern = r"(\D+)(\d+)"
            match = re.match(pattern, name)
            if match:
                name = match.group(1)
                if "月亮" not in name:
                    soc.append((x, y))
    if len(soc) > 0:
        return soc[0]
    else:
        return None



# 測試
JPG1 = "screenshot2.png"
image = cv2.imread(JPG1)
ass = check_all(image)

x = check_key(ass)
print(x)
'''
print(check_duplicate(x[0],ass))

xxx = check_duplicate(ass)

if xxx[2] == -999 :
    check_keycharge(ass)
    xxx = check_duplicate(x1,ass)
elif  xxx[2] == -1 :
    print("OK")'''