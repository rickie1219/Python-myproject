# coding:utf-8
import requests
from bs4 import BeautifulSoup
import re
path = "E:\\Dropbox\\pythonTest\\Python-lxf\\"
domain = "http://www.liaoxuefeng.com"
html_head = r'<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"></head><body>'

file_name = path + 'Git教程.html'
with open(file_name,"wb") as f:
        f.write(html_head.encode("utf-8"))


r = requests.get("http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000") # Python教程
r = requests.get("http://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000") # Git教程
soup = BeautifulSoup(r.text,"html.parser")
# 得到每节的链接
links = [a.attrs.get('href') for a in soup.select('div.x-sidebar-left-content a[href^=/wiki]')]
title = [a.attrs.get('href') for a in soup.select('div.x-sidebar-left-content a[href^=/wiki]')]
# 开始遍历链接
print(len(links))
for li in links:
    url = domain + li
    r = requests.get(url)
    soup = BeautifulSoup(r.text,"html.parser")
    head = str((soup.find("h4")))
    title =str(soup.find("h4").text)
    title = title.replace("/", " ")
    body = str(soup.find("div",{"class":"x-wiki-content"}))
    html = head + body
    html = html.split(r'<h3 id="-">关于作者</h3>')[0]
    html_body = html.replace(r'src="', 'src="' + domain)

    html_file = html_body
    # 输出html文件
    with open(file_name,"ab") as f:
        f.write(html_file.encode("utf-8"))

with open(file_name,"ab") as f:
        f.write("</body></html>".encode("utf-8"))




