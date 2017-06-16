'''
Created on Jun 10, 2017

@author: xiao jinpeng
'''
from app import app
app.debug = True

#用flask类中的run函数启动本地服务器来运行我们的应用
app.run()