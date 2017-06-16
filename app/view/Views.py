'''
Created on Jun 10, 2017

@author: xiao jinpeng
'''
from app import app
from flask import request
from flask import make_response
from app.controller import WatsonAPI
import time
from os.path import dirname
from flask.templating import render_template

#使用装饰器route()告诉Flask哪个URL才能触发我们函数
#route()装饰器用于把一个函数绑定到一个URL上
@app.route('/')
def index():
    return 'Hello World'

@app.route('/text2speech')
def text2speech():
    #使用方法render_template()来渲染模版。需要做的是提供模版的名称以及你想要作为关键字参数传入模版的变量
    #Flask将会在templates文件夹中寻找模版
    print('*********testing No.1************')
    return render_template('text2speech.html')

'''
HTTP有不同的方法来访问URLs。默认情况下，路由只会相应GET请求，但是能够通过给route()装饰器
提供methods参数来改变。

'''
@app.route('/dotext2speech',methods=['POST','GET'])
def doText2Speech():
    print('********testing No.2*********')
    if (request.method == 'GET'):
        message = request.args.get('message')
    
    path = dirname(__file__)
    
   
    #以下打印为测试代码，path = C:\Users\IBM_ADMIN\workspace\ProjectForPython\FirstDemo\app\view

    print(message)
    print(path)
    print('******')
    path =path[0:len(path) - 4]
    
    #path = C:\Users\IBM_ADMIN\workspace\ProjectForPython\FirstDemo\app\
    print(path)
    print('****')
    fileName = 'static/tmp/'+str(time.time())+'message.wav'
    
    #想要存在发音频文件的名以及存放在的路径
    #文件名以当前系统时间+'message.wav'的形式命名
    #存放路径是app/static/tmp路径下
    print('filename is :'+fileName)
    
    #调用WatsonAPI（自定义的一个类，存在在controller包下）的文本转语音
    #第一个参数是含有存放路径的文本转语音后生成的音频文件名
    #第二参数是要转换的文本内容
    WatsonAPI.text2speech(fileName=path+fileName, message=message)
    response = make_response(fileName)
    return response

