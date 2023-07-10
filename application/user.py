from flask import Blueprint, request
from common.models.User import User as User_model

blueprint = Blueprint('user', __name__, url_prefix='/user')


@blueprint.route('/info')
def info():
    user_id = request.args.get("id", type=int, default=0)
    user = User_model.query.get(user_id)
    if user:
        return str(user_id)
    return '用户不存在'


@blueprint.route('/add')
def add():
    db = User_model.db
    user = User_model(username="joysaaa", password="556520", email="547720744@qq.com")
    db.session.add(user)
    db.session.commit()
    return '创建成功'
