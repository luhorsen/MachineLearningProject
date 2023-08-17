import requests
from bs4 import BeautifulSoup

# 设置请求头，模拟浏览器访问
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# 目标小说的url
url = 'http://www.lidapoly.com/ldks/22884/'

# 发送请求获取小说章节页面
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

# 找到所有章节的链接
chapter_links = soup.select('.book_item')

# 创建一个空的文本文件
filename = 'D:\桌面\\book.txt'
with open(filename, 'w', encoding='utf-8') as f:
    # 循环遍历章节链接，并逐个下载章节内容
    for link in chapter_links:
        chapter_url = link['href']
        chapter_url = url + chapter_url  # 构造完整的章节链接

        # 发送请求获取章节内容页面
        chapter_response = requests.get(chapter_url, headers=headers)
        chapter_soup = BeautifulSoup(chapter_response.content, 'html.parser')

        # 找到章节标题和内容
        chapter_title = chapter_soup.select_one('.bookname h1').text.strip()
        chapter_content = chapter_soup.select_one('#content').text.strip()

        # 将章节标题和内容写入文本文件
        f.write(chapter_title + '\n\n')
        f.write(chapter_content + '\n\n')

        print(f"已抓取章节：{chapter_title}")

print("所有章节已爬取完成！")