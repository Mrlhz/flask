# Flask+Web开发：基于Python的Web应用开发实战

## Jinja2模板引擎

### 模板标签
| 过滤器名  |      说  明       |
| :---------| ------------------|
|safe       | 渲染值时不转义    |
|capitalize | 把值的首字母转换成大写，其他字母转换成小写
|lower      | 把值转换成小写形式|
|upper      | 把值转换成大写形式
|title      | 把值中每个单词的首字母都转换成大写
|trim       | 把值的首尾空格去掉
|striptags  | 渲染之前把值中所有的 HTML 标签都删掉

## 控制结构

## Web表单
### 跨站请求伪造保护(CSRF)

## 数据库

```
(venv)python
>>>from models import db
>>>db.create_all() #创建数据库表
```