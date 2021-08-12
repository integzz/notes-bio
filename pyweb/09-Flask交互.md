# Flask 交互

## 1. 模板

网站需要模板（template）和静态文件（static file）来生成更加丰富的网页。

- 模板：包含程序页面的 HTML 文件
- 静态文件：需要在 HTML 文件中加载的 CSS，JavaScript 脚本，以及图片、字体等资源文件

默认情况下，模板文件存放在项目根目录中的 `templates` 文件夹中，静态文件存放在 `static` 文件夹中，这两个文件夹需要和包含程序实例的模块处于同一个目录下。

### 1.1. Jinja2

Flask 默认使用的模板引擎是 Jinja2，一个功能齐全的 Python 模板引擎，除了设置变量，还允许我们在模板中添加 `if` 判断，执行 `for` 迭代，调用函数等，以各种方式控制模板的输出。对 Jinja2 ，模板可以是任何格式的纯文本文件，如 HTML、XML、CSV、LaTeX。Jinja2 用 `render_template()` 函数传入的参数中的相应值替换模版中的 `{{}}` 块。模板也支持在 `{% ％}` 块内使用控制语句。

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <title>{{user.username}}'s Watchlist</title>
  </head>
  <body>
    <a href=" {{url for ('index')}}">&larr; Return</a>
    <h2>{{user.username}}</h2>
    {% if user.bio %}
    <i>{{user.bio}}</i>
    {%else%}
    <i>This user has not provided a bio.</i>
    {% endif %} {# 下面是电影清单（这是注释）#}
    <h5>{{user.username}}'s Watchlist ({{movies.length}}):</h5>
    <ul>
      {% for movie in movies%}
      <li>{{movie.name}} - {{movie.year}}</li>
      {% endfor %}
    </ul>
  </body>
</html>
```

模板引擎的作用就是读取并执行模板中的特殊语法标记，并根据传入的数据将变扯替换为实际值，输出最终的 HTML 页面，这个过程被称为渲染（rendering）。为了渲染模板，需要在 `app/routes.py` 中从 Flask 框架中导入 `render_template()` 函数。该函数需要传入模板文件名和模板参数的变量列表，并返回模板中所有占位符都用实际变量值替换后的字符串结果。

```python
from flask import Flask, render_template

@app.route('/watchlist')
def watchlist():
    return render_template('watchlist.html', user=user, movies=movies)

user = {'username': 'Li', 'bio': 'A boy who loves movies.'}

movies = [
    {
        'name': 'Perfect Blue',
        'year': '1997'
   },
    {
        'name': 'The Matrix',
        'year': '1999'
   },
    {
        'name': 'Memento',
        'year': '2000'
   },
    {
        'name': 'The Bucket list',
        'year': '2007'
   },
]
```

渲染后返回的结果为

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <title>Li's Watchlist</title>
  </head>
  <body>
    <a href="/">&larr; Return</a>
    <h2>Li</h2>
    <i>A boy who loves movies.</i>
    <h5>Li's Watchlist (4) :</h5>
    <ul>
      <li>Perfect Blue - 1997</li>
      <li>The Matrix - 1999</li>
      <li>Memento - 2000</li>
      <li>The Bucke list - 2007</li>
    </ul>
  </body>
</html>
```

### 1.2. 辅助工具

### 1.3. 继承

Jinja2 有一个模板继承特性，就是将所有模板中相同的部分转移到一个基础模板中，然后再从它继承过来。定义一个名为 `base.html` 的基本模板，其中包含一个简单的导航栏，以及之前实现的标题逻辑。

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    {% if title %}
    <title>{{title}} - Mini Blog</title>
    {% else %}
    <title>Mini Blog</title>
    {% endif %}
  </head>
  <body>
    <div>
      Microblog:
      <a href="/index">Home</a>
      <a href="/login">Login</a>
    </div>
    <hr />
    <!-- 返回用 flash() 注册过的消息列表-->
    <!--闪现消息的一个有趣的属性是，一旦通过 `get_flashed_messages` 函数请求了一次，它们就会从消息列表中移除-->
    {% with messages = get_flashed_messages() %}
    <!--检查变量 `messages` 是否包含元素，若有，则在 `<ul>` 元素中，为每条消息用 `<li>` 元素来包裹渲染-->
    {% if messages %}
    <ul>
      {% for message in messages %}
      <li>{{message}}</li>
      {% endfor %}
    </ul>
    {% endif %} {% endwith %} {% block content %}{% endblock %}
  </body>
</html>
```

通过从基础模板 `base.html` 继承 HTML 元素，可简化模板 `index.html` 了。

```html
{% extends "base.html" %} {% block content %}
<h1>Hi, {{user.username}}!</h1>
{% for post in posts %}
<div>
  <p>{{post.author.username}} says: <b>{{post.body}}</b></p>
</div>
{% endfor %} {% endblock %}
```

### 1.4. 导航栏

在基础模板 `templates/base.html` 的导航栏上添加登录的链接，以便访问：

```html
<div>
  <a href="{{url_for('index')}}">Home</a>
  <a href="{{url_for('login')}}">Login</a>
</div>
```

## 2. 表单

### 2.1. Flask-WTF

`Flask-WTF` 使用它来保护网页表单免受名为 [Cross-Site Request Forgery] 或 CSRF 的恶意攻击。顾名思义，密钥应该是隐密的，因为由它产生的令牌和签名的加密强度保证，取决于除了可信维护者之外，没有任何人能够获得它。

`__init__.py`

```python
import os

class Config(object):
  SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
```

### 2.2. 表单调用

在 `app/forms.py` 中调用 `Flask-WTF` ，使用类来表示 Web 表单。表单类只需将表单的字段定义为类属性即可。

由于 `Flask-WTF` 本身不提供字段类型，因此从 `WTForms` 中导入了四个表示表单字段的类。每个字段类都接受一个描述或别名作为第一个参数，并生成一个实例来作为 `LoginForm` 的类属性。

```python
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
  # validators 验证输入字段是否符合预期
  # DataRequired 仅验证字段输入是否为空
  username = StringField('Username', validators=[DataRequired()])
  password = PasswordField('Password', validators=[DataRequired()])
  remember_me = BooleanField('Remember Me')
  submit = SubmitField('Sign In')
```

### 2.3. 表单渲染

在 `LoginForm` 类中定义的字段支持自渲染为 HTML 元素，将把登录模板存储在文件 `app/templates/login.html` 中。这个模板需要一个 form 参数的传入到渲染模板的函数中，form 来自于 `LoginForm` 类的实例化。

```html
{% extends "base.html" %} {% block content %}
<h1>Sign In</h1>
<form action="" method="post" novalidate>
  {{form.hidden_tag()}}
  <p>
    {{form.username.label}}<br />
    {{form.username(size=32)}}
  </p>
  <p>
    {{form.password.label}}<br />
    {{form.password(size=32)}}
  </p>
  <p>{{form.remember_me()}} {{form.remember_me.label}}</p>
  <p>{{form.submit()}}</p>
</form>
{% endblock %}
```

`form.hidden_tag()` 模板参数生成了一个隐藏字段，其中包含一个用于保护表单免受 CSRF 攻击的 `token` 。对于保护表单，你需要做的所有事情就是在模板中包括这个隐藏的字段，并在 Flask 配置中定义 `SECRET_KEY` 变量，Flask-WTF 会完成剩下的工作。

表单的字段对象的在渲染时会自动转化为 HTML 元素，故只需在需要字段标签的地方加上 `{{form.<field_name>.label}}` ，需要这个字段的地方加上 `{{form.<field_name>()}}` 。对于需要附加 HTML 属性的字段，可作为关键字参数传递到函数中。 此模板中的 username 和 password 字段将 `size` 作为参数，将其作为属性添加到 `<input>` HTML 元素中。 你也可通过这种手段为表单字段设置 class 和 id 属性。

### 2.4. 表单视图

函数的逻辑只需创建一个 form 实例，并将其传入渲染模板的函数中即可，然后用*/login* URL 来关联它。这个视图函数也存储到 `app/routes.py` 模块中。

```python
from flask import render_template, flash, redirect
from app import LoginForm

# 覆盖默认的 GET
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    # 执行 form 校验的工作
    if form.validate_on_submit():
        flash(
            f'Login requested for user {form.username.data}, remember_me={form.remember_me.data}.'
        )
        # 指引浏览器自动重定向到它的参数所关联的 URL
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
```

### 2.5. 登录模版

```html
{% extends "base.html" %} {% block content %}
<h1>Sign In</h1>
<form action="" method="post" novalidate>
  {{form.hidden_tag()}}
  <p>
    {{form.username.label}}<br />
    {{form.username(size=32)}}<br />
    {% for error in form.username.errors %}
    <span style="color: red">[{{error}}]</span>
    {% endfor %}
  </p>
  <p>
    {{form.password.label}}<br />
    {{form.password(size=32)}}<br />
    {% for error in form.password.errors %}
    <span style="color: red">[{{error}}]</span>
    {% endfor %}
  </p>
  <p>{{form.remember_me()}} {{form.remember_me.label}}</p>
  <p>{{form.submit()}}</p>
</form>
{% endblock %}
```

## 3. 电子邮件
