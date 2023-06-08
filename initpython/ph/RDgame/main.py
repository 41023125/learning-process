import random
types =  ['充電', '聖劍', '小丑', '月亮', '雪球'] #骰子種類
counts = [0, 0, 0, 0, 0]
result =    [] #版面陣列
"""
['充電1', '小丑1', '小丑1', '小丑1', '充電1']
            ,['小丑1', '小丑1', '小丑1', '小丑1', '小丑1']
            ,['雪球1', '聖劍1', '月亮1', '小丑1', '小丑1']
"""
game = False #遊戲開關

def init(): #初始隨機產生版面
    for i in range(3):
        temp = []
        for j in range(5):
            temp.append(random.choice(types) + str(1))
        result.append(temp)
    '''
    for i, arr in enumerate(result):
        print(f"{' '.join(arr)}")
        # print(arr)
    '''   

def amount():#檢查每種數量
    global counts
    counts = [0,0,0,0,0]
    for arr in result:
        for candy in arr:
            for i, t in enumerate(types):
                if t in candy:
                    counts[i] += 1
    """#顯示數量
    for i, t in enumerate(types):
        print(f"{t}有{counts[i]}顆")
    """

def stop() :
    all_positive = False #檢查每種是否都存在
    # print(counts)
    for count in counts:
        if count <= 0:
            all_positive = True
            break 
    
    if counts[0]>2 or counts[3]>4 or counts[4]>1:#充聖丑月雪
        all_positive = True

    if all_positive == True:
        # print("沒有都存在")
        pass
    else:
        # print("有都存在")
        moon = False
        positions = [(0, 2), (1, 0), (1, 4), (2, 2)] #檢查月亮位置
        target_types = ['小丑', '月亮']
        for pos in positions:
            row, col = pos
            candy = result[row][col]
            for t in target_types:
                if t in candy:
                    #print(f"位置{pos}是{t}")
                    break
            else:
                # print(f"位置{pos}不是{target_types}")
                moon = True
                break
        if moon ==True :
            print("四位不正確")
        else :
            found = False #檢查其他地方是否有月亮
            target_type = '月亮' 
            for row in range(len(result)):
                for col in range(len(result[row])):
                    if (row, col) not in positions:
                        candy = result[row][col]
                        if target_type in candy:
                            found = True
                            # print(f"位置({row}, {col})是{target_type}")
                            break
                if found:
                    break
            if found ==True:
                # print("其他位置有月亮")
                pass
            else:
                # print(f"其他位置沒有月亮")
                position = (0, 0)
                arget_type = '充電'
                row, col = position
                candy = result[row][col]
                if arget_type in candy:
                    print(f"通關!!!!!!!!")
                    game = False
                    return game
                else:
                    # print(f"位置{position}不是{arget_type}")
                    pass
game = True
def main():
    global game
    init()
    amount()
    #print(counts)
    print("///////////////////開始遊戲///////////////") 
    while game != False:
        for i, arr in enumerate(result):
            print(f"{' '.join(arr)}") 
        amount()
        game  = stop() 
        while game != False:
            input_str = input("請輸入四個數字：")
            if len(input_str) == 4 and input_str.isdigit():
                x1, y1, x2, y2 = map(int, input_str)    
                if 0 <= x1 <= 2 and 0 <= x2 <= 2 and 0 <= y1 <= 4 and 0 <= y2 <= 4 and(x1,y1) != (x2,y2)  :
                    string1 = result[x1][y1]
                    string2 = result[x2][y2]  # 要取得的字串位置 (0, 1)
                    number1 = str(int(string1[2:])+1)  # 取得字串後面的數字部分
                    number2 = str(int(string2[2:])+1)
                    if number1 == number2:
                        # print("後面的數字相同")
                        if "小丑" in result[x1][y1] and "小丑" not in result[x2][y2]:
                            # print("字串包含'小丑'且另一個不是")
                            result[x1][y1] = result[x2][y2] 
                            break
                        else:
                            # print("字串不包含'小丑'或兩個都是小丑")
                            if result[x1][y1] == result[x2][y2]:
                                result[x2][y2] = random.choice(types) + number1
                                result[x1][y1] = random.choice(types) + str(1)
                                break
                            else :
                                print("合成錯誤，請重新輸入。")
                    else:
                        print("後面的數字不相同請重新輸入")    
                else:        
                    print("重複位置，請重新輸入。")        
            else:        
                print("輸入的格式不正確，請重新輸入。")
        # print("座標1：({}, {})".format(x1, y1) ,result[x1][y1])
        # print("座標2：({}, {})".format(x2, y2),result[x2][y2])
    print("遊戲結束")
#main()