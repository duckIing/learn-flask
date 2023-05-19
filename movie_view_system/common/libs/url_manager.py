from application import app


def build_url(path):
    config_domain = app.config["DOMAIN"]["www"]
    return f"{config_domain}{path}"


def build_static_url(path):
    path = '/static' + path
    return build_url(path)
