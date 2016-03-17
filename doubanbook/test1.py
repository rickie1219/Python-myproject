import re
from prettytable import PrettyTable 
def len_zh(data):
    temp = re.findall('[^a-zA-Z0-9.()Ⅱ ]+', data)
    count = 0
    for i in temp:
        count += len(i)
    return(count)
 

width = 60
width1 = int(width)
pricr_width = 10
item_width = width1 - pricr_width
header_format = '%-*s%*s'
format1 = '%-*s%*.2f'
print('='*width1)

str1 = "zhongwen测试()"
str2 = "aaa"
#调用ljust前先计算中文字符个数
zh1 = len_zh(str1)
zh2 = len_zh(str2)
#动态修正填充字符数
print(zh1,zh2)



aa = "就喜欢你看不惯我又干不掉我的样子"
bb = "剩者为王Ⅱ"

cc = "亞人 01"
dd = "Neural Networks for Pattern Recognition"
zh1 = len_zh(aa)
zh2 = len_zh(bb)
zh3 = len_zh(cc)
zh4 = len_zh(dd)
#print(header_format % (item_width, 'Item', pricr_width, 'Price'))
#rint('-'*width1)
print(format1 % (item_width-zh1,aa,pricr_width, 8.4))
print(format1 % (item_width-zh2,bb,pricr_width, 7.5))
print(format1 % (item_width-zh3,cc,pricr_width, 7.5))
print(format1 % (item_width-zh4,dd,pricr_width, 7.5))

x = PrettyTable(["City name", "Area", "Population", "Annual Rainfall"])  
x.align["City name"] = "l"# Left align city names
x.padding_width = 1# One space between column edges and contents (default)
x.add_row(["Adelaide",1295, 1158259, 600.5])  
x.add_row(["Brisbane",5905, 1857594, 1146.4])  
x.add_row(["Darwin", 112, 120900, 1714.7])  
x.add_row(["Hobart", 1357, 205556, 619.5])  
x.add_row(["Sydney", 2058, 4336374, 1214.8])  
x.add_row(["Melbourne", 1566, 3806092, 646.9])  
x.add_row(["Perth", 5386, 1554769, 869.4])

result = x.get_html_string()
with open('test.html','w') as f:
	f.write(result)


