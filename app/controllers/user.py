from . import app_route

'''
    user controller
'''

@app_route.route('/user')
def user():
    return "你好，user"