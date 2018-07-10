#beautiful_pic.py
#py脚本同目录下建立一个static目录存放图片

from flask import Flask
from flask import request
from flask import render_template
import os

app = Flask(__name__)

#显示所有文件夹
@app.route('/',methods=['GET','POST'])
def list_all():
    path = './static/mzitu/'
    all_pic = os.listdir(path)
    return render_template('welcome.html',all_pic = all_pic)

#具体展示图片
@app.route('/<path>',methods=['GET','POST'])
def list_pic(path):
    #错误链接无法找到图片目录就提示错误链接
    if(path not in os.listdir('./static/mzitu/')):
        return render_template('error.html')
    pic_path = './static/mzitu/' + path
    all_pic = -1
    if not os.path.isfile(pic_path):
        all_pic = os.listdir(pic_path)
    return render_template('pic.html',title = path,all_pic = all_pic)

if __name__ == '__main__':
    #port为端口，host值为0.0.0.0即不单单只能在127.0.0.1访问，外网也能访问
    app.run(host='0.0.0.0',port='2333')