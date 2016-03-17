import re
import json
def len_zh(data):
    temp = re.findall('[^a-zA-Z0-9.]+', data)
    count = 0
    for i in temp:
        count += len(i)
    return(count)
 

width = 46
width1 = int(width)
pricr_width = 10
item_width = width1 - pricr_width
header_format = '%-*s%*s'
format1 = '%-*s%*.2f'
print('='*width1)

str1 = "zhongwen测试"
str2 = "aaa"
#调用ljust前先计算中文字符个数
zh1 = len_zh(str1)
zh2 = len_zh(str2)
#动态修正填充字符数
print(zh1,zh2)

print(header_format % (item_width, 'Item', pricr_width, 'Price'))
print('-'*width1)
print(format1 % (item_width-zh1,str1,pricr_width, 8.4))
print(format1 % (item_width-zh2,str2,pricr_width, 7.5))

aa = "白鹿原"
aa = "aaaaaa"
print(len(aa))
index= 2
print(repr(index).rjust(20))


with open('book.txt','r') as f:
	tmp_list = f.readlines()


print(type((tmp_list[0])))