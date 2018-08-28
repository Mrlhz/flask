from flask import Flask, url_for
from flask_sqlalchemy import SQLAlchemy
from api import simple_page
from common.libs.UrlManager import UrlManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@127.0.0.1:3306/wechat_order?charset=utf8'
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = 'a random string'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.debug = True
app.register_blueprint(simple_page, url_prefix="/api")


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


@app.route('/')
def hello_world():
    url = url_for('index')
    version = UrlManager.build_static_url('/css/style.css')
    return 'Hello World!, url:%s, version:%s' % (url, version)


@app.route('/index')
def index():
    from sqlalchemy import text
    sql = text('select * from `user`')
    result = db.engine.execute(sql)
    for row in result:
        print(row)
    print(123)
    return '这是主页'


if __name__ == '__main__':
    app.run(debug=True)
