import random

def get_next_position(arr):
    # 定義各個種類的數字初始值
    num_dict = {'充電': 0, '月亮': 0, '小丑': 0, '聖劍': 0, '雪球': 0}

    # 計算每個種類的數字
    for row in arr:
        for item in row:
            item_type = item.split()[0]
            if item_type in num_dict:
                num_dict[item_type] += 1
            else:
                print(f"Warning: {item_type} not in num_dict")

    # 確保聖劍、月亮、充電、雪球至少有一顆
    num_dict['聖劍'] = max(1, num_dict['聖劍'])
    num_dict['月亮'] = max(1, num_dict['月亮'])
    num_dict['充電'] = max(1, num_dict['充電'])
    num_dict['雪球'] = max(1, num_dict['雪球'])

    # 判斷小丑是否出現，若有則取代其中一個種類的數字最小者
    if num_dict['小丑'] > 0:
        min_num = min(num_dict.values())
        for key, value in num_dict.items():
            if value == min_num:
                num_dict[key] = num_dict['小丑']
                num_dict['小丑'] = 0
                break

    # 隨機選擇兩個種類進行合成
    types = list(num_dict.keys())
    first_type = random.choice(types)
    second_type = random.choice(types)

    # 找出兩個位置
    first_pos = None
    second_pos = None
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j].startswith(first_type):
                if first_pos is None:
                    first_pos = (i, j)
                elif second_pos is None:
                    second_pos = (i, j)
                    break
            elif arr[i][j].startswith(second_type):
                if first_pos is None:
                    first_pos = (i, j)
                elif second_pos is None:
                    second_pos = (i, j)
                    break

        if second_pos is not None:
            break

    # 如果兩個種類不同，則重新選擇
    while first_type != second_type or (first_type == second_type and int(arr[first_pos[0]][first_pos[1]].split()[1]) + int(arr[second_pos[0]][second_pos[1]].split()[1]) not in [2, 3, 4]):
        second_type = random.choice(types)
        second_pos = None
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                if arr[i][j].startswith(second_type):
                    if first_pos is None:
                        first_pos = (i, j)
                    elif second_pos is None:
                        second_pos = (i, j)
                        break

            if second_pos is not None:
                break

        if second_pos is not None:
            break

    return {'first_pos': first_pos, 'second_pos': second_pos}


# 測試用的二維陣列
arr = [['充電1', '月亮1', '月亮1', '聖劍1', '充電1'],
       ['充電1', '小丑1', '充電1', '月亮1', '充電1'],
       ['聖劍1', '月亮1', '小丑1', '月亮1', '月亮1']]

# 取得下一步合成的兩個位置

pos_dict = get_next_position(arr)
if pos_dict['first_pos'] is not None and pos_dict['second_pos'] is not None:
    print(f"合成：{arr[pos_dict['first_pos'][0]][pos_dict['first_pos'][1]]} + {arr[pos_dict['second_pos'][0]][pos_dict['second_pos'][1]]}")
    print(f"位置：{pos_dict['first_pos']}, {pos_dict['second_pos']}")
else:
    print("找不到符合條件的位置")
    ''''''