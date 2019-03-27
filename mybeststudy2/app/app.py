from flask import Flask

from flask_login import LoginManager
login_manager = LoginManager()

def register_blueprints(app):
    from app.chang import chang
    app.register_blueprint(chang)

def register_plugin(app):
    from  app.models.base import db
    db.init_app(app)
    with app.app_context():
        db.create_all()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.setting')
    #flasklogin初始化
    login_manager.init_app(app)

    register_blueprints(app)
    register_plugin(app)


    return app
