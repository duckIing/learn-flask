from flask import Blueprint
from flask import render_template
from common.models.user import User

user_page = Blueprint('user_page', __name__, url_prefix='/user/')


@user_page.route('/info/')
def user_page_info():
    user = User.query.first()
    context = {
        'user_id': user.id,
        'user_name': user.name,
        'user_age': user.age,
        'user_address': user.address
    }
    return render_template('hello.html', **context)
