from application import app

# interceptors - 拦截器处理 / 错误处理
from interceptors.auth import before_request  # 拦截器处理，判断用户是否登陆
from interceptors.error_handler import error_404  # 错误处理，返回 404

# controllers - 控制器(蓝图)
from controllers.login import login_page
from controllers.index import index_page
from controllers.reg import reg_page
from controllers.logout import logout_page

app.register_blueprint(index_page)  # 主页
app.register_blueprint(login_page)  # 登陆页
app.register_blueprint(reg_page)  # 注册页
app.register_blueprint(logout_page)  # 注销页

# jinja2 模板函数
from common.libs.url_manager import build_url
from common.libs.url_manager import build_static_url

app.add_template_global(build_url)  # 创建路径
app.add_template_global(build_static_url)  # 创建 static 资源路径
