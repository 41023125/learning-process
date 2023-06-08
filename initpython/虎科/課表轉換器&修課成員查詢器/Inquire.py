"""查詢特定課堂學生"""
from selenium import webdriver
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
inselyr = '1121'
ineqno = '2713'
url = 'https://qry.nfu.edu.tw/studlist.php?selyr='+ inselyr +'&seqno=' + ineqno

# 建立Chrome選項物件
chrome_options = Options()

# 設定視窗不顯示
chrome_options.add_argument("--headless")

# 建立WebDriver物件
driver = webdriver.Chrome('chromedriver.exe', options=chrome_options)



# 加載網頁
driver.get(url)




# 等待伺服器回應
time.sleep(0.1)  # 暫停0.2秒
# 獲取回應內容
content = driver.page_source
soup = BeautifulSoup(content, "html.parser")
span_tags = soup.find_all(['tr'])
# 在這裡處理回應的內容
#print(span_tags[2:].get_text(separator=" ").strip())
text = ' '.join([tag.get_text(separator=" ") for tag in span_tags[2:]]).strip()
word_lists = text.split()
for word_list in word_lists:
    if "4" in word_list :
        print( word_list)

# 關閉瀏覽器
driver.quit()
