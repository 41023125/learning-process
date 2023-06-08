import requests
from bs4 import BeautifulSoup
import os
from tkinter import *
from tkinter import messagebox
import urllib.request


def check(asf1):
    path = './' + str(asf1)
    while os.path.isdir(path):
        asf1 += 1
        path = './' + str(asf1)
    os.makedirs(path)  # 創建資料夾
    return (path)


def download(asd, path, name):
    for x in asd:
        b = x.string.split('"')
        for xd in b:
            if "jpg?" in xd:
                if not "100x100" in xd:
                    xdf = xd.replace("\/", "/")
                    jpg = requests.get(xdf)
                    f = open(
                        f'{path}/test_{name}.jpg', 'wb')
                    f.write(jpg.content)   # 寫入圖片的 content
                    f.close()              # 寫入完成後關閉圖片檔案
                    name = name + 1


def downinst():
    asf = 0
    try:
        urllib.request.build_opener().open(ent1.get())
        web = requests.get(ent1.get())
        soup = BeautifulSoup(web.text, "html.parser")
        asd = soup.find_all("script", type="application/ld+json")
        path = check(asf)
        download(asd, path, 0)
        messagebox.showinfo(" ", "下載完成")
    except ValueError:
        messagebox.showerror(" ", "輸入錯誤")


top = Tk()
top.title("ig圖片下載.exe")
top.geometry('275x75')
top.resizable(0, 0)
lbl1 = Label(top, text="IG網址:")
lbl1.pack(side=LEFT)
ent1 = Entry(top, bd=5)
# 這個欄位就是用來做使用者輸入紀錄的地方
ent1.pack(side=LEFT)
button_pop = Button(top, text="下載", command=downinst)
button_pop.pack(side=RIGHT)
top.mainloop()
