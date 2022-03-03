from urllib import request
import urllib.request
from selenium import webdriver
import requests
import time
import re
import os
import random

# 全局声明的可以写到配置文件，这里为了读者方便看，故只写在一个文件里面

fileDir = {
    '国产': {'自拍视频': "/video/zipai/", '淫妻作乐': "/video/fuqi/", '开放青年': "/video/kaifang/", '精品分享': "/video/jingpin/", '台湾辣妹': "/video/twmn/", '韩国主播': "/video/krzb/", '动漫卡通': "/video/dongman/", '经典三级': "/video/sanji/"}, 
    '女优': {'女性向純愛': "/av/nxx/", '波多野结衣': "/av/bdyjy/", '深田咏美': "/av/stym/", '桥本有菜': "/av/qbyc/", '苍井空': "/av/cjk/", '三上悠亚': "/av/ssyy/", '天海翼': "/av/thy/", '吉泽明步': "/av/jzmb/"},
    '电影': {'无码中字': "/movie/wuma/", 'SM系列': "/movie/sm/", '高清无码': "/movie/gaoqing/", '熟女人妻': "/movie/shunv/", '美颜巨乳': "/movie/meiyan/", '丝袜制服': "/movie/siwa/", '中文有码': "/movie/youma/", '欧美系列': "/movie/oumei/"}, 
    '图文': {'自拍偷拍': "/pic/toupai/", '美腿丝袜': "/pic/meitui/", '欧美色图': "/pic/oumei/", '卡通图片': "/pic/katong/", '都市小说': "/pic/dushi/", '乱伦小说': "/pic/luanlun/", '校园小说': "/pic/xiaoyuan/", '人妻小说': "/pic/renqi/"}
    } 

fileDir1 = {
    '电影': {'日韩无码': "/home/vodlist/38/1316-%s.html", '欧美无码': "/home/vodlist/38/1317-%s.html", '中文字幕': "/home/vodlist/38/1318-%s.html", '日韩有码': "/home/vodlist/38/1319-%s.html", '国产自拍': "/home/vodlist/38/1320-%s.html", '国产偷拍': "/home/vodlist/38/1321-%s.html", '卡通动漫': "/home/vodlist/38/1322-%s.html", '三级剧情': "/home/vodlist/38/1323-%s.html", '日韩女优': "/home/starslist/38/1325-%s.html", '欧美艳星': "/home/starslist/38/1347-%s.html"},
    '图片': {'精品图集': "/home/piclist/38/1327-%s.html", '欧美风情': "/home/piclist/38/1328-%s.html", '亚洲情色': "/home/piclist/38/1329-%s.html", '性爱自拍': "/home/piclist/38/1330-%s.html", '成人动漫': "/home/piclist/38/1331-%s.html", '美腿丝袜': "/home/piclist/38/1332-%s.html", '唯美写真': "/home/piclist/38/1333-%s.html", '人体艺术': "/home/piclist/38/1334-%s.html"},
    '小说': {'都市情感': "/home/textlist/38/1336-%s.html", '人妻熟女': "/home/textlist/38/1337-%s.html", '玄幻武侠': "/home/textlist/38/1338-%s.html", '另类其它': "/home/textlist/38/1339-%s.html", '明星校园': "/home/textlist/38/1340-%s.html", '家庭乱伦': "/home/textlist/38/1341-%s.html", '成人小说': "/home/textlist/38/1342-%s.html", '暴力虐待': "/home/textlist/38/1343-%s.html"}
    }

dirList = []
dirList1 = []
FileNUM = len(fileDir1)
FileTypeNUM = len(dirList1) - 3

BOOK = 2
IMG = 1

TYPE = [1316, 1327, 1336]

# 图片地址
bookPath = r'E:/'
# bookPath = r'g:'

# 地址
rootPath = r'https://www.x8c88.com/'
rootURL = r'https://aaq52.com:33666/'

def setpath(name):
    path = os.path.join(bookPath, name)
    # print(path)
    if not os.path.isdir(path):
       os.makedirs(path)
    return path

