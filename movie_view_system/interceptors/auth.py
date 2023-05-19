from application import app
from flask import request
from common.libs.user_services import encryption_userinfo
from common.models.user import User
from flask import g


@app.before_request
def before_request():
    user_info = check_login()
    g.current_user = None
    if user_info:
        g.current_user = user_info
    return None


def check_login():
    """
    校验 cookie 信息是否准确，判断登陆信息是否正确
    :return:
        如果正确，返回用户信息
        如果不正确，返回 False
    """
    cookies = request.cookies
    cookie_name = app.config["AUTH_COOKIE_NAME"]
    auth_cookie = cookies.get(cookie_name, None)
    if auth_cookie is None:
        return False

    # cookie = 用户加密信息 + #### + 用户id
    auth_info = auth_cookie.split('####')
    if len(auth_info) != 2:
        return False

    # 利用 用户id 从数据库中获取 用户信息
    try:
        user = User.query.filter_by(id=auth_info[1]).first()
    except Exception as e:
        return False

    if user is None:
        return False

    # 用户信息再次加密，看看是否和 cookie 中的 用户加密信息相同。
    if auth_info[0] != encryption_userinfo(user):
        return False

    return user
