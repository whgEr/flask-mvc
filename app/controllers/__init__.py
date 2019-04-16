from flask import Blueprint
import os

'''
create route with blueprint
'''

app_route = Blueprint('app_route',__name__)
controller_path = os.path.dirname(__file__)
for f in os.listdir(controller_path):
    file = os.path.join(controller_path,f)
    if os.path.isfile(file) and not f.startswith('__'):
        __import__('app.controllers.%s' % f[:-3])