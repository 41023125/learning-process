"""查看修課成員"""
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
 
#設定只顯示特定學號 ''則不篩選
studentID = "410231"
 
# 讀取HTML文件
# #有驗證碼問題未解決無法使用爬蟲 暫時自行抓取
file_path = "課表.html"
with open(file_path, "r", encoding="utf-8") as file: 
    # "r"：讀取模式，用於讀取檔案的內容。
    # "w"：寫入模式，用於創建新的檔案或覆寫現有檔案的內容。
    # "a"：附加模式，用於在現有檔案的末尾添加內容。
    # "x"：獨佔創建模式，用於創建新的檔案，如果檔案已存在則引發錯誤。
    #讀取的內容儲存在 html_content 變數中
    html_content = file.read()  
 
# 创建Beautiful Soup对象
soup = BeautifulSoup(html_content, "html.parser") 
#使用 BeautifulSoup 庫來解析 HTML 內容並尋找所有符合條件的 <tr> 標籤
span_tags = soup.find_all(['tr'])
#allScheduletype分別儲存 課表種類,老師,教室,課號
allScheduletype = [],[],[],[] 
for tr_tag in span_tags:
    #尋找所有符合條件的 <td> 標籤
    td_tags = tr_tag.find_all('td')
    if len(td_tags) == 10:  
        course_name = td_tags[3].get_text(separator=" ").strip().replace("<br/>", "")
        
        #get_text() 方法用於提取指定元素的文字內容。在這裡，separator=" " 參數指定在文字內容中多個節點之間使用空格作為分隔符。
        #strip() 方法用於去除文字內容開頭和結尾的空格
        #replace("<br/>", "") 方法用於將文字內容中的 <br/> 標籤替換為空字串，即將它們從文字中移除。
         
        course_name = course_name.split()[0]  
        #將課表種類寫入
        allScheduletype[0].append(course_name) 
        #將對應課堂老師寫入
        allScheduletype[1].append(td_tags[7].get_text(separator=" ").strip()) 
        classroom = td_tags[8].get_text(separator=" ").strip()
        classroom = classroom.split()[0]  
        #將對應教室寫入
        allScheduletype[2].append(classroom)
        classroomNumber = td_tags[1].get_text(separator=" ").strip()
        classroomNumber = classroomNumber.split()[0]   
        #將對應課號寫入
        allScheduletype[3].append(classroomNumber)
 
#檢查課數
length = len(allScheduletype[3]) 
#依據課數建立陣列
my_array = [[] for _ in range(length)] 
 
import threading
#threading 模組提供了多執行緒編程的功能，允許在同一個程序中同時執行多個任務
def process_schedule(index):
    #獲取課號
    ineqno = allScheduletype[3][index]
    #根據課號獲取相對url
    url = 'https://qry.nfu.edu.tw/studlist.php?selyr=1121&seqno=' + ineqno 
 
    # 建立Chrome選項物件
    chrome_options = Options()
    # 設定視窗不顯示
    chrome_options.add_argument("--headless")
    # 建立WebDriver物件
    driver = webdriver.Chrome('chromedriver.exe', options=chrome_options)
 
    # 加載網頁
    driver.get(url)
 
  
    # 暫停0.2秒
    time.sleep(0.2)  
    # 獲取回應內容
    content = driver.page_source
    soup = BeautifulSoup(content, "html.parser") 
    #使用 BeautifulSoup 庫來解析 HTML 內容並尋找所有符合條件的 <tr> 標籤
    span_tags = soup.find_all(['tr'])
 
    # 在這裡處理回應的內容
    text = ' '.join([tag.get_text(separator=" ") for tag in span_tags[2:]]).strip()
    word_lists = text.split()
    for word_list in word_lists: 
        #查詢特定學號
        if studentID in word_list:   
            # 獲取鎖以避免多線程競爭
            lock.acquire()
            #寫入陣列
            my_array[index].append(word_list)   
            # 釋放鎖
            lock.release()
 
# 建立二維陣列
my_array = [[] for _ in range(len(allScheduletype[3]))]
# 建立鎖物件
lock = threading.Lock()
 
# 互斥鎖是一種同步機制，用於保護共享資源的訪問，以避免多個執行緒同時對其進行修改或訪問而導致不一致的結果。
# 在多執行緒環境中，如果多個執行緒同時試圖修改共享資源，可能會發生資源競爭 (race condition) 的情況。
# 使用互斥鎖可以確保在任何時候只有一個執行緒可以擁有該鎖，從而確保共享資源的安全訪問。
 
 
# 建立多個線程並執行任務
threads = []
for x in range(len(allScheduletype[3])):
    thread = threading.Thread(target=process_schedule, args=(x,))
    thread.start()
    threads.append(thread)
 
# 等待所有線程完成
for thread in threads:
    thread.join()
 
 
 
#all =[arr1, my_array[0], my_array[1], my_array[2], my_array[3], my_array[4], my_array[5], my_array[6],my_array[7],my_array[8],my_array[9],my_array[10]]
all = [['']] + [my_array[i] for i in range(length)]  #讓其根據選課數量做變化
# 將每個陣列作為一行資料儲存到DataFrame中
# DataFrame 的形狀（行數和列數）將取決於 all 中資料的結構和大小
df = pd.DataFrame(all)
 
# 轉置DataFrame，使每個陣列的元素作為一列
df = df.transpose()
allScheduletype[0].insert(0, '')
# 加入列標題
df.columns = allScheduletype[0]
 
#儲存DataFrame到Excel檔案，包含列標題和索引
file_path = "classmate.xlsx"
df.to_excel(file_path, index=False, header=True, sheet_name="3上")
with pd.ExcelWriter(file_path, engine='xlsxwriter') as writer:
    df.to_excel(writer, index=False, header=True, sheet_name="3上")
    worksheet = writer.sheets['3上']
 
    # 調整列寬
    for i in range(df.shape[1]):
        worksheet.set_column(i, i, width=44)
        worksheet.set_column(0, 0, width=7)
 
import subprocess
#開啟檔案
subprocess.Popen(['start', "classmate.xlsx"], shell=True)
''''''