# 公共json返回
# -----------------------------------------
from flask import jsonify
import json


def output(code, msg, data):
    return jsonify({
        'code': code,
        'msg': msg,
        'data': data
    })


def success(data=None):
    if data is None:
        data = []
    return output(0, 'success', data)


def error(code=1, msg=''):
    if msg == '':
        msg = 'error'
    return output(code, msg, [])
