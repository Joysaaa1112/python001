from flask import Blueprint

blueprint = Blueprint('index', __name__, url_prefix='/')


@blueprint.route('/')
def index():
    return 'index'
