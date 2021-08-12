# Flask 与 HTTP

## 1. 架构

### 1.1. 初始化

在 `app/__init__.py` 中导入的类 `Flask` ，并以此类创建了一个应用程序对象。传递给 `Flask` 类的 `__name__` 变量是一个 Python 预定义的变量。

`app` 包由*app*目录和 `__init__.py` 脚本来定义构成，并在 `from app import routes` 语句中被引用。 `app` 变量被定义为 `__init__.py` 脚本中的 `Flask` 类的一个实例，以至于它成为 `app` 包的属性。

`routes` 模块是应用程序实现的不同 URL。在 Flask 中，应用程序路由的处理逻辑被编写为 Python 函数，称为*视图函数*。 视图函数被映射到一个或多个路由 URL，以便 Flask 知道当客户端请求给定的 URL 时执行什么逻辑。

> `routes` 模块是在底部导入的，而不是在脚本的顶部。 最下面的导入是解决*循环导入*的问题，这是 Flask 应用程序的常见问题。

```python
from flask import Flask
from config import Config

# 当前调用它的模块的名字
app = Flask(__name__)
app.config.from_object(Config)

from app import routes, models
```

### 1.2. 路由

在一个 Web 应用里，客户端和服务器上的 Flask 程序的交互可以简单概括为以下几步：

1. 用户在浏览器输入 URL 访问某个资源
2. Flask 接收用户请求并分析请求的 URL
3. 为这个 URL 找到对应的处理函数
4. 执行函数并将其返回值生成响应，返回给浏览器
5. 浏览器接收并解析响应，将信息显示在页面中

上面这些步骤，大部分都由 Flask 完成，我们要做的只是建立处理请求的函数，并为其定义对应的 URL 规则，只在 `app/routes.py` 中使用 `@app.route` 修饰器在作为参数给出的 URL 和函数之间创建一个关联，这个过程我们称为注册路由。

路由负责管理 URL 和函数之间的映射，而这个函数则被称为视图函数（view function）。在下面的程序里， `@app.route` 把地址 `/index` 和 `index()` 函数绑定起来，当用户访问这个 URL 时就会触发 `index()` 函数。

```python
from app import app
from flask import render_template

# 绑定多个地址
@app.route('/')
@app.route('/index')
def index():
  return '<h1>Hello, World! </h1>'

# 绑定动态地址
@app.route('/greet/<name>')
def greet(name):
  return '<h1>Hello, World!</h1>' % name

# 设置默认值
@app.route('/greet', defaults= {'name':'Programmer'})
@app.route('/greet/<name>')
def greet(name):
  return '<h1>Hello, World!</h1>' % name
```

### 1.3. 环境变量

`.flaskenv` 用于存储和 Flask 相关的公开环境变； `.env` 用于存储包含敏感信息的环境变量，如后面用于配 Email 服务器的账户名与密码。

`.env` 包含敏感信息，除非是私有项目，否则绝对不能提交到 Git 仓库中。当你开发一个新项目时，记得把它的名称添加到 `.gitignore` 文件中，这会告诉 Git 忽略这个文件。

- .flaskenv

```sh
FLASK_APP=[app_name].py
FLASK_ENV=development
```

### 1.4. 启动

服务启动后将处于阻塞监听状态，将等待客户端连接。部署在生产 Web 服务器上的应用程序通常会在端口 443 上进行监听，若不执行加密，则有时会监听 80，但启用这些端口需要 root 权限。 由于此应用程序在开发环境中运行，因此 Flask 使用自由端口 5000。

执行 `flask run` 命令时的 `host` 和 `port` 选项也可以通过环境变量 `FLASK_RUN_HOST` 和 `FLASK_RUN_PORT` 设置。事实上，Flask 内置的命令都可以使用这种模式定义默认选项值，即 `FLASK_<COMMAND>_<OPTION>` 。

```bash
flask run
# 对外可见
flask run -- host=0.0.0.0
# 改变端口
flask run --port=8000
```

打开浏览器并在地址栏中输入以下 URL

