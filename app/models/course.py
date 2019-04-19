from .base import Base
from .. import db

class Course(Base):
    __tablename__ = 'course'

    cid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    teacher_id = db.Column(db.Integer)
    cname = db.Column(db.String(255))