from .. import db

class Base(db.Model):
    # 不创建表
    __abstract__ = True