from application import mysql


class User(mysql.Model):
    __tablename__ = 'user'

    id = mysql.Column(mysql.Integer, primary_key=True, info='User ID')
    nick_name = mysql.Column(mysql.String(30), info="User's nickname")
    login_name = mysql.Column(mysql.String(20), nullable=False, unique=True, info="User's login name")
    login_pwd = mysql.Column(mysql.String(32), nullable=False, info="User's login password")
    status = mysql.Column(mysql.Integer, nullable=False, info='User status; 0 - invalid; 1 - valid')
    update_time = mysql.Column(mysql.DateTime, nullable=False, info='Last update time')
    created_time = mysql.Column(mysql.DateTime, nullable=False, info='Entry creation time')
