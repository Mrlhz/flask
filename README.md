# Flask+Web开发：基于Python的Web应用开发实战

## 下载依赖包
在虚拟环境中使用pip生成requirements.txt：
```
(venv) $ pip freeze > requirements.txt
```
当需要创建这个虚拟环境的完全副本，可以创建一个新的虚拟环境，并在其上运行以下命令：

```
(venv) $ pip install -r requirements.txt
```
## 使用豆瓣源 

```
pip install -i https://pypi.douban.com/simple/ flask django==1.11.6
```
```
pip install -r requirements.txt -i https://pypi.douban.com/simple/
```
## 运行django项目 
```
python manage.py runserver
```
## python启动一个本地服务器
```
python -m http.server [8000]
```
## pipenv(官方推荐)
```
在C盘mkdir env_anme 
pipenv install
pip shell
退出：exit
下载：pipenv flask 或 pip install flask

cd C:\Users\crystal\pipenvs 进入
pipenv shell

exit 退出
```
# 查看虚拟环境位置
```
pipenv --venv

C:\Users\crystal>cd C:\Users\crystal\pipenvs

C:\Users\crystal\pipenvs>pipenv --venv
C:\Users\crystal\.virtualenvs\pipenvs-twBDG695

C:\Users\crystal\pipenvs>
```

# 入口文件
```
if __name__ == '__main__':
# 生产环境下一般用 nginx + uwsgi
# 保证在生产环境下不会启动内置Web服务器
```
# Flask学习笔记
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

> '<h1>Hello</h1>' => '&lt;h1&gt;Hello&lt;h1&gt;'

## 控制结构

## Web表单
### 跨站请求伪造保护(CSRF)

## 数据库

```
(venv)python
>>>from models import db
>>>db.create_all() #创建数据库表
```
```
# 删除旧表，数据都销毁了
db.drop_all()
```
```
# 创建一些角色和用户
>>> from FlaskBlog import Role, User 
>>> admin_role = Role(name='Admin') 
>>> mod_role = Role(name='Moderator') 
>>> user_role = Role(name='User') 
>>> user_tom = User(username='tom', role=admin_role) 
>>> user_Aragaki = User(username='新垣结衣', role=user_role) 
```
> 数据库会话管理对数据库所做的改动，在 Flask-SQLAlchemy 中，会话由 db.session
表示

```
# 方式一
db.session.add(admin_role) 
```
```
# 方式二
db.session.add_all([admin_role, mod_role, user_role, user_tom, user_Aragaki, user_david])
```
```
# 提交
db.session.commit()
```
```
数据库会话回滚。调用 db.session.rollback() 
```
```
# 修改行
>>> admin_role.name = 'Administrator' 
>>> db.session.add(admin_role) 
>>> db.session.commit()
```

