# https://www.youtube.com/watch?v=BEA7F9ExiPY&t=1313s&ab_channel=%E5%BD%AD%E5%BD%AD%E7%9A%84%E8%AA%B2%E7%A8%8B
# 抓取原始碼
import bs4
import urllib.request as req


def gatdata(url):
    request = req.Request(url, headers={
        "cookie": "_gat=1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
    # 解析原始碼
    root = bs4.BeautifulSoup(data, "html.parser")
    nextlink = root.find_all("div", class_="title")
    for titlle in nextlink:
        if titlle.a != None:
            print(titlle.a.string)
    nextlink = root.find("a", string="‹ 上頁")
    return nextlink["href"]


pageurl = "https://www.ptt.cc/bbs/movie/index.html"
count = 0
while count < 3:
    pageurl = "https://www.ptt.cc"+gatdata(pageurl)
    count += 1