def get_html(url_ref, url):
    # req = request.Request(url)
    # return request.urlopen(req).read()

    # aa = urllib.request.Request(url)
    # html = urllib.request.urlopen(aa).read()

    # options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # options.add_argument('--no-sandbox')
    # options.add_argument('--disable-gpu')
    # options.add_argument('--disable-dev-shm-usage')
    # browser = webdriver.Chrome(chrome_options=options)
    # # browser = webdriver.Chrome()
    # # browser.get('https://aaq52.com:33666/home/index.html')
    # # browser.get('https://www.x8c88.com/pic/oumei')
    # browser.get(url)
    # html = browser.page_source
    # time.sleep(5)
    # browser.quit()

    headers = {
            'Referer': url_ref,
            'User-Agent': 'Mozilla/5.0 (Linux; U; Android 2.2.1; zh-cn; HTC_Wildfire_A3333 Build/FRG83D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'
            }
    h = requests.get(url, headers=headers, timeout = 5)
    h.encoding = 'utf-8'
    html = h.text
    # print(html)
    return html

def get_book_url(url):
    html = get_html(rootPath, rootPath + url)
    p = r'<dt><a href="(.*?)" title="(.*?)" target="_blank">'
    book_url_list = re.findall(p, str(html))
    p = r'(/\w+/\w+/index_\d+.html)">下一页'
    next_url = re.findall(p, str(html))
    # print(next_url) 
    return (book_url_list, next_url)

def get_book(num, url):
    next_url = [url]
    if num > 7:
        while(next_url != []):
            print(next_url[0])
            book_url_list, next_url = get_book_url(next_url[-1])
            download_book(book_url_list)
    else:
        while(next_url != []):
            print(next_url[0])
            pic_html, next_url = get_book_url(next_url[-1])
            download_pic(pic_html)

    print('\n*****下载完毕*****')

def download_pic(pic_html):
    for pic_name in pic_html:
        if os.path.exists(pic_name[1] + '.txt'):
            print(pic_name[1] + '\t已存在')
            continue
        html = get_html(rootPath, rootPath + pic_name[0])
        p = r"<br><img src='https://[\w/]+.jpg'"
        pic_list = re.findall(p, str(html))
        print(pic_list)

def download_book(book_url_list):
    for book_url in book_url_list:
        if os.path.exists(book_url[1] + '.txt'):
            print(book_url[1] + '\t已存在')
            continue
        html = get_html(rootPath, rootPath + book_url[0])
        p = r'&nbsp;</h2>\r\n\t\t(.*?)<br/>'
        text = re.findall(p, str(html), re.S)[0]
        w_book(book_url[1], text)

def w_book(name, text):
    text = re.sub(' ', '', text)
    text = re.sub('····+', r'……<br><br>', text)
    for ch in ['。','？','」','！','”']:
        # text = re.sub(ch + '<br>', ch + r"\n", book_text[0])
        text = text.replace(ch + '<br>', ch + r'<br><br>')

    rn = re.compile('|'.join(['<br><br>', '</p><p>', '<p></p>', '\n']))
    text = re.sub(rn, r"\n", text)
    
    rn = re.compile('|'.join(['＊', '</p>', '<p>', r'\t', '【完】', '<br>\.*', r'\u3000']))
    text = re.sub(rn, "", text)

    print(name)

    fd = open(name + '.txt','w', encoding = 'utf-8')
    fd.write(text)
    fd.close()

    time.sleep(random.randint(0,2))

    now = time.strftime("%Y-%m-%d %H:%M:%S")
    
    f = open('book.md','a', encoding = 'utf-8')
    f.write(name + '\t' + now  +'\n')
    f.close()

