from selenium import webdriver
import os
import requests
import re
from urllib.request import urlopen
import urllib.error
import time


# 全局声明的可以写到配置文件，这里为了读者方便看，故只写在一个文件里面
# 图片地址
bookpath = r'E:\Python_Doc\Book'
# 网站地址
url_main = "https://www.6859s.com"
ooxx_url = "https://www.6859s.com/Html/84/"
# 保存路径的文件夹，没有则自己创建,不能创建目录
def setpath(book_path, name):
	path = os.path.join(book_path, name)
	if not os.path.isdir(path):
		os.mkdir(path)
	return path

def judge_file(file):
	flag = False
	if os.path.isfile(file):
		flag = True
	return flag

# 用chrome headless打开网页
def gethtml(url):
	# # options = webdriver.ChromeOptions()
	# # options.add_argument('--headless')
	# # browser = webdriver.Chrome(chrome_options=options)
	
	# browser = webdriver.Chrome()
	# browser.get(url)
	# html = browser.page_source
	# browser.quit()
	# return html
	try:
		response = urlopen(url, timeout = 60) #这里是要读取内容的url  
		content = response.read().decode('utf-8') #读取，一般会在这里报异常
		response.close() #记得要关闭
	except urllib.error.URLError as e:
		print (e.reason)
		content = ''
		fileObject = open(bookpath + '/error.txt', 'w', encoding='utf-8')
		fileObject.write(str(e) + '\n')
		fileObject.write(url) 
		fileObject.write("\n\n") 
		fileObject.close()

	return content

# 打开网页返回网页内容
def open_webpage(html):
	reg = r'<li><a href="(.*?)".*?</span>【(.*?)】(.*?)</a>'
	bookre = re.compile(reg)
	booklist = re.findall(bookre, html)
	return booklist

# 打开网页返回图书内容
def open_book(book_html):
	reg = '<font size="4" color="#1e1d1d">\r\n(.*?)</font>'
	bookre = re.compile(reg, re.S)
	booklist = re.findall(bookre, book_html)
	book =re.sub("<i>.*?<br />\u3000\u3000","", booklist[0])
	book = "    "+ re.sub("<br />|<br>","\n", book)
	return book

# 保存图书
def savebook(path, url, bookname):

	book_url = url_main + url
	booktext = gethtml(book_url)
	book = open_book(booktext)  
	
	fileObject = open(path + '/' + bookname, 'w', encoding='utf-8')
	fileObject.write(book) 
	fileObject.close() 

def do_task(path, index):
	print("正在处理第 %s 页:\n" % index)
	web_url = ooxx_url 
	if index != 1:
		web_url += "index-%s.html" % index
	htmltext = gethtml(web_url)
	booklists = open_webpage(htmltext)

	for j in range(len(booklists)):
		bookname = re.sub("\?|/| ","", booklists[j][2]) + '.txt'
		filepath = setpath(path, booklists[j][1])
		if(judge_file(filepath + '/' + bookname)):
			print("\t%s 已存在" % bookname)
			continue
		print("\t第 %s-%d 本 %s " % (index, j+1, booklists[j][1])+ bookname)
		time.sleep(j % 5)
		savebook(filepath, booklists[j][0], bookname)
	print ("\n")


if __name__ == '__main__':

	for i in range(61, 246):
		do_task(bookpath, i)
		time.sleep(i % 5)
