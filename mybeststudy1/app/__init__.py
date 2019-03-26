from flask import Flask

def create_app():
    app =Flask(__name__)
    app.config.from_object('app.setting')
    register_blueprints(app)
    return app

def register_blueprints(app):
    from app.chang import chang
    app.register_blueprint(chang)

