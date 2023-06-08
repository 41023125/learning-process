import random

types = ['充電', '聖劍', '小丑', '月亮', '雪球']  # 骰子種類
counts = [0, 0, 0, 0, 0]
result = [['小丑1', '小丑1', '小丑1', '小丑1', '充電1']
            ,['小丑1', '小丑1', '小丑1', '小丑1', '小丑1']
            ,['雪球1', '聖劍1', '月亮1', '小丑1', '小丑1']]  # 版面陣列

game = True  # 遊戲開關

game_data = []  # 數據收集列表


def init():
    """
    初始隨機產生版面
    """
    global result
    result = []
    for _ in range(3):
        temp = [random.choice(types) + str(1) for _ in range(5)]
        result.append(temp)


def amount():
    """
    檢查每種數量
    """
    global counts
    counts = [0, 0, 0, 0, 0]
    for arr in result:
        for candy in arr:
            for i, t in enumerate(types):
                if t in candy:
                    counts[i] += 1


def stop():
    """
    檢查遊戲是否結束
    """
    all_positive = False  # 檢查每種是否都存在
    for count in counts:
        if count <= 0:
            all_positive = True
            break

    if counts[0] > 2 or counts[3] > 4 or counts[4] > 1:  # 充聖丑月雪
        all_positive = True

    if all_positive:
        return False

    moon = False  # 檢查月亮位置
    positions = [(0, 2), (1, 0), (1, 4), (2, 2)]
    target_types = ['小丑', '月亮']
    for pos in positions:
        row, col = pos
        candy = result[row][col]
        for t in target_types:
            if t in candy:
                break
        else:
            moon = True
            break

    if moon:
        return False

    found = False  # 檢查其他地方是否有月亮
    target_type = '月亮'
    for row in range(len(result)):
        for col in range(len(result[row])):
            if (row, col) not in positions:
                candy = result[row][col]
                if target_type in candy:
                    found = True
                    break
        if found:
            break

    if found:
        return False

    position = (0, 0)  # 檢查充電位置
    target_type = '充電'
    row, col = position
    candy = result[row][col]
    if target_type in candy:
        return True

    return False


def collect_data(game_state, player_action):
    """
    收集遊戲數據
    """
    global game_data
    game_state_str = '['
    for row in game_state:
        row_str = '[' + ', '.join([f"'{element}'" for element in row]) + ']'
        game_state_str += row_str + ', '
    game_state_str = game_state_str.rstrip(', ') + ']'
    game_data.append(f"{game_state_str},{player_action}\n")




def main():
    global game
    #init()
    amount()
    print("///////////////////開始遊戲///////////////")
    while game:
        for arr in result:
            print(" ".join(arr))
        amount()
        if stop():
            print("通關!!!!!!!!")
            game = False
            break
        while game:
            input_str = input("請輸入四個數字：")
            if len(input_str) == 4 and input_str.isdigit():
                x1, y1, x2, y2 = map(int, input_str)
                if (
                    0 <= x1 <= 2
                    and 0 <= x2 <= 2
                    and 0 <= y1 <= 4
                    and 0 <= y2 <= 4
                    and (x1, y1) != (x2, y2)
                ):
                    string1 = result[x1][y1]
                    string2 = result[x2][y2]
                    number1 = str(int(string1[2:]) + 1)
                    number2 = str(int(string2[2:]) + 1)
                    if number1 == number2:
                        if "小丑" in result[x1][y1] and "小丑" not in result[x2][y2]:
                            result[x1][y1] = result[x2][y2]
                            collect_data(str(result), f"{x1},{y1},{x2},{y2}")
                            break
                        else:
                            if result[x1][y1] == result[x2][y2]:
                                result[x2][y2] = random.choice(types) + number1
                                result[x1][y1] = random.choice(types) + str(1)
                                collect_data(str(result), f"{x1},{y1},{x2},{y2}")
                                break
                            else:
                                print("合成錯誤，請重新輸入。")
                    else:
                        print("後面的數字不相同請重新輸入")
                else:
                    print("重複位置，請重新輸入。")
            else:
                print("輸入的格式不正確，請重新輸入。")
        

    print("遊戲結束")

    # 儲存遊戲數據到文件
    with open("RDgame/game_data.txt", "w", encoding="utf-8") as file:
        file.writelines(game_data)



main()
