from . import app_route

'''
this is authenticate controller，it contains some functions:
    login
    logout
    resetpassword
    captcha
'''

@app_route.route('/')
def hello():
    return "hello world,lucy"