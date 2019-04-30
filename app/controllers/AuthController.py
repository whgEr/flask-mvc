from . import app_route, need_login
from flask import render_template, make_response, session
import gvcode
from io import BytesIO

'''
this is authenticate controller，it contains functions as:
    login
    logout
    resetpassword
    captcha
'''


@app_route.route('/')
def login():
    return render_template('auth/login.html', captcha=session.get('image'))



@app_route.route('/auth/logout/')
@need_login
def logout():
    return "logout"


# graphic-verification-code(gvcode) [or captcha]
@app_route.route('/auth/captcha/', methods=['GET'])
def captcha():
    s, v = gvcode.generate()
    buf = BytesIO()
    s.save(buf, 'png')
    buf_str = buf.getvalue()
    response = make_response(buf_str)
    response.headers['Content-Type'] = 'image/png'
    session['image'] = v
    print(v)
    return response