def getBookUrl(i, j, url, type_num, num):

    while True:
        try:
            book_html_url = url % (j, i)
            print('\n***** %s *****\n' % book_html_url)
            html = get_html(book_html_url, book_html_url)
            p = [
                r'<a href="(/home/play/38/\d+_\d+.html)" title="(.*?)" .*?data-original="(https://.*?jpg)"',
                r'<a href="(/home/pic/38/\d+_\d+.html)" title="(.*?)" target="_blank">',
                r'<li><a href="(/home/.*?\.html)" .*?<h3>(.*?)</h3>'
                ]
            book_urls = re.findall(p[type_num], str(html), re.S)
            p = r'totalpage= (\d+)'
            # p1 = '(\d+-\d+-\d+)'
            # time = re.findall(p1, str(html), re.S)[0]
            # nowtime = time.strftime('%Y-%m-%d',time.localtime(time.time()))
            num = re.findall(p, str(html))
            flag_i= down_book(book_urls, type_num)
            if not num:
                flag_i = False
            i += 1
            if int(num[0]) < i or flag_i:
            # if int(num[0]) < i:  # frist
                print('*****\%s 下载完毕*****' %dirList1[j - TYPE[type_num] + FileNUM])
                os.remove(dirList1[j - TYPE[type_num] + FileNUM] + '.md')
                j += 1
                if j < TYPE[type_num] + FileTypeNUM:
                    fd = open('../md','w', encoding = 'utf-8')
                    fd.write(str(j - TYPE[type_num] + FileNUM))
                    fd.close()
                    filepath = setpath('/' + dirList1[type_num] + '/' + dirList1[j - TYPE[type_num] + FileNUM])
                    os.chdir(filepath)
                    i = 1
                else:
                    os.remove('../md')
                    break

            fd = open(dirList1[j - TYPE[type_num] + FileNUM] + '.md','w', encoding = 'utf-8')
            fd.write(str(i))
            fd.close()

        except:
            fd = open(r'../er.txt','a', encoding = 'utf-8')
            fd.write('\n类型 = ' + str(j))
            fd.write('\t页数 = ' + str(i))
            fd.close()
            print('///////////////////')
            time.sleep(random.randint(5, 8))
            continue

    print('*****%s 下载完毕*****' % dirList1[type_num])

def down_book(book_urls, num):
    flag = 0
    if os.path.exists('pic.md'):
        fd = open('pic.md','r', encoding = 'utf-8')
        filename = fd.read().split('\n')[-2]
        # print(filename)
        fd.close()
    else:
        filename = ''

    for book_url in book_urls:
        # print(book_url[1])
        name = re.sub('&#\d+;', "", book_url[1])
        name = re.sub('&amp;([gl]t;)?', "&", name).split('作者')[0]

        list1 = ["[", "]", "/", ":", "*", "?", "\"", ",", "\'", "|","《","》","【", "】",'{','}',' ','\\','。']
        for c in list1:
            name = name.replace(c, '')
        if num == BOOK:
            if os.path.exists(name + '.txt'):
                fd = open(r'../cf.txt','a', encoding = 'utf-8')
                fd.write(name + '\t' + book_url[0] + '\n')
                fd.close()
                flag += 1
                if flag > 20 :
                    return True
                print(name + '\t已存在')
                continue
            html = get_html(rootURL, rootURL + book_url[0])
            p = r'<div class="zw">(.*?)</div>'
            text = re.findall(p, str(html), re.S)[0]
            # print(name)
            w_book(name, text)
        else:
            if os.path.exists(name) and name != filename:
                print(name + '\t已存在')
                flag += 1
                if flag > 20 :
                    return True
                continue
            html = get_html(rootURL, rootURL + book_url[0])
            p = [r'(https://.*?m3u8)', r'<img src="(https://.*?)" />']
            img_urls = re.findall(p[num], str(html), re.S)
            # print(img_urls)
            text = img_urls[0]
            fd = open('pic.md','a', encoding = 'utf-8')
            fd.write(name +'\n')
            fd.close()

            path = os.path.join(os.getcwd(), name)
            if not os.path.isdir(path):
                os.mkdir(path)
            print(name)
            if num == IMG:
                w_img(name, img_urls)
            else:
                with open(name + '/' + name + '.txt', 'w') as f:
                    f.write(text) 
                r = requests.get(book_url[2])
                jpg = book_url[2].split('/')[-1]
                with open(name + '/' + jpg, 'wb') as f:
                    f.write(r.content) 

                # w_vedio(name, text, book_url[2])
        # else:
        #     if os.path.exists(name + '.m3u8'):
        #         flag += 1
        #         if flag > 20 :
        #             return True
        #         print(name + '\t已存在')
        #         continue
            
        #     fd = open(r'../cf.txt','a', encoding = 'utf-8')
        #     fd.write(name + '\t' + book_url[0] + '\n')
        #     fd.close()

        #     html = get_html(rootURL, rootURL + book_url[0])
        #     p = r'(https://.*?m3u8)'
        #     text = re.findall(p, str(html), re.S)[0]
        #     print(text)
        #     w_vedio(name, text)
            
    return False