- `http://localhost:5000/`
- `http://localhost:5000/index`

### 1.5. 开发环境

- 调试器

`Werkzeug` 提供的调试器非常强大，当程序出错时，我们可以在网页上看到详细的错误追踪信息，这在调试错误时非常有用。调试器允许你在错误页面上执行 Python 代码。

- 重载器

在对代码做了修改后，期望的行为是这些改动立刻作用到程序。重载器的作用就监测文件变动，然后重新启动开发服务器。默认会使用 `Werkzeug` 置的 `stat` 重载器，它的缺点是耗电较严重，而且准确性一般。为了获得更优秀的体验，可以安装 `Watchdog` ， `Werkzeug` 会自动使用它来监测文件变动。

- config.py

`SECRET_KEY` 是 `config.py` 中添加的唯一配置选项，对大多数 Flask 应用于说，它均是极其重要的。Flask 及其一些扩展使用密钥的值作为加密密钥，用于生成签名或令牌。

```python
app.config.update(
  TESTING=True,
  SECRET_KEY='_S#yF4Q8z\n\xec]/'
)
```

## 2. 请求

当用户在浏览器的地址栏中输入一个 URL 并按回车键之后，浏览器会发送一个请求去获取请求网站的 HTML 文件，服务器把响应文件对象发送回给浏览器。

- 浏览器分析响应中的 HTML，发现其中引用了很多其他文件，如 CSS 文件，JS 文件
- 浏览器会自动再次发送请求去获取图片，CSS 文件，或 JS 文件
- 当所有的文件都下载成功后，网页会根据 HTML 语法结构，完整的显示出来

![workflow](images/ch8/flask_workflow.png)

### 2.1. 请求方法

HTTP/1.1 指示使用的 HTTP 协议版本是 1.1，有如下方法；

| 请求方式 |     作用     |        备注         |
| :------: | :----------: | :-----------------: |
|   GET    |   获取资源   |   多用于搜索引擎    |
|   POST   |   数据交互   |     多用于爬虫      |
|   PUT    |  存储并覆盖  |   多用于传输文件    |
|  DELETE  |     删除     | 删除 URL 位置的资源 |
|   HEAD   |   返回报头   |                     |
|  PATCH   | 询问某种支持 |                     |

