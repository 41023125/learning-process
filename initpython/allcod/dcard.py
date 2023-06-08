# https://www.youtube.com/watch?v=ximjGyZ93YQ&t=1260s&ab_channel=GrandmaCan-%E6%88%91%E9%98%BF%E5%AC%A4%E9%83%BD%E6%9C%83
# https://selenium-python.readthedocs.io/waits.html
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome()
driver.get("https://www.dcard.tw/f")
div = driver.find_element(By.NAME, "query")
div.send_keys("嚴家銘")
time.sleep(1)
div.send_keys(Keys.RETURN)
element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "atm_am_kb7nvz wdl7s0r"))
)
