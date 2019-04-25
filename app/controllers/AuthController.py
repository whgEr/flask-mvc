from . import app_route
from flask import render_template,make_response,session
import gvcode
from io import BytesIO

'''
this is authenticate controller，it contains some functions:
    login
    logout
    resetpassword
    captcha
'''

@app_route.route('/auth/login')
def login():
    return render_template('auth/login.html',captcha=session.get('image'))

# graphic-verification-code [captcha]
@app_route.route('/auth/captcha',methods=['GET'])
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