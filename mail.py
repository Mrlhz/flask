from flask import Flask
from flask_mail import Mail, Message
import os
from threading import Thread

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.163.com'
app.config['MAIL_PORT'] = 25
# app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'email@163.com'
app.config['MAIL_PASSWORD'] = 'password'
app.config['MAIL_DEBUG'] = True
mail = Mail(app)


def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


@app.route('/')
def index():
    msg = Message('来自Flask', sender='lhz_email@163.com', recipients=['1784591401@qq.com'])
    msg.body = '居然就这样毕业了'
    msg.html = '遗憾是难免的'
    thread = Thread(target=send_async_email, args=[app, msg])
    thread.start()

    return '<h1>邮件发送成功</h1>'


if __name__ == '__main__':
    app.run(debug=True)
