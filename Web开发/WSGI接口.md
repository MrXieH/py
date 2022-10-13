# WSGI：Web Server Gateway Interface

```python
# 定义符合WSGI标准的函数
def application(environ, start_response):
    # environ：一个包含所有HTTP请求信息的dict对象；
    # start_response：一个发送HTTP响应的函数。
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'<h1>Hello, web!</h1>']
```

运行WSGI服务

```python
# hello.py
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'<h1>Hello, web!</h1>']


# server.py
# 从wsgiref模块导入:
from wsgiref.simple_server import make_server
# 导入我们自己编写的application函数:
from hello import application


# 创建一个服务器，IP地址为空，端口是8000，处理函数是application:
httpd = make_server('', 8000, application)
print('Serving HTTP on port 8000...')
# 开始监听HTTP请求:
httpd.serve_forever()


$ python server.py
# 访问localhost:8000
```