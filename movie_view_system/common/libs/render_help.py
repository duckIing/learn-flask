from flask import jsonify, g, render_template


def ops_render(template, context=None):
    if context is None:
        context = {}
    if 'current_user' in g:
        context['current_user'] = g.current_user
    return render_template(template, **context)


def ops_render_json(msg="操作成功", code=200, data=None):
    if data is None:
        data = {}
    resp = {
        "code": code,
        "msg": msg,
        "data": data
    }
    return jsonify(resp)


def ops_render_error_json(msg, data=None):
    if data is None:
        data = {}
    return ops_render_json(msg=msg, code=-1, data=data)
