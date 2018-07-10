# hello.py
# 
'''
def application(environ, start_response):
	# environ：一个包含所有HTTP请求信息的dict对象；
	# start_response：一个发送HTTP响应的函数。
	
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'<h1>Hello, Python web!</h1>']
'''
def application(environ, start_response):
    method = environ['REQUEST_METHOD']
    path = environ['PATH_INFO']
    if method=='GET' and path=='/':
        return handle_home(environ, start_response)
    if method=='POST' and path=='/signin':
        return handle_signin(environ, start_response)
        