def get_best_merge(arr):
    merge_candidates = {}
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            key = arr[i][j]
            if key not in merge_candidates:
                merge_candidates[key] = []
            merge_candidates[key].append((i, j))

    best_merge = None
    max_score = -1

    for key, values in merge_candidates.items():
        for i in range(len(values)):
            for j in range(i + 1, len(values)):
                score = abs(values[i][0] - values[j][0])
                if key == "小丑1":
                    score = 0  # 小丑的合成位置分數設為0，使其優先合成
                if score > max_score:
                    max_score = score
                    best_merge = (values[i], values[j])

    return best_merge

# 二維陣列
arr = [["充電1", "月亮2", "月亮1", "聖劍1", "充電1"],
       ["充電1", "小丑1", "充電1", "月亮1", "充電1"],
       ["聖劍1", "月亮1", "小丑1", "月亮1", "月亮1"]]

# 判斷最佳合成位置
best_merge = get_best_merge(arr)
if best_merge:
    print("最佳合成位置：", best_merge)
    # print(best_merge[0][0])
    print(arr[best_merge[0][0]][best_merge[0][1]])
    print(arr[best_merge[1][0]][best_merge[1][1]])
else:
    print("無合成位置")
