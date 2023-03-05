# 所有的程序都需要创建一个示例，
# Web中采用网关接口协议， WSGI(Web Server Gateway Interface)
from flask import Flask

app = Flask(__name__)
app.config["SECRET_KEY"] = "hard to guess string"
# 这个秘钥是用于加密表单的， 用于保护表单免受跨站请求伪造的攻击
# 为了安全起见， 一般不会直接写在代码中， 而是写在配置文件中， 然后从配置文件中读取
# __name__ 这个参数 用于确定程序的根目录，以便能够找到资源文件的位置
# 路由和视图函数， 客户端将请求发丝东到Web服务器，
# Web 服务器再把请求发给Flask， 处理URL和函数之间的关系叫做路由


@app.route('/')
# 将修饰函数注册为路由
def index():
    # index 这种称为视图函数
    return '<h1>Hello World!</h1>'


@app.route('/user/<name>')
# 动态路由， 尖括号中的内容会作为参数传入函数, 这里可以指定传入的参数类型
# flask支持的类型有： string, int, float, path， 不过path类型的参数会包含斜杠， 将其作为路径的一部分
def user(name):
    return '<h1>Hello, %s!</h1>' % name


if __name__ == '__main__':
    app.run(debug=True)
    # 服务器启动后， 会进入轮询，等待请求， 一旦收到请求， 就会调用对应的视图函数
    # app.run() 启动开发Web服务器， 用于测试
    # debug=True, 开启调试模式， 服务器会在代码修改后自动载入，并在发生错误时提供一个相对友好的出错页面

