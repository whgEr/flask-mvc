from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config.config import Config
'''
init application
'''

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    # database
    app.config.from_object(Config)
    db.init_app(app)
    # register blueprint
    from .controllers import app_route
    app.register_blueprint(app_route)
    return app
