var tipuesearch = {"pages": [{'title': 'About', 'text': '這裡將放置學習python的所有過程 \n 以便將來回憶與查詢 \n 網站網址: https://41023125.github.io/learning-process/content/index.html/ \n \n', 'tags': '', 'url': 'About.html'}, {'title': 'course', 'text': '這裡放置上課學的過程與知識 \n', 'tags': '', 'url': 'course.html'}, {'title': 'web page', 'text': '這裡放置 所學編寫網頁之知識 \n \n', 'tags': '', 'url': 'web page.html'}, {'title': '模板', 'text': '所使用模板 \n cmsimde.zip \n', 'tags': '', 'url': '模板.html'}, {'title': 'game', 'text': '學習用python製作遊戲 \n', 'tags': '', 'url': 'game.html'}, {'title': 'adb', 'text': '\n 學習利用python控制手機與模擬器 \n 如何在 WIN10 安裝 Android ADB工具 \n 如何讓 NOX 夜神模擬器支援 ADB \n Android adb 基本用法教學 \n 可以使用 \n adb shell pm list packages | findstr dice\n \n 指令來查看當前顯示的應用程式的相關資訊，其中 mCurrentFocus 顯示目前的視窗和活動的應用程式包名和類名，mFocusedApp 顯示當前焦點的應用程式包名和進程 ID。可以在模擬器或設備上執行此指令，以獲得目標應用程式的包名和主活動。 \n 假設輸出了package:com.percent.royaldice \n 可以使用 \n adb shell monkey -p com.percent.royaldice -c android.intent.category.LAUNCHER 1 \n \n 打開程式 \n 使用 \n adb shell am force-stop com.percent.royaldice \n \n 關閉程式 \n \n', 'tags': '', 'url': 'adb.html'}, {'title': '列出設備上的應用程式', 'text': "from ppadb.client import Client\n \n# 建立 ADB 連線\nadb = Client(host='127.0.0.1', port=5037)\ndevice = adb.device('127.0.0.1:62001')\n \n# 取得所有已安裝應用程式列表\nresult = device.shell('pm list packages')\npackages = [line.strip()[8:] for line in result.split('\\n') if line.strip()]\n \n# 列出所有應用程式名稱\nfor package in packages:\n    print(package) \n", 'tags': '', 'url': '列出設備上的應用程式.html'}, {'title': '測試端口是否正常連接', 'text': 'import socket\n\n# 設置主機地址和端口號\nhost = \'127.0.0.1\'\nport = 62001\n\n# 創建套接字對象\nsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)\n\n# 嘗試連接主機和端口號\nresult = sock.connect_ex((host, port))\n\n# 檢查連接結果\nif result == 0:\nprint("端口連接成功！")\nelse:\nprint("端口連接失敗。")\n\n# 關閉套接字對象\nsock.close() \n \n', 'tags': '', 'url': '測試端口是否正常連接.html'}, {'title': '取得目前應用程式的包名稱和主活動', 'text': 'from ppadb.client import Client\n\n# 建立 ADB 連線\nadb = Client(host=\'127.0.0.1\', port=5037)\ndevice = adb.device(\'127.0.0.1:62001\')\n\n# 查詢目前應用程式的包名稱和主活動\noutput = device.shell(\'dumpsys window windows | grep -E "mCurrentFocus"\')\npackage_activity = output.split(\' \')[-1].split(\'/\')\npackage_name = package_activity[0]\nactivity_name = package_activity[1].strip()\n\n# 開啟應用程式\n#device.shell(f"am start -n {package_name}/{activity_name}") \n 輸出結果範例: \n com.percent.royaldice com.google.firebase.MessagingUnityPlayerActivity} \n 分別帶入後變成 \n \n package_name  =  \'com.percent.royaldice\' \n activity_name  =  \'com.google.firebase.MessagingUnityPlayerActivity\' \n 便能利用\n \n device .shell( f "am start -n  { package_name } / { activity_name } " ) \n 開啟想要開啟的程式 \n \n \n \n \n', 'tags': '', 'url': '取得目前應用程式的包名稱和主活動.html'}, {'title': '截圖', 'text': 'import subprocess\n\nsubprocess.run("adb shell screencap -p /sdcard/screenshot.png")\nsubprocess.run("adb pull /sdcard/screenshot.png .")\nsubprocess.run("adb shell rm /sdcard/screenshot.png") \n \n', 'tags': '', 'url': '截圖.html'}, {'title': '點擊', 'text': "\n \n import subprocess\n\n\ndef click(x, y):\n\xa0 \xa0 subprocess.run(['adb', 'shell', f'input tap {x} {y}'])\n\n\nclick(500, 500) \xa0# 點擊座標 (500, 500)\n \n \n", 'tags': '', 'url': '點擊.html'}, {'title': 'tel2023', 'text': 'labview程式: \n \n', 'tags': '', 'url': 'tel2023.html'}, {'title': '直線校正', 'text': '直線校正.zip \n \n 使用python編寫 \n 下方為程式碼 \n import tkinter as tk\n\n\nclass Application(tk.Frame):\n    def __init__(self, master=None):\n        super().__init__(master)\n        self.master = master\n        self.pack()\n        self.create_widgets()\n\n    def create_widgets(self):\n        self.input2_label = tk.Label(self, text="實際距離:")\n        self.input2_label.pack()\n        self.input2 = tk.Entry(self)\n        self.input2.pack()\n\n        self.input3_label = tk.Label(self, text="當前輪徑:")\n        self.input3_label.pack()\n        self.input3 = tk.Entry(self)\n        self.input3.pack()\n\n        self.submit_button = tk.Button(\n            self, text="計算", command=self.show_output)\n        self.submit_button.pack()\n\n        self.output_label = tk.Label(self, text="輪徑:")\n        self.output_label.pack()\n        self.output = tk.Label(self, text="")\n        self.output.pack()\n\n        self.quit_button = tk.Button(\n            self, text="Quit", command=self.master.quit)\n        self.quit_button.pack()\n\n    def show_output(self):\n        input2_value = self.input2.get()\n        input3_value = self.input3.get()\n\n        # 在這裡加上你的處理邏輯，將結果顯示在output的Label中\n        input2_value = float(self.input2.get())\n        input3_value = float(self.input3.get())\n        output_value = (input3_value * input2_value) / 1000\n        self.output.config(text=output_value)\n\n\nroot = tk.Tk()\napp = Application(master=root)\napp.mainloop()\n \n \n', 'tags': '', 'url': '直線校正.html'}, {'title': 'other', 'text': '放置其他零散物品 \n', 'tags': '', 'url': 'other.html'}, {'title': '建立倉儲', 'text': '進入github選擇new repository.png \n \n 填寫要建立的倉儲名稱 \n 並勾選 Add a README file後 \n 點選create repository進行建立 \n \n \n 進入建立的倉儲 \n 並點擊code選擇HTTPS or SSH複製連結 \n \n 開啟cmd \n 輸入git clone (複製的網址) \n (需先安裝好 git ) \n 倉儲的內容便會下載下來 \n', 'tags': '', 'url': '建立倉儲.html'}, {'title': '設定Personal access tokens(碼牌)', 'text': '打開github帳號點選右上頭像並點選Settings 點選Developer settings 點選Personal access tokens 點選 Generate new token Note (任意) 打勾repo(第一個) 點選最下面的Generate token 複製產生出來的token 打開可攜系統 打開要設Personal access tokens的資料夾 點開.git(要開隱藏項目才看的到) 將裡面的congif拉到SciTE(球球) 將複製的字串貼在github.com的前面再加上@並存檔(CTRL+S) 這樣Personal access tokens就設定完成 \n', 'tags': '', 'url': '設定Personal access tokens(碼牌).html'}, {'title': '可攜', 'text': '可攜模板.zip \n', 'tags': '', 'url': '可攜.html'}, {'title': 'key.py', 'text': 'key.py \n key.bat \n 將上方檔案放入倉儲內部 \n 並將碼牌放入特定txt檔後 \n 將txt位置放入key.py裡面 \n 需要時只需要輸入key便可以快速輸入碼牌 \n \n \n', 'tags': '', 'url': 'key.py.html'}, {'title': 'question', 'text': '所遇到的問題與解決方法 \n 上傳檔案太大 \n', 'tags': '', 'url': 'question.html'}, {'title': '上傳檔案太大', 'text': '\n 取消commit \n 刪除過大的問題的文件 \n 改用雲端硬碟等方式 \n 重新commit \n', 'tags': '', 'url': '上傳檔案太大.html'}, {'title': '取消commit', 'text': 'git中如何取消 commit 操作 \n git reset --soft HEAD^ \n \n 這個命令將撤銷最後一個提交，但保留更改。如果您需要撤銷更多的提交，可以使用 HEAD~n \n 其中 n 是要撤銷的提交數量。例如，如果您要撤銷最後兩個提交，可以使用以下命令： \n git reset --soft HEAD~2', 'tags': '', 'url': '取消commit.html'}]};