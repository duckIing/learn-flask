import bcrypt
from hashlib import md5

"""
bcrypt 生成的哈希密码的长度是一个固定的长度，并且长度是根据工作因子 (work factor) 来计算的。在 Python 中，bcrypt 生成的哈希密码默认长度为60字节。

salt 是与密码结合使用用于生成密码哈希值的随机值。在每次生成哈希值时使用随机的salt可以防止两个相同的用户密码生成相同的哈希值，从而增强密码的安全性。
因此，salt是为了密码安全性而设计的，不应该与用户的密码一起存储在同一个地方。

在bcrypt中，salt值已经包含在生成的哈希值中。因此，在验证用户的密码时，只需要使用哈希值和用户提供的密码就可以了。
一般而言，我们不应该将salt存储在数据库中。而是每次使用新的随机值来生成哈希值，以确保每个用户的密码哈希值都是唯一的，
否则攻击者可以更加轻松地通过攻击哈希值来获得用户密码。
"""


# bcrypt 密码加密
def encryption(string):
    """
    密码加密
    :param string: 用户输入的密码字符串，等需要加密的字符串
    :return: 加密后的字符串
    """
    # 生成一个salt
    salt = bcrypt.gensalt()
    # 生成密码哈希值
    hashed_bytes = bcrypt.hashpw(string.encode('utf-8'), salt)
    hashed_string = hashed_bytes.decode('utf-8')
    return hashed_string


# bcrypt 密码核对
def check_encryption(string, hashed_string):
    """
    密码核对
    :param string: 待 check 的字符串，例如：用户输入的密码字符串
    :param hashed_string: 加密后的字符串，例如：在数据库中保存的密码加密后的字符串
    :return: 1 - 核对成功； -1 - 核对失败
    """
    # 验证密码哈希值
    if bcrypt.checkpw(string.encode('utf-8'), hashed_string.encode('utf-8')):
        return 1  # 核对成功
    else:
        return -1  # 核对失败


# 用户信息加密
def encryption_userinfo(user):
    """
    将用户信息加密
    :param user: 用来生成 判断用户登陆状态的 cookie 值; 是从数据库中取出来的一条数据。
    :return: 加密后的用户信息
    """
    user_info_string = f'{user.id}+=+{user.login_name}+=+{user.login_pwd}'
    m = md5()
    m.update(user_info_string.encode('utf-8'))
    return m.hexdigest()


# 利用用户信息创建用于判断用户登陆状态的cookie值
def gen_user_cookie(user=None):
    """
    使用用户信息，创建用户登陆状态，存储 cookie 中。cookie = 用户加密信息 + #### + user.id
    :param user: 用来生成 判断用户登陆状态的 cookie 值; 是从数据库中取出来的一条数据。
    :return: 加密后数据
    """

    # cookie = 用户加密信息 + #### + user.id
    cookie = encryption_userinfo(user) + '####' + str(user.id)

    return cookie


if __name__ == '__main__':
    password_string = '123123132132132'
    hashed_password_string = encryption(password_string)
    print(hashed_password_string)
    print(check_encryption(password_string, hashed_password_string))
