# https://www.youtube.com/watch?v=IMOUf4BYTG8&t=440s&ab_channel=%E5%BD%AD%E5%BD%AD%E7%9A%84%E8%AA%B2%E7%A8%8B
# 抓取原始碼
import bs4
import urllib.request as req
url = "https://www.ptt.cc/bbs/movie/index.html"
request = req.Request(url, headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
})
with req.urlopen(request) as response:
    data = response.read().decode("utf-8")
# 解析原始碼
root = bs4.BeautifulSoup(data, "html.parser")
titles = root.find_all("div", class_="title")  # 尋找所有 class_="title" 的 div 標籤
for title in titles:
    if title.a != None:
        print(title.a.string)
