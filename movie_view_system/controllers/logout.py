from flask import Blueprint
from flask import redirect, make_response
from application import app
from common.libs.url_manager import build_url

logout_page = Blueprint('logout_page', __name__, url_prefix='/logout/')


@logout_page.get('/')
def logout():
    response = make_response(redirect(build_url('/')))
    response.delete_cookie(app.config["AUTH_COOKIE_NAME"])
    return response