当某个请求的方法不符合要求时，请求将无法被正常处理。如，在提交表单时通常使用 POST 方法， 而若提交的目标 URL 应的视图函数只允许 GET 方法， Flask 会自动返回 405 响应 (Method Not Allowed）。

```python
@app.route('/hello', methods= ['GET', 'POST'])
def hello():
  return '<h1>Hello Flask !</h1>'
```

### 2.2. 变量变换

```python
# 整型变换器
@app.route('goback/<int:year>')
def go_back(year):
  return f'<p>Welcome to {(2018 - year)} !</p>'

# any 变换器
# 若将 color 替换为 any 变换器中设置的可选值以外的任意字符，均会获得 404 错误响应。
@app.route('/colors/<any(blue, white, red):color>')
def three_colors(color):
  return '<p>Love is patient and kind. Love is not jealous or boastful or proud or rude.</p>'

# any 变换器，列表形式
colors = ['blue', 'white', 'red']
@app.route(f'/colors/<any({str(colors)[1:-1]}):color>')
```

### 2.3. 请求钩子

当请求需要预处理和后处理时，可以使用 Flask 提供当一些钩子（Hook），它们可以用来注册在请求处理的不同阶段执行的处理函数（回调函数）。

- `before_first_request` ，在处理第一个请求前运行一个函数。用于在程序中，运行程序前我需要进行些程序的初始化操作，如创建数据库表，添加管理员用户。
- `before_request`：在处理每个请求前运行一个函数。用于诸如网站上要记录用户最后在线的时间，可以通过用户最后发送请求时间来实现。
- `after_request`：在每个请求结束后运行一个函数（若没有异常抛出的话）。用于经常在视图函数中进行数据库的操作，如更新、插入，之后需要将更改提交到数据库中。
- `teardown_request`：在每个请求结束后，使一个函数有未处理的异常抛出，若发生异常，会传入异常对象作为参数到注册的函数中。
- `after_this_request`：在这个请求结束后运行一个函数。

![hooks](images/ch8/flask_hooks.png)

### 2.4. 请求报文

请求报文的组成主要有

- 请求行
- 请求头部
- 空行
- 请求数据

|          条目           |                     作用                     |
| :---------------------: | :------------------------------------------: |
|          Host           |      对应网址 URL 中的 Web 名称和端口号      |
|       Connection        |           表示客户端与服务连接类型           |
| Upgrade-Insecure-请求 s |    加载 HTTP 资源时自动替换成 HTTPS 请求     |
|       User-Agent        |               客户浏览器的名称               |
|         Accept          | 浏览器或其他客户端可接受的 MIME 文件类型格式 |
|         Referer         |       表明产生请求的网页来自于哪个 URL       |
|     Accept-Encoding     |            浏览器可接受的编码方式            |
|     Accept-Language     |            浏览器可接受的语言种类            |
|     Accept-Charset      |            浏览器可接受的字符编码            |
|         Cookie          |          在浏览器中寄存的小型数据体          |
|      Content-Type       |        POST 请求里用于表示的内容类型         |

## 3. 响应

响应报文的组成主要有

- 响应头部（Response Header）
  - 协议版本
  - 状态码（Status Code）
  - 原因短语
- 空行
- 响应主体（Response Body），可选项，是 HTML 源码

- 状态码

| 状态码 |  信息类别  |                 解释                 |
| ------ | :--------: | :----------------------------------: |
| 1xx    |    消息    |     请求已被服务器接收，继续处理     |
| 2xx    |    成功    | 请求已成功被服务器接收、理解、并接受 |
| 3xx    |   重定向   |     需要后续操作才能完成这一请求     |
| 4xx    |  请求错误  |    请求含有词法错误或者无法被执行    |
| 5xx    | 服务器错误 |  服务器在处理某个正确请求时发生错误  |

### 3.1. 响应方法

视图函数可以返回最多由三个元素组成的响应主体：响应主体、状态码、头部字段。其中，头部字段可以为字典，或是两元素元组组成的列表。

```python
from flask import Flask, abort
# 指定状态码
@app.route('/hello')
def hello():
    return '<h1>Hello, Flask !</h1>', 201

# 错误响应
@app.route('/404')
def not_found():
    abort(404)
```

### 3.2. 响应报文

HTTP 响应中，数据可以通过多种格式传输。多数情况下，使用 HTML 格式，这也是 Flask 中的默认设置。在特定的情况下，也使用其他格式。不同的响应数据格式需要设置不同的 MIME 类型，MIME 型在首部的 `Content-Type` 字段中定义。

MIME 类型是一种用来标识文件类型的机制，它与文件扩展名相对应，可以让客户瑞区分不同的内容类型，并执行不同的操作。一般的格式＂类型名／子类型名"，其中的子类型名一般为文件扩展名。如，HTML MIME
型为 `text/html` ，png 图片的 MIME 类型 `image/png` 。详见 [标准 MIME 类型列表](https://www.iana.org/assignments/media-types/media-types.xhtml)

```python
from flask import mark_response

@app.route('/foo')
def foo():
    response = mark_response('Hi')
    # 指定 MIME 类型
    response.mimetype = 'text/plain'
    return response

from flask import jsonify

@app.route('/foo')
def foo():
    # json 化
    return jsonify({
      name:'Grey Li',
      gender:'male'
     })
```

|       条目        |                       作用                       |
| :---------------: | :----------------------------------------------: |
|   Cache-Control   |   这个值告诉客户端，服务端不希望客户端缓存资源   |
|    Connection     |                    keep-alive                    |
| Content-Encoding  |            服务端发送的资源使用的编码            |
|   Content-Type    |           资源文件的类型，还有字符编码           |
|       Date        |           服务端发送资源时的服务器时间           |
|      Expires      |         在这个时间前，以直接访问缓存副本         |
| Pragma: no-cache  |            含义与 Cache-Control 等同             |
|      Server       |               服务器和相对应的版本               |
| Transfer-Encoding |              服务器发送的资源的方式              |
|       Vary        | 告诉缓存服务器，缓存压缩文件和非压缩文件两个版本 |

### 3.3. Cookie

Cookie 在 Web 程序中发挥了很大作用，最重要的功能是存储用户的认证信息。 `set_cookie()` 用来设置 Cookie，它会 URL 中的 `name` 变量的值设置到名为 `name` 的 Cookie 里。

```python
from flask import Flask, make_response

@app.route('/set/<name>')
def set_cookie(name):
    response=make_response(redirect(url_for('hello')))
    response=set_cookie('name', name)
    return response
```

然而，这会带来一个问题，在浏览器中手动添加和修改 Cookie 是很容易的事，仅仅通过浏览器插件就可以实现。为了避免这个问题，需要对敏感 Cookie 容进行加密。于是，就有了 Session，即加密的 Cookie。

安全的做法是把密钥写进系统环境变量里（在命令行中使用 `export` 命令），或是保存在 `.env` 文件中：

```env
SECRET_KEY=secret string
```

然后在程序脚本中使用 OS 模块提供的 `getenv()` 方法获取

```python
import os

app.secret_key = os.getenv('SECRET_ KEY', 'secret string')
```

### 3.4. 登录

- 登录

```python
from flask import redirect, session, url_for

@app.route('/login')
def login():
    session['logged_in'] = True  #写入 session
    return redirect(url_for('hello'))
```

- 登录后

```python
from flask import request, session

@app.route('/')
@app.route('/hello')
def hello():
    name = request.args.get('name')
    if name is None:
        name = request.cookies.get('name', 'Human')
        response = f'<h1>Hello, {name} !</h1>'  # 根据用户认证状态返回不同的内容
        if 'logged_in' in session:
            response = '[Authenticated]'
        else:
            response += '[Not Authenticated]'
        return response
```

- 登出

```python
from flask import session

@app.route('/logout')
def logout():
    if 'logged_in' in session:
        session.pop('logged_ in')
    return redirect(url_for('hello'))
```

- 后台管理

```python
from flask import session, abort

@app.route('/admin')
def admin():
    if 'logged_in' not in session:
        abort(403)
    return 'Welcome to admin page.'
```

## 4. 重定向

在复杂的应用场景下，需要在用户访问某个 URL 重定向到上一个页面最常见的情况是，用户单击某个需要登录才能访问的链接，这时程序会重定向到登录页面，当用户登录后合理的行为是重定向到用户登录前浏览的页面，以便用户执行未完成的操作，而不是直接重定向到主页。

```python
from flask import Flask, redirect, url_for

@app.route('/hello')
def hello():
    # redirect() 默认状态码为 302，即临时重定向，其第二个参数可以指定状态码
    return redirect('http://www.example.com')

# 重定向到其他视图
@app.route('/hi')
def hi():
    return redirect(url_for('hello'))
```

### 4.1. 返回上一个页面

HTTP referer，是一个用来记录请求发源地址的 HTTP 首部字段，即访问来源，起源为 referrer 在 HTTP 规范中的错误拼写。当用户在某个站点单击链接，浏览器向新链接所在的服务器发起请求，请求的数据中包含的 `HTTP_REFERER` 字段记录了用户所在的原站 URL。这个值通常会用来追踪用户，如记录用户进入程序的外部站点，以此来更有针对性地进行营销。Flask 中，referer 的值可以通过请求对象的 referrer 属性获取，即 `request.referrer` 。

```python
@app.route('/foo')
def too():
  return f'<h1>Foo page</h1><a href="{url_for('do_something', next＝request.full_path)}" >Do something and redirect</a>'

@app.route('/bar')
def bar():
  return f'<h1>Bar page</h1><a href="{url_for('do_something', next＝request.full_path)}" >Do something and redirect</a>'

def redirect_back(default='hello', **kwargs):
  for targe in request.args.get('next'), request.referrer:
    if target:
      return redirect(target)
    return redirect(url_for(default, **kwargs))

@app.route('/do something and redirect')
def do_something():
  # do something
  return redirect_back()
```

### 4.2. 安全

虽然已经实现了重定向回上一个页面的功能 但安全问题不容小觑，鉴于 `referer` 和 `next` 容易被篡改的特性，若不对这些值进行验证，会形成开放漏洞。

```python
from urllib.parse import urlparse, urljoin
from flask import request

def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http',
                               'https') and ref_url.netloc == test_url.netloc
```

在执行重定向回上个页面的 `redirect_back()` 函数中，使用 `is_safe_url` 验证 `next` 和 `referer` 的值。

```python
def redirect_back(default='hello', **kwargs):
    for target in request.args.get('next'), request.referrer:
        if not target:
            continue
        if is_safe_url(target):
            return redirect(target)
        return redirect(url_for(default, **kwargs))
```

## 5. 上下文

### 5.1. 全局变量

在多线程服务器中，在同一时间可能会有多个请求在处理。假设有多个客户端同时向服务器发送请求，这时每个请求都有各自不同的请求报文，故请求对象也必然是不同的 因此，请求对象只在各自的线程内是全局的。Flask 通过本地线程（thread local）技术将请求对象在特定的线程和请求中全局可访问。

为了方便获取这两种上下文环境中存储的信息，Flask 提供了四个上下文全局变量。

- 上下文
  - 程序
    - `current_ app`：指向处理请求的当前程序实例
    - `g`：替代 Python 全局变量用法，确保仅在当前请求中可用。用于存储全局数据，每次请求都会重置。
  - 请求
    - `request`：封装客户端发出的请求报文数据
    - `session`：记住请求之间的数据，通过签名的 Cookie 实现

### 5.2. 激活、钩子

当请求进入时，Flask 会自动激活请求上下文，这时可以使用 `request` 和 `session` 变量。另外，当请求上下文被激活时，程序上下文也被自动激活。当请求处理完毕后，请求上下文和程序上下文也会自动销毁，也就是说，在请求处理时这两者拥有相同的生命周期。

在使用 flask shell 打开的 Python Shell 中，或是自定义的 flask 命令函数中，可以使用 `current_app` ，也可以手动激活请求上下文来使用 `request` 和 `session` 变量。

- 程序上下文

```python
from app import app
from flask import current_app

with app.app_context():
  current_app.name
```

- 请求上下文

```python
from app import app
from flask import request

with app.test_request_context('/hello'):
  request.method
```

Flask 也为上下文提供了 `teardown_appcontext` 钩子，使用它注册的回调函数会在程序上下文被销毁时调用，而且通常也会在请求上下文被销毁时调用。如，你需要请求处理结束后销毁数据库连接。使用 `teardown_appcontext` 装饰器注册的回调函数需要接收异常对象作为参数，当请求被正常处理时这个参数值将是 `None` , 这个函数的返回值将被忽略。

```python
@app.teardown_appcontext
def teardown_db(exception):
  db.close()
```

## 6. 异步请求

- 纯文本或局部 HTML 模板

纯文本可以在 JavaScript 用来直接替换页面中的文本值，而局部 HTML 则可以直接到插入页面中，如返回评论列表。

```python
@app.route('/comments/<int:post_id>')
def get_comments(post_id):
  return render_template('comments.html')
```

- JSON 数据

JSON 据可以 JavaScript 直接操作

```python
@app.route('/profile/<int:user_id>')
def get_profile(user_id):
  return jsonify(username=username, bio=bio)
```

- 空值

有些时候，程序中的某些接收 AJAX 请求的视图并不需要返回数据给客户端，如用来删除文章的视图。这时我们可以直接返回空值，并将状态码指定为 204（表示无内容），如：

```python
@app.route ('/post/delete/<int:post_ id>', methods= ['DELETE'])
def delete_post(post_id):
  return '', 204
```
