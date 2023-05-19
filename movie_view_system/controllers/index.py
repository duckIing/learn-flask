from flask import Blueprint
from flask import render_template
from common.libs.render_help import ops_render

index_page = Blueprint('index_page', __name__, url_prefix='/')


@index_page.route('/')
def home():
    return ops_render("index.html")
