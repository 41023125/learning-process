import requests
from bs4 import BeautifulSoup
import datetime

file_path = 'Book.txt'  
file_path = '書本.txt'  

def print_hyperlink(text, url):
    print(f"\033]8;;{url}\033\\{text}\033]8;;\033\\")

def count_lines_in_file(file_path):
    """
    檢查Book資料數
    """
    with open(file_path, 'r',encoding='utf-8') as file:
        for line in file:
            url = line.strip().split()[-1]
            #print(line.strip().split()[0])
            if (main(url.strip())) != []:
                # print(line.strip().split()[0])
                print_hyperlink(line.strip().split()[0],url)
                print(main(url.strip()))
                
    '''
        for line in file:
            '''

# 獲取現在的日期
current_date = datetime.date.today()
# 將日期轉換為特定格式的字串
formatted_date = current_date.strftime("%Y-%m-%d")

def main(url):
    tagall= []
    response = requests.get(url)
    soup = BeautifulSoup(response.content.decode('GBK'), 'html.parser')

    span_tags = soup.find_all(['a'])

    for tag in span_tags:
        if '章' in tag.text and formatted_date in tag.text:
            #print(tag.text)
            tagall = tag.text
    return tagall
count_lines_in_file(file_path)
input("按下Enter退出...")
