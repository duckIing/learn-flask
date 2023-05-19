# movie_view_system 电影资源展示网站

# python 环境构建

```bash
# 1. 安装 miniconda / anaconda ，等 conda 相关环境管理工具。
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn//anaconda/cloud/conda-forge
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/bioconda
conda config --set show_channel_urls yes
conda config --show
# 2. 切换路径：cd 到项目目录, 例如：
cd ~/Code/learn-flask/movie_view_system
# 3. 安装环境
conda env create --prefix ./movie_view_system_env --file python-environment.yml --force
# 4. 使用环境
conda activate ./movie_view_system_env
pip -V
python -V
```

# mysql 环境构建

1. 安装好 docker 环境
2. 切换路径：cd 到项目目录, 例如：cd ~/Code/learn-flask/movie_view_system
3. docker 安装 mysql8 环境，并且把 mysql 数据文件，映射到 ./MySQL8 中

```bash
# 进入项目目录
cd ~/Code/learn-flask/movie_view_system

# 配置目录变量
now_dir=$(pwd)

# 拉镜像
docker pull mysql:8.0.32

# 设置本地目录，存放mysql的配置文件，日志和数据，防止容器删除后数据丢失
mkdir -p $now_dir/mysql8/conf/
mkdir -p $now_dir/mysql8/logs/
mkdir -p $now_dir/mysql8/data/

# mysql配置文件
cat > $now_dir/mysql8/conf/my.cnf <<EOF
[mysqld]
max_connections=1000
max_connect_errors=1000
interactive_timeout=1800
wait_timeout=1800
transaction_isolation=READ-COMMITTED
default-storage-engine=INNODB
character-set-server=utf8mb4
collation-server=utf8mb4_general_ci
default-authentication-plugin=mysql_native_password

[client]
default-character-set=utf8mb4

[mysql]
default-character-set=utf8mb4
EOF

# 配置mysql的docker启动文件
cat > $now_dir/mysql-docker-compose.yml << EOF
version: "3.9"
services:
 mysql8:
   image: mysql:8.0.32
   restart: always
   container_name: mysql8
   volumes:
     - "$now_dir/mysql8/conf:/etc/mysql/conf.d"
     - "$now_dir/mysql8/logs:/var/log/mysql"
     - "$now_dir/mysql8/data:/var/lib/mysql"
   ports:
     - "3306:3306"
   environment:
     MYSQL_ROOT_PASSWORD: rootroot
     TZ: Asia/Shanghai
EOF

# 后台启动 mysql
docker-compose -f $now_dir/mysql-docker-compose.yml up -d
```

```sql
-- 创建数据库
CREATE DATABASE IF NOT EXISTS `movie_system` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- 创建表格
CREATE TABLE `movie_system`.`user`
(
    `id`           int unsigned NOT NULL AUTO_INCREMENT COMMENT 'User ID',
    `nick_name`    varchar(30)          DEFAULT NULL COMMENT 'User''s nickname',
    `login_name`   varchar(20) NOT NULL COMMENT 'User''s login name',
    `login_pwd`    varchar(60) NOT NULL COMMENT 'User''s login password',
    `status`       tinyint     NOT NULL DEFAULT '1' COMMENT 'User status; 0 - invalid; 1 - valid',
    `update_time`  datetime    NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Last update time',
    `created_time` datetime    NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Entry creation time',
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

ALTER TABLE `movie_system`.`user`
    ADD UNIQUE INDEX `login_name_UNIQUE` (`login_name` ASC);
```

## 一、学习要点总结

1. 网站功能设计：前端 & 后端
2. 数据库创建表格、自动导出 ORM model
3. Jinja2 & Bootstrap3、创建首页、登陆页、注册页
    1. 模板加载 js 的顺序
    2. layer 组件的构成
4. 静态页面加载方式（创建页面路由的方式，统一链接管理器）
    1. 配置文件设置：DOMAIN
    2. common/libs/url_manager.py
    3. 模板中使用函数创建路径
5. 注册功能后端
    1. jquery 的简单写法，数据发送到后端
6. 登陆功能
    1. 密码校验功能
    2. cookie 和 session 设置用户登陆状态的优劣，已经如何选择。
    3. 选择 cookie 存储。使用 user 信息，生成令牌，cookie 的值，发送给浏览器。
    4. 可以在拦截器中验证用户登陆状态。
7. common/lib 设计和写法
    1. 消息处理 - render_msg_help.py
    2. 时间处理 - date_help.py
    3. 用户密码处理 - user_services.py
    4. 统一链接管理器 - url_manager.py
8. 实际开发的经验学习

## 二、功能设计

### （一）前台功能

#### 1）账户功能

1. 账户注册
2. 账户登陆

#### 2）展示功能

1. 电影类别
2. 电影详情

### （二）后台功能

## 三、数据库设计

### 一、创建数据库

### 二、前台功能数据库设计

#### 1）用户功能

用户表：账户注册 / 账户登陆

#### 2）电影展示功能

电影类别

电影详情

### 三、 后台功能数据库设计