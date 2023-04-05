var tipuesearch = {"pages": [{'title': 'About', 'text': '這裡將放置學習python的所有過程 \n 以便將來回憶與查詢 \n 網站網址: https://41023125.github.io/learning-process/content/index.html/ \n \n', 'tags': '', 'url': 'About.html'}, {'title': 'course', 'text': '這裡放置上課學的過程與知識 \n', 'tags': '', 'url': 'course.html'}, {'title': 'web page', 'text': '這裡放置 所學編寫網頁之知識 \n \n', 'tags': '', 'url': 'web page.html'}, {'title': '模板', 'text': '所使用模板 \n cmsimde.zip \n', 'tags': '', 'url': '模板.html'}, {'title': 'game', 'text': '學習用python製作遊戲 \n', 'tags': '', 'url': 'game.html'}, {'title': 'adb', 'text': '\n 學習利用python控制手機與模擬器', 'tags': '', 'url': 'adb.html'}, {'title': 'tel2023', 'text': 'labview程式: \n', 'tags': '', 'url': 'tel2023.html'}, {'title': '直線校正', 'text': '直線校正.zip \n \n 使用python編寫 \n 下方為程式碼 \n import tkinter as tk\n\n\nclass Application(tk.Frame):\n    def __init__(self, master=None):\n        super().__init__(master)\n        self.master = master\n        self.pack()\n        self.create_widgets()\n\n    def create_widgets(self):\n        self.input2_label = tk.Label(self, text="實際距離:")\n        self.input2_label.pack()\n        self.input2 = tk.Entry(self)\n        self.input2.pack()\n\n        self.input3_label = tk.Label(self, text="當前輪徑:")\n        self.input3_label.pack()\n        self.input3 = tk.Entry(self)\n        self.input3.pack()\n\n        self.submit_button = tk.Button(\n            self, text="計算", command=self.show_output)\n        self.submit_button.pack()\n\n        self.output_label = tk.Label(self, text="輪徑:")\n        self.output_label.pack()\n        self.output = tk.Label(self, text="")\n        self.output.pack()\n\n        self.quit_button = tk.Button(\n            self, text="Quit", command=self.master.quit)\n        self.quit_button.pack()\n\n    def show_output(self):\n        input2_value = self.input2.get()\n        input3_value = self.input3.get()\n\n        # 在這裡加上你的處理邏輯，將結果顯示在output的Label中\n        input2_value = float(self.input2.get())\n        input3_value = float(self.input3.get())\n        output_value = (input3_value * input2_value) / 1000\n        self.output.config(text=output_value)\n\n\nroot = tk.Tk()\napp = Application(master=root)\napp.mainloop()\n \n', 'tags': '', 'url': '直線校正.html'}, {'title': 'other', 'text': '放置其他零散物品 \n', 'tags': '', 'url': 'other.html'}, {'title': '建立倉儲', 'text': '進入github選擇new repository.png \n \n 填寫要建立的倉儲名稱 \n 並勾選 Add a README file後 \n 點選create repository進行建立 \n \n \n 進入建立的倉儲 \n 並點擊code選擇HTTPS or SSH複製連結 \n \n 開啟cmd \n 輸入git clone (複製的網址) \n (需先安裝好 git ) \n 倉儲的內容便會下載下來', 'tags': '', 'url': '建立倉儲.html'}, {'title': '設定Personal access tokens(碼牌)', 'text': '打開github帳號點選右上頭像並點選Settings 點選Developer settings 點選Personal access tokens 點選 Generate new token Note (任意) 打勾repo(第一個) 點選最下面的Generate token 複製產生出來的token 打開可攜系統 打開要設Personal access tokens的資料夾 點開.git(要開隱藏項目才看的到) 將裡面的congif拉到SciTE(球球) 將複製的字串貼在github.com的前面再加上@並存檔(CTRL+S) 這樣Personal access tokens就設定完成', 'tags': '', 'url': '設定Personal access tokens(碼牌).html'}, {'title': '可攜', 'text': '可攜模板.zip', 'tags': '', 'url': '可攜.html'}, {'title': 'key.py', 'text': '', 'tags': '', 'url': 'key.py.html'}, {'title': 'question', 'text': '所遇到的問題與解決方法 \n 上傳檔案太大', 'tags': '', 'url': 'question.html'}, {'title': '上傳檔案太大', 'text': '\n 取消commit \n 刪除過大的問題的文件 \n 改用雲端硬碟等方式 \n 重新commit', 'tags': '', 'url': '上傳檔案太大.html'}, {'title': '取消commit', 'text': 'git中如何取消 commit 操作 \n git reset --soft HEAD^ \n \n 這個命令將撤銷最後一個提交，但保留更改。如果您需要撤銷更多的提交，可以使用 HEAD~n \n 其中 n 是要撤銷的提交數量。例如，如果您要撤銷最後兩個提交，可以使用以下命令： \n git reset --soft HEAD~2 \n', 'tags': '', 'url': '取消commit.html'}]};