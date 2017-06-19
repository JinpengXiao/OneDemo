'''
Created on Jun 10, 2017

@author: xiao jinpeng
'''
from app import app

app.debug = True
'''
当Python解释器读.py文件，它会执行它发现的所有代码。在执行代码之前，他会定义一些变量。
例如，如果这个py文件就是主程序，他会设置__name__变量为“__main__”.
如果这个py被引入到别的模块，__name__会被设置为该模块的名字。
'''
if __name__ == '__main__':
    # 用flask类中的run函数启动本地服务器来运行我们的应用
    #程序实例用run方法启动Flask继承的开发web服务器，服务器启动后，会进入轮询，等待并处理请求。
    #轮询会一直进行，直到程序停止，比如按ctrl-c建。
    app.run()
