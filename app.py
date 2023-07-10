from flask import Flask
import config.config as config
from extends import db
from application.index import blueprint as index_blueprint
from application.user import blueprint as user_blueprint
from flask_migrate import Migrate

app = Flask(__name__)


# 加载配置文件
app.config.from_object(config)
# 初始化数据库
db.init_app(app)
# 初始化Flask-Migrate
migrate = Migrate(app, db)
# 注册蓝图
app.register_blueprint(index_blueprint)
app.register_blueprint(user_blueprint)


if __name__ == '__main__':
    app.run(debug=True)
