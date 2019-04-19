from . import app_route
from ..models.course import Course
from ..utils import helper
'''
    user controller
'''

@app_route.route('/user')
def user():
    item = Course.query.all()
    print("the item is:**************************************\n",type(item))
    return helper.to_json(item)