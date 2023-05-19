from flask import request
from flask import Blueprint
from flask import render_template
from common.libs.render_help import ops_render_json
from common.libs.render_help import ops_render_error_json
from common.models.user import User
from common.libs.user_services import encryption
from common.libs.date_help import get_current_time
from application import mysql

reg_page = Blueprint('reg_page', __name__, url_prefix='/reg/')


@reg_page.get('/')
def reg():
    return render_template('reg.html')


@reg_page.post('/check')
def reg_check():
    req = request.values

    login_name = req['login_name'] if "login_name" in req else ''
    nick_name = req['nick_name'] if "nick_name" in req else ''
    login_pwd1 = req['login_pwd1'] if "login_pwd1" in req else ''
    login_pwd2 = req['login_pwd2'] if "login_pwd2" in req else ''

    if nick_name is None or len(nick_name) < 2:
        return ops_render_error_json('昵称设置错误！')

    if login_name is None or len(login_name) < 2:
        return ops_render_error_json('用户名设置错误！')

    if login_pwd1 is None or len(login_pwd1) < 6:
        return ops_render_error_json('密码设置错误！')

    if login_pwd2 != login_pwd1:
        return ops_render_error_json('两次密码不相同！')

    user_info = User.query.filter_by(login_name=login_name).first()
    if user_info:
        return ops_render_error_json('用户名已经被注册，请换一个！')

    model_user = User()
    model_user.nick_name = nick_name
    model_user.login_name = login_name
    model_user.login_pwd = encryption(login_pwd1)
    model_user.status = 1
    model_user.update_time = model_user.created_time = get_current_time()

    mysql.session.add(model_user)
    mysql.session.commit()

    return ops_render_json("注册成功")
