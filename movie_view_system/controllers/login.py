from flask import request
from flask import Blueprint
from flask import render_template
from flask import make_response
from application import app
from common.models.user import User
from common.libs.user_services import check_encryption
from common.libs.render_help import ops_render_json
from common.libs.render_help import ops_render_error_json
from common.libs.user_services import gen_user_cookie

login_page = Blueprint('login_page', __name__, url_prefix='/login/')


@login_page.get('/')
def login():
    return render_template('login.html')


@login_page.post('/check')
def login_check():
    req = request.values

    login_name = req['login_name'] if 'login_name' in req else ''
    login_pwd = req['login_pwd'] if 'login_pwd' in req else ''

    if login_name is None or len(login_name) < 2:
        return ops_render_error_json("请输入正确的登录用户名~~")

    if login_pwd is None or len(login_pwd) < 6:
        return ops_render_error_json("请输入正确的登录密码~~")

    user = User.query.filter_by(login_name=login_name).first()

    if user:
        hashed_password_string = user.login_pwd
    else:
        return ops_render_error_json('用户名或者密码错误，登陆失败！')  # 不能告知用户名错误，否则撞库。

    if check_encryption(login_pwd, hashed_password_string) == 1:
        # 将用户登陆状态保存在 session 中， 其实本质是把数据加密放到 cookie 中，不安全。
        # session['uid'] = user.id
        # return ops_render_json('登陆成功！')

        # 使用 cookie 存储用户状态
        response = make_response(ops_render_json('登陆成功!'))
        response.set_cookie(
            app.config["AUTH_COOKIE_NAME"],
            gen_user_cookie(user),
            60 * 60 * 24
        )
        return response

    else:
        return ops_render_error_json('用户名或者密码错误，登陆失败！')
