from .. import db



class Base(db.Model):
    '''
    base model class
    '''
    __abstract__ = True
