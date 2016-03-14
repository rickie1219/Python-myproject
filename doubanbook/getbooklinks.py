
import requests
import re
from bs4 import BeautifulSoup
import time
import json

domain = "https://book.douban.com/tag/?view=type&icn=index-sorttags-all"
headers={    "Host":"www.douban.com",    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0",    "Accept-Language":"zh \
-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",    "Accept-Encoding":"gzip, deflate",    "Connection":"keep-alive"}
proxies = {
  "http": "http://111.56.13.150:82"
}

class GetLable:
	'''
	得到所有标签及对应url
	'''
	def __init__(self, url,proxy):
		#self.label_name = []
		#self.label_links = []

	
		request = requests.get(url,proxies = proxy)
		state = request.status_code
		print(state)
		soup = BeautifulSoup(request.text,"html.parser")
		links_body = soup.find_all("tbody")
		links = []

		for index in range(len(links_body)):
		#for index in range(2):
		    links += links_body[index].find_all('a')

		url1 = "https://www.douban.com/tag/"
		url2 = "/book"
		self.label_name = [tmp.text for tmp in links]
		self.label_links = [url1 + tmp.text + url2 for tmp in links ]
		#labellinks_dict = dict(zip(label_name,label_links))





def GetBookLinks(url,proxy):
	book_links = []
	pages_num = 1
	url_tmp = url
	while True:
		time.sleep(5)

		request = requests.get(url,proxies=proxy)
		state = request.status_code
		soup = BeautifulSoup(request.text,"html.parser")
		html_body = soup.find_all("dd")
		links_tmp = []
		print(url)
		print("当前标签的第 %d 页" % (pages_num))  
		if len(html_body) == 0:
			print("当前标签采集完成")
			break
		
		for index in range(len(html_body)):
			links_tmp += html_body[index].find_all('a')
		for index in range(len(links_tmp)):
			book_links.append(links_tmp[index]['href'])
		
		url = url_tmp + '?start=' + str(15*pages_num)
		pages_num += 1


	
	return book_links

def GetBookLinks_firstpage(url,proxy):
	
	
	time.sleep(1)
	request = requests.get(url,proxies=proxy)
	state = request.status_code
	soup = BeautifulSoup(request.text,"html.parser")
	html_body = soup.find_all("dd")
	links_tmp = []
	book_links = []
	
	for index in range(len(html_body)):
		links_tmp += html_body[index].find_all('a')
	for index in range(len(links_tmp)):
		book_links.append(links_tmp[index]['href'])
	


	
	return book_links


label_links = GetLable(domain,proxies).label_links
label_name = GetLable(domain,proxies).label_name

book_links = []
#for index in range(len(label_links[0])):
#for index in range(1):
for index in range(len(label_links)):
	time.sleep(5)
	print("当前标签：%s" % (label_name[index]))
	book_links.append(GetBookLinks(label_links[index],proxies))

	with open(label_name[index]+'.txt','w') as f:
		f.write(label_name[index]+"\n")
		tmp_list = [line + '\n' for line in book_links[index]]
		f.writelines(tmp_list)


bookinfo = dict(zip(label_name,book_links))

with open('bookinfo.json', 'w') as f:
    json.dump(bookinfo, f, ensure_ascii=False)


for (k,v) in bookinfo.items():
	with open('bookinfo.txt','a') as f:
		f.write(k+"\n")
		tmp_list = [line + '\n' for line in bookinfo[k]]
		f.writelines(tmp_list)


#print(state)
#print(len(label_links))#145
#print(type(label_links[0]))
#print(len(book_links[0]))#145
#print(book_links)
