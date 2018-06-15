import os
from threading import Thread
from datetime import datetime
from flask import Flask, render_template, session, flash, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail, Message

from form import NameForm

# from models import User

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite3')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# 邮件设置
app.config['MAIL_SERVER'] = 'smtp.163.com'
app.config['MAIL_PORT'] = 25
# app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'email@163.com'
app.config['MAIL_PASSWORD'] = 'password'
app.config['MAIL_DEBUG'] = True

bootstrap = Bootstrap(app)
moment = Moment(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
mail = Mail(app)


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role')

    def __repr__(self):
        return '<Role %r>' % self.name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' % self.username


def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


def send_email():
    """
    :param to: 收件人地址
    :param subject: 主题
    :param template: 渲染邮件正文的模板
    :param kwargs: 和关键字参数列表
    :return:
    """
    msg = Message('来自Flask', sender='send@163.com', recipients=['receive@qq.com'])
    msg.body = '你好吗'
    msg.html = '静下心学你的'
    thread = Thread(target=send_async_email, args=[app, msg])
    thread.start()

    return '<h1>邮件发送成功</h1>'


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    form_name = form.name.data
    if form.validate_on_submit():
        user = User.query.filter_by(username=form_name).first()
        if user is None:
            user = User(username=form_name)
            db.session.add(user)
            db.session.commit()
            flash('Successful addition of new users!')
            session['known'] = False
            send_email()
        else:
            session['known'] = True
        session['name'] = form.name.data
        form.name.data = ''  # 清空表单字段
        return redirect(url_for('index'))
    return render_template('index.html',
                           current_time=datetime.utcnow(),
                           form=form,
                           name=session.get('name'),
                           known=session.get('known', False)
                           )


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


if __name__ == "__main__":
    app.run(debug=True)
