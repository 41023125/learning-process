
import imageio

# 設定輸入MP4檔案的路徑和輸出GIF檔案的路徑
input_path = ''
output_path = 'C:\\Users\\alin\\Downloads\\c8763.gif'

# 使用imageio庫讀取MP4檔案中的所有幀
with imageio.get_reader(input_path, 'ffmpeg') as reader:
    # 使用imageio庫創建一個GIF檔案寫入器
    with imageio.get_writer(output_path, mode='I', duration=0.1) as writer:
        # 將每一個幀轉換為GIF圖像並寫入GIF檔案
        for i, frame in enumerate(reader):
            if i % 2 != 0 and i != 7:
                writer.append_data(frame)
                print(f'已處理第{i+1}幀')
