import re
import json
import requests
import time
from prettytable import PrettyTable

def len_zh(data):
    temp = re.findall('[^a-zA-Z0-9()[]Ⅱ .·]+', data)
    count = 0
    for i in temp:
        count += len(i)
    return(count)


pattern = re.compile(r'\d+')

with open('bookinfo.json', 'r') as f:
    bookinfo = json.load(f)

book_num = []
for (k,v) in bookinfo.items():
	for index in range(len(bookinfo[k])):
		booknum_tmp = pattern.findall(bookinfo[k][index])
		booknum_tmp_str = ''.join(booknum_tmp)
		book_num.append(booknum_tmp_str)


with open('booknum.txt','w') as f:
	tmp_list = [line + '\n' for line in book_num]
	f.writelines(tmp_list)
book_num1 = list(set(book_num))

with open('booknum1.txt','w') as f:
	tmp_list = [line + '\n' for line in book_num1]
	f.writelines(tmp_list)

print(len(book_num))
print(len(book_num1))
book = []
proxies = {
  "http": "http://111.56.13.150:82"
}
for index in range(len(book_num1)):
	time.sleep(2)
	url = "https://api.douban.com/v2/book/" + book_num1[index]
	print(index)
	request = requests.get(url,proxies = proxies)
	book.append(json.loads(request.text))

#print(book)

#for index in range(len(book)):
	#print(book[index]['rating']['average'])


#print('\n\n\n\n')

book_sort= sorted(book, key=lambda d:d['rating']['average'], reverse = True)
#print((book_sort))
with open('book.txt','w') as f:
	tmp_list = [str(line) + '\n' for line in book_sort]
	f.writelines(tmp_list)

bookinfoTable = PrettyTable(["排序", "书名", "作者", "评分", "评分人数"])  
bookinfoTable.align["排序"] = "l"
bookinfoTable.align["评分人数"] = "r"
bookinfoTable.align["书名"] = "l"

bookinfoTable.padding_width = 5# One space between column edges and contents (default)

for index in range(len(book_sort)):
	#print(str(index)+' '+book_sort[index]['title']+'\t'+book_sort[index]['author'][0]+'\t'+str(book_sort[index]['rating']['average'])+'\t'+str(book_sort[index]['rating']['numRaters'])+'\n')
	#print(book_sort[index]['rating']['average']+'\t'+)
	author = ''
	title = book_sort[index]['title']
	rating_ave = str(book_sort[index]['rating']['average'])
	numRaters = str(book_sort[index]['rating']['numRaters'])
	for i in range(len(book_sort[index]['author'])):
		author += book_sort[index]['author'][i]
	zh = len_zh(title)
	width = 50 - zh
	bookinfoTable.add_row([index,title, author, rating_ave, numRaters])  
	
print(bookinfoTable)

bookhtml = bookinfoTable.get_html_string()
#bookhtml = str(bookhtml.encode("utf-8"))
with open('book.html','w') as f:
	f.write(bookhtml)
with open('book.txt','w') as f:
	f.write(bookinfoTable)

#print(repr(index).ljust(3), title.ljust(50-zh), rating_ave.ljust(5),numRaters.ljust(5))	
	#print('{0:5d} {1:width} {2:10} {3:10}'.format(index, title, rating_ave, numRaters))
	#print(format1 % (5, index, width, title, 10, rating_ave, 10, numRaters))
		#print(repr(index).ljust(3), title.ljust(20-zh), rating_ave.ljust(5),numRaters.ljust(5),file = f)
		#f.writelines(repr(index).ljust(3), title.ljust(40-zh), rating_ave.ljust(5),numRaters.ljust(5))

	#print('{0:10d} ==> {1:50} ==> {2:10} ==> {3:10}'.format(index, title, rating_ave, numRaters))
