# 所有的程序都需要创建一个示例，
# Web中采用网关接口协议， WSGI(Web Server Gateway Interface)
from flask import Flask, request, current_app, redirect, abort
app = Flask(__name__)
# __name__ 这个参数 用于确定程序的根目录，以便能够找到资源文件的位置
# 路由和视图函数， 客户端将请求发丝东到Web服务器，
# Web 服务器再把请求发给Flask， 处理URL和函数之间的关系叫做路由


# 在处理请求之前或者之后做一些事情， 可以使用钩子
# before_first_request 在处理第一个请求之前运行
# before_request 在每次请求之前运行
# after_request 在每次请求之后运行， 如果没有未处理的异常抛出
# teardown_request 在每次请求之后运行， 即使有未处理的异常抛出


@app.route('/')
# 将修饰函数注册为路由
def index():
    # 由于请求传递的参数是很多的，为了方便，Flask把它们封装在一个对象中
    user_agent = request.headers.get('User-Agent')
    # flask 使用上下文让特定的变量在一个线程中全局可访问，与此同时，又不会影响其他线程
    # flask 包括了请求上下文和应用上下文
    # current_app 代表当前激活的程序实例
    # g 代表一个请求的特定的“钩子”（hook）或者“挂钩”（hook）。
    # request 代表客户端发出的请求对象
    # session 代表用户在一次会话中储存的值
    # 这里还可以传递一个状态码， 默认是200
    # return '<p>Your browser is %s</p>' % user_agent, 200
    # 使用跳转函数
    return redirect('http://www.baidu.com')


@app.route('/user/<name>')
# 动态路由， 尖括号中的内容会作为参数传入函数, 这里可以指定传入的参数类型
# flask支持的类型有： string, int, float, path， 不过path类型的参数会包含斜杠， 将其作为路径的一部分
def user(name):
    return '<h1>Hello, %s!</h1>' % name


@app.route('/post/abort')
def abort_func():
    # 使用abort函数可以立即终止请求处理， 并返回错误响应
    # abort函数接受一个状态码作为参数
    # 返回状态码
    abort(404)
    return '<h1>abort</h1>'

# 可以使用flask-script扩展来管理程序的启动参数


if __name__ == '__main__':
    app.run(debug=True)
    # 服务器启动后， 会进入轮询，等待请求， 一旦收到请求， 就会调用对应的视图函数
    # app.run() 启动开发Web服务器， 用于测试
    # debug=True, 开启调试模式， 服务器会在代码修改后自动载入，并在发生错误时提供一个相对友好的出错页面

