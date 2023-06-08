import requests
from bs4 import BeautifulSoup
import os
path = "./123 "
if not os.path.isdir(path):
    os.makedirs(path) #創建資料夾
web = requests.get(
    'https://danbooru.donmai.us/posts?page=17&tags=misaka_mikoto+')
soup = BeautifulSoup(web.text, "html.parser")
titles = soup.find_all("a", class_="post-preview-link")
name = 0  # 設定圖片編號
for i in titles:
    web2 = requests.get("https://danbooru.donmai.us/"+i.get('href'))
    soup2 = BeautifulSoup(web2.text, "html.parser")
    imgs = soup2.find_all('img')
    # https://www.delftstack.com/zh-tw/howto/python/python-string-contains-word/
    for x in imgs:
        # https://steam.oxxostudio.tw/category/python/spider/ptt-beauty.html
        if "jpg" in x['src']:
            print(x['src'])
            jpg = requests.get(x['src'])     # 使用 requests 讀取圖片網址，取得圖片編碼
            # 使用 open 設定以二進位格式寫入圖片檔案
            f = open(
                f'C:/initpython/123/test_{name}.jpg', 'wb')
            f.write(jpg.content)   # 寫入圖片的 content
            f.close()              # 寫入完成後關閉圖片檔案
            name = name + 1
