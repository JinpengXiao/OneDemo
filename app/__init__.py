'''
这段代码做了什么？
1，首先导入类Flask.这个类的实例化将会是我们的WSGI应用。
  第一个参数是应用模块的名称。如何你使用的是单一的模块，第一个参数应该使用__name__
'''
from flask import Flask

#创建flask这个类的实例，把包名app传递给flask，这样flask才会知道去哪里寻找模块，静态文件等等
app = Flask(__name__)

from app.view import Views
