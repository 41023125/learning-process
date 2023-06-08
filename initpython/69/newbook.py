from bs4 import BeautifulSoup

def extract_h3_content_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        html_data = file.read()

    soup = BeautifulSoup(html_data, 'html.parser')
    h3_tags = soup.select('h3 > a')#>span

    h3_contents = []
    for h3_tag in h3_tags:
        h3_tag2 = h3_tag.select('span')
        if h3_tag2:
            span_tag = h3_tag2[0]  # 获取第一个 <span> 标签
            name = span_tag.text.strip()
            h3_contents.append(name + '  ' + 'https://www.69shu.com' + h3_tag.get('href'))
            #print(name)

    return h3_contents

file_path = 'mybook.txt'  # 替换为你的文件路径
h3_contents = extract_h3_content_from_file(file_path)

for content in h3_contents:
    print(content)
    pass
    
def save_to_txt(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as file:
        for item in data:
            file.write(item + '\n')

# output_file_path = '書名.txt'  # 替换为你想要保存的文件路径
# 
output_file_path = '書本.txt'
save_to_txt(output_file_path, h3_contents)
''''''