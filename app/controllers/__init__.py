from flask import Blueprint,session
import os
import functools

'''
create route with blueprint
'''

def need_login(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        user_info = session.get('user_info')
        if user_info is None:
            return "no user"
        return func(*args,**kw)
    return wrapper

app_route = Blueprint('app_route',__name__)
controller_path = os.path.dirname(__file__)
for f in os.listdir(controller_path):
    file = os.path.join(controller_path,f)
    if os.path.isfile(file) and not f.startswith('__'):
        __import__('app.controllers.%s' % f[:-3])

