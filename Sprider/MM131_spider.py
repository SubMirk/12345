# import requests
# import re

# url = 'http://www.mm131.com/xinggan/2373_3.html'
# html = requests.get(url).text           #读取整个页面为文本
# a = re.findall(r'<img alt=".*?" src="(.*?.jpg)" /></a></div>',html,re.S)  #匹配图片url
# print(a)

# pic= requests.get(a[0], timeout=20)  #time设置超时，防止程序苦等
# fp = open(r'F:\图片\1234\2.jpg','wb')    #以二进制写入模式新建一个文件
# fp.write(pic.content)  #把图片写入文件
# fp.close()
# 
# 
# 
# 


# """
# 此程序考虑的情况很多，下面有注释
# """
# import requests, time
# import os
# import numpy as np
# import urllib.request
# from bs4 import BeautifulSoup

# #tag =['清纯私房','俏皮私房','COSPLAY', '比基尼美女', '魅惑写真',  '日本美女', '丝袜美女', '丝袜美腿', '性感车模', '性感美女', '阳光美女', '长腿美女']
# tag = [ '魅惑写真']


# URL = 'https://www.chaoxiubang.com'
# FILE = 'F:\\python program\\潮秀网图片'
# #创建文件夹
# def CreatFile(file, title):
#     path = file
#     title = title
#     new_path = os.path.join(path, title)
#     if not os.path.isdir(new_path):
#         os.makedirs(new_path)
#     return new_path

# #获取html
# def get_html(url):
#     html = requests.get(url)
#     html.encoding = 'gbk'
#     soup = BeautifulSoup(html.text, 'lxml')
#     return soup
# #判断文件名是否合法，有些图片名中含有非法字符不止一处，所以使用循环判断，直到合法
# def judgeName(name):
#     flag = True
#     while flag:
#         if '?' in name:
#             name = name.replace('?', '_')
#         elif '\\' in name:
#             name = name.replace('\\', '_')
#         elif '/' in name:
#             name = name.replace('/', '_')
#         elif '：' in name:
#             name = name.replace('：', '_')
#         elif ':' in name:
#             name = name.replace(':', '_')
#         elif '*' in name:
#             name = name.replace('*', '_')
#         elif '"' in name:
#             name = name.replace('"', '_')
#         elif '<' in name:
#             name = name.replace('<', '_')
#         elif '>' in name:
#             name = name.replace('>', '_')
#         elif '|' in name:
#             name = name.replace('', '_')
#         else:
#             flag = False
#     return  name

# #获得图片，暂时第一张，因为网站的特点，每一组图片的第二及之后的图片链接和第一张的不一致
# #只能分别处理
# def get_pic_name(soup):
#     h3 = soup.find('h3')
#     name = h3.find('a').get_text()
#     pic_href = soup.find('div', attrs={'class':'article_left_top_body'})
#     src = pic_href.find('img')['src']
#     return name, src

# def main():
#     for category in tag:
#         fInput = open('F:\\python program\\潮秀网图片\\url.txt', 'r', encoding = 'utf-8')
#         line = fInput.readline()
#         while line:
#             linesplit = line.split(';')
#             countNum = linesplit[0].strip()
#             print(time.ctime() + '正在打印' + category + ':第' + str(countNum) + '组')
#             url = linesplit[1].strip()
#             if URL not in url:
#                 url =  URL + url
#             print(url)
#             html = get_html(url)


#             try:#有些链接定位不到就继续下一个链接的爬取
#                 name, src = get_pic_name(html)
#                 print('-------------'+name)
#                 name = judgeName(name)
#             except:
#                 line = fInput.readline()  #
#                 continue

#             try:
#                 print(name+'-------------')
#                 fOutput = open('F:\\python program\\潮秀网图片\\'+category + '\\'+countNum+'_'+ name + '\\'+ name +'.jpg', 'wb')
#                 print(fOutput)
#                 print(category)
#             except:
#                 newpath = CreatFile(FILE+'\\'+category, countNum+'_'+name)
#                 fOutput = open(newpath + '\\'+ name +'(1).jpg', 'wb')
#                 print(newpath)
#             try:#有些图片不存在，若不存在就继续下一组套图的爬取
#                 req = urllib.request.urlopen(src)
#                 buf = req.read()
#                 fOutput.write(buf)
#                 fOutput.close()
#             except:
#                 line = fInput.readline()#链接图片不存在跳转到下一页
#                 continue
#             page = 2#控制图片链接的页数，也可以用代码去定位到页数控制，个人感觉这样方便
#             while url:#对套图非首页的采集
#                 try:
#                     surl = url[:-5] + '_'+str(page)+'.html'
#                     print(surl)
#                     html = get_html(surl)
#                     sname, src = get_pic_name(html)
#                     sname = judgeName(sname)
#                     fOutput = open('F:\\python program\\潮秀网图片\\'+category + '\\'+countNum+'_'+ name + '\\'+ sname +'.jpg', 'wb')
#                     req = urllib.request.urlopen(src)
#                     buf = req.read()
#                     fOutput.write(buf)
#                     fOutput.close()
#                     page += 1
#                 except:
#                     break
#             line = fInput.readline()
#         fInput.close()
#         # break
# if __name__ == '__main__':
#     main()


