from urllib import request
import re
import os


# 全局声明的可以写到配置文件，这里为了读者方便看，故只写在一个文件里面
# 图片地址
picpath = r'E:\Python_Doc\Images'
# 7160地址
mm_url = "http://www.7160.com/xingganmeinv/list_3_%s.html"
mm_url2 = "http://www.7160.com/meinv/%s/index_%s.html"


# 保存路径的文件夹，没有则自己创建文件夹,不能创建上级文件夹
def setpath(name):
 path = os.path.join(picpath, name)
 if not os.path.isdir(path):
    os.mkdir(path)
 return path


def get_html(url):
 req = request.Request(url)
 return request.urlopen(req).read()


def get_image(path, url):
 req = request.Request(url)
 get_img = request.urlopen(req).read()
 with open(path + '/' + url[-14:], 'wb') as fp:
     fp.write(get_img)
 return


def do_task(path, url):
 html = get_html(url)
 p = r"<a href=\"/meinv/(\d+)/\""
 get_list = re.findall(p, str(html))
 for list in get_list:
     for i in range(2, 200):
         try:
             url2 = mm_url2 % (list, i)
             html2 = get_html(url2)
             p = r"http://img\.7160\.com/uploads/allimg/\d+/\S+\.jpg"
             image_list = re.findall(p, str(html2))
             print(image_list[0])
             get_image(path, image_list[0])
         except:
             break
         break


if __name__ == '__main__':
 # 文件名
 filename = "7160"
 filepath = setpath(filename)

 for i in range(2, 288):
     print("正在下载页数：List_3_%s " % i)
     url = mm_url % i
     do_task(filepath, url)