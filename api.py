from flask import Blueprint

simple_page = Blueprint('simple_print', __name__)

@simple_page.route('/')
def index():
    return 'index page'

@simple_page.route('/hello')
def hello():
    return 'index hello'

