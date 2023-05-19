from urllib.parse import quote_plus
import os


AUTH_COOKIE_NAME = 'USER'
SECRET_KEY = os.urandom(32).hex()
DEBUG = True

DOMAIN = {
    "www": "http://192.168.1.201:5000"
}

mysql_hostname = '127.0.0.1'
mysql_port = 3306
mysql_username = "root"
mysql_password = quote_plus("rootroot")
mysql_database = "movie_system"
mysql_driver = "pymysql"

SQLALCHEMY_DATABASE_URI = f"mysql+{mysql_driver}://{mysql_username}:" \
                          f"{mysql_password}@{mysql_hostname}:" \
                          f"{mysql_port}/{mysql_database}?charset=utf8mb4"
