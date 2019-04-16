from flask import Flask
from .controllers import app_route

'''
init application
'''


def create_app():
    app = Flask(__name__)
    # register blueprint
    app.register_blueprint(app_route)
    return app
