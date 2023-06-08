import requests
from bs4 import BeautifulSoup
import os
path = "./123 "
if not os.path.isdir(path):
    os.makedirs(path)  # 創建資料夾
web = requests.get('https://www.instagram.com/p/Cng-nG4hG-w/')
soup = BeautifulSoup(web.text, "html.parser")
name = 0  # 設定圖片編號

asd = soup.find_all("script", type="application/ld+json")
for x in asd:
    b = x.string.split('"')
    for xd in b:
        if "jpg?" in xd:
            if "100x100" in xd:
                pass
            else:
                xdf = xd.replace("\/", "/")
                jpg = requests.get(xdf)
                f = open(
                    f'C:/initpython/123/test_{name}.jpg', 'wb')
                f.write(jpg.content)   # 寫入圖片的 content
                f.close()              # 寫入完成後關閉圖片檔案
                name = name + 1
