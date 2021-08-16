# Jinja2

Jinja2 是 Flask 默认使用的模板引擎，也可以被 Django 使用。除了设置变量，还允许在模板中添加 `if` 判断，执行 `for` 迭代，调用函数等，以各种方式控制模板的输出。对 Jinja2 ，模板可以是任何格式的纯文本文件，如 HTML、XML、CSV、LaTeX。Jinja2 用 `render_template()` 函数传入的参数中的相应值替换模版中的 `{{}}` 块。模板也支持在 `{% ％}` 块内使用控制语句。

## 1. 结构

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
    <i>{{user.bio}}</i>} {%else%}}
    <i>This user has not provided a bio.</i>
    {% endif %} {# 下面是电影清单（这是注释）#}
    <h5>{{user.username}}'s Watchlist ({{movies.length}}):</h5>
    <ul>
      {% for movie in movies%}
      <li>{{movie.name}} - {{movie.year}}</li>
      } {% endfor %}
    </ul>
  </body>
</html>
```

模板引擎的作用就是读取并执行模板中的特殊语法标记，并根据传入的数据将变扯替换为实际值，输出最终的 HTML 页面，这个过程被称为渲染（rendering）。

## 2. 继承

Jinja2 有一个模板继承特性，就是将所有模板中相同的部分转移到一个基础模板中，然后再从它继承过来。定义一个名为 `base.html` 的基本模板，其中包含一个简单的导航栏，以及之前实现的标题逻辑。

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    {% if title %}
    <title>{{title}} - Mini Blog</title>
    } {% else %}
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
    <!--检查变量 `messages` 是否包含元素，若有，则在 `<ul>` 元素中，为每条消息用 `<li>` 元素来包裹渲染-->}
    {% if messages %}}
    <ul>
      } {% for message in messages %}
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

## 3. 组件

### 3.1. 导航栏

在基础模板 `templates/base.html` 的导航栏上添加登录的链接，以便访问：

```html
<div>
  <a href="{{url_for('index')}}">Home</a>
  <a href="{{url_for('login')}}">Login</a>
</div>
```