def w_vedio(name, text, url):
    r = requests.get(url).text()
    with open(name + '.m3u8', 'w') as f:
        f.write(r) 

def w_img(name, img_urls):
    j = len(img_urls)
    # print(name)
    for i in range(j):
        img_url = img_urls[i]
        r = requests.get(img_url)
        jpg = img_url.split('/')[-1]
        process_bar((i + 1)/j, total_length = 50)
        # print(jpg)
        with open(name + '/' + jpg, 'wb') as f:
            f.write(r.content) 

    print('\n')

def process_bar(percent, total_length):
    bar = ''.join(["\033[31m%s\033[0m"%'▓'] * int(percent * total_length)) + ''
    bar = '\r' + '进度: {:''>5.1f}%'.format(percent*100) + '  ' + bar.ljust(total_length)
    print(bar, end='', flush=True)

def file_dir(fileDirs):
    dirList = []
    for name, age in zip(range(len(fileDirs)), fileDirs):
        dirList.append(age)
        print(name + 1, ':', age, end="  ")
    num1 = int(input("\n选择数字:")) - 1
    file = fileDirs[dirList[num1]]
    for name, age in zip(range(len(file)), file):
        dirList.append(age)
        print(name + 1, ':', age, end="  ")
    num2 = int(input("\n选择数字:")) + len(fileDirs) - 1

    num3 = int(input("1:顺序 2:一次 \n选择数字:")) - 1

    # 文件名
    filepath = setpath(dirList[num1] + '/' + dirList[num2])
    os.chdir(filepath)

    return num1, num2, num3, dirList, False

def main():
    f_md = False
    num1 = 1
    num2 = 7
    if num2 == 3:
        f_md = True

    num1, num2, num3, dirList1, f_1md = file_dir(fileDir1)
    # print(dirList1)

    file_path, name = os.path.split(fileDir1[dirList1[num1]][dirList1[num2]])
    sh = int(name.split('-')[0]) - num2
    # print(file_path, sh)
    url = rootURL + file_path + '/%s-%s.html'
    filepath = setpath(dirList1[num1] + '/' + dirList1[num2])
    os.chdir(filepath)

    if os.path.exists('../md') and f_md:
        fd = open('../md','r', encoding = 'utf-8')
        num2 = int(fd.read().split('\n')[0])
        fd.close()

        filepath = setpath(dirList1[num1] + '/' + dirList1[num2])
        os.chdir(filepath)

    i = 1
    j = sh + num2

    if os.path.exists(dirList1[num2] + '.md'):
        fd = open(dirList1[num2] + '.md','r', encoding = 'utf-8')
        i = int(fd.read().split('\n')[0])
        fd.close()
    
    getBookUrl(i, j, url, num1, num3)


if __name__ == '__main__':
    main()
    exit()

    # /*****rootPath*****/
    # num1, num2 = file_dir(fileDir)

    num1 = 3
    num2 = 8


    if(num1 > 2 and num2 > 7):
        get_book(num2, fileDir[dirList[num1]][dirList[num2]])
    elif(num1 > 2 and num2 < 8):
        get_book(num2, '/pic/oumei/')
    else:
        pass
