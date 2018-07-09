from urllib.request import urlopen
import urllib.request
import os
import sys
import time
import re
import requests


# 全局声明的可以写到配置文件，这里为了读者方便看，故只写在一个文件里面
# 图片地址
picpath = r'E:\Python_Doc\Images'
# 网站地址
mm_url = "http://www.263dm.com/html/ai/%s.html"


# 保存路径的文件夹，没有则自己创建文件夹,不能创建上级文件夹
def setpath(name):
 path = os.path.join(picpath, name)
 if not os.path.isdir(path):
     os.mkdir(path)
 return path


def getUrl(url):
 aa = urllib.request.Request(url)
 html = urllib.request.urlopen(aa).read()
 p = r"(http://www\S*/\d{4}\.html)"
 return re.findall(p, str(html))


def get_image(savepath, url):
 aa = urllib.request.Request(url)
 html = urllib.request.urlopen(aa).read()
 p = r"(http:\S+\.jpg)"
 url_list = re.findall(p, str(html))
 for ur in url_list:
     save_image(ur, ur, savepath)


def save_image(url_ref, url, path):
 headers = {"Referer": url_ref,
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
            '(KHTML, like Gecko)Chrome/62.0.3202.94 Safari/537.36'}
 content = requests.get(url, headers=headers)
 if content.status_code == 200:
     with open(path + "/" + str(time.time()) + '.jpg', 'wb') as f:
         for chunk in content:
             f.write(chunk)


def do_task(savepath, index):
 print("正在保存页数：%s " % index)
 url = mm_url % i
 get_image(savepath, url)


if __name__ == '__main__':
 # 文件名
 filename = "Adult"
 # filepath = setpath(filename)

 for i in range(10699, 9424, -1):
     filepath = setpath(filename+'\\'+str(i))
     do_task(filepath, i)