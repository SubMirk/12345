from urllib import request
import re
import os
from bs4 import BeautifulSoup
from urllib.error import HTTPError


# 全局声明的可以写到配置文件，这里为了读者方便看，故只写在一个文件里面
# 图片地址
picpath = r'E:\Python_Doc\Images'
# 网站地址
mm_url = "http://pic.yesky.com/c/6_20771_%s.shtml"


# 保存路径的文件夹，没有则自己创建文件夹,不能创建上级文件夹
def setpath(name):
 path = os.path.join(picpath, name)
 if not os.path.isdir(path):
     os.mkdir(path)
 return path


# 获取html内容
def get_html(url):
 req = request.Request(url)
 return request.urlopen(req).read()


# 保存图片
def save_image(path, url):
 req = request.Request(url)
 get_img = request.urlopen(req).read()
 with open(path + '/' + url[-14:], 'wb') as fp:
     fp.write(get_img)
 return


def do_task(path, url):
 html = get_html(url)
 p = r'(http://pic.yesky.com/\d+/\d+.shtml)'
 urllist = re.findall(p, str(html))
 # print(urllist)
 for ur in urllist:
     for i in range(2, 100):
         url1 = ur[:-6] + "_" + str(i) + ".shtml"
         print(url1)
         try:
             html1 = get_html(url1)
             data = BeautifulSoup(html1, "lxml")
             p = r"http://dynamic-image\.yesky\.com/740x-/uploadImages/\S+\.jpg"
             image_list = re.findall(p, str(data))
             print(image_list[0])
             save_image(path, image_list[0])
         except:
             break


if __name__ == '__main__':

 # 文件名
 filename = "YeSky"
 filepath = setpath(filename)

 for i in range(2, 100):
     print("正在6_20771_%s " % i)
     url = mm_url % i
     do_task(filepath, url)