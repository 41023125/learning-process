# https://www.youtube.com/watch?v=ximjGyZ93YQ&ab_channel=GrandmaCan-%E6%88%91%E9%98%BF%E5%AC%A4%E9%83%BD%E6%9C%83
# https://sites.google.com/chromium.org/driver/
# https://sites.google.com/chromium.org/driver/getting-started?authuser=0
# https://stackoverflow.com/questions/29092970/importerror-cannot-import-name-webdriver
# 新版本更改https://blog.csdn.net/m0_49076971/article/details/126233151
# https://blog.csdn.net/stitchD/article/details/123818886
# 網頁自動關閉問題https://blog.csdn.net/qq_38737519/article/details/128553456
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://popcat.click")
div = driver.find_element(By.ID, "app")
count = 0
while (count < 999999999):
    div.click()
    count += 1
