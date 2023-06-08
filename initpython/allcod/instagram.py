# https://www.youtube.com/watch?v=ximjGyZ93YQ&t=1260s&ab_channel=GrandmaCan-%E6%88%91%E9%98%BF%E5%AC%A4%E9%83%BD%E6%9C%83
# https://selenium-python.readthedocs.io/waits.html
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
import os
path = "./123 "
if not os.path.isdir(path):
    os.makedirs(path, mode=0o777)
driver = webdriver.Chrome()
driver.get("https://www.instagram.com/")
username = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "username"))
)
password = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "password"))
)
username.clear()
password.clear()
username.send_keys("3j2413")
password.send_keys("asd123456")
login = driver.find_element_by_xpath(
    '//*[@id="loginForm"]/div/div[3]/button/div')
login.click()
asdd = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]'))
)
asdd.click()
search = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[1]/div/input'))
)
search.clear()
search.send_keys("#cat")
search.send_keys(Keys.RETURN)
time.sleep(1)
search.send_keys(Keys.RETURN)
time.sleep(1)
search.send_keys(Keys.RETURN)
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.CLASS_NAME, "_aao7"))
)
name = 0
imgs = driver.find_elements_by_class_name(
    "x5yr21d.xu96u03.x10l6tqk.x13vifvy.x87ps6o.xh8yej3")
for img in imgs:
    # https://steam.oxxostudio.tw/category/python/spider/ptt-beauty.html
    print(img.get_attribute("src"))
    # 使用 requests 讀取圖片網址，取得圖片編碼
    jpg = requests.get(img.get_attribute("src"))
    # 使用 open 設定以二進位格式寫入圖片檔案
    f = open(
        f'C:/initpython/123/test_{name}.jpg', 'wb')
    f.write(jpg.content)   # 寫入圖片的 content
    f.close()              # 寫入完成後關閉圖片檔案
    name = name + 1
