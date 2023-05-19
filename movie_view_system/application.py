from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# 初始化 app
app = Flask(__name__)

# 配置 app 的 config 参数
app.config.from_pyfile('./config/config.py', silent=True)

# 初始化数据库
mysql = SQLAlchemy(app)
