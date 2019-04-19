class Config(object):
    ''' 通用配置类 '''

    # 设置连接数据库的URL
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123@127.0.0.1:3306/test'
    # 设置每次请求结束后会自动提交数据库中的改动
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    # SQLAlchemy 将追踪对象的修改并且发送信号。这需要额外的内存， 如果不必要可以禁用
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # 查询时会显示原始SQL语句
    SQLALCHEMY_ECHO = True
