# flask-mvc
基于flask、轻量级 python MVC 开发框架

## 使用说明
### 1.目录
<br>

```php
flask-mvc
│───README.md
│───requirements.txt    #依赖模块   
│───run.py              #flask 入口文件
│───app                 #项目目录
│   │───config          #配置目录
│   │    │───config.py  #通用配置
│   │    └───__init__.py
│   │───controllers     #控制器目录
│   │    │───AuthController.py  #用户授权相关控制器
│   │    │───UserController.py  #参考如何使用模型
│   │    └───__init__.py    #装载路由、定义强制登录装饰器
│   │───models          #模型目录
│   │    │───BaseModel.py  #模型基类
│   │    │───CourseModel.py  #测试模型
│   │    └───__init__.py
│   │───static          #静态资源目录
│   │    │───css
│   │    └───js
│   │───templates       #模板目录
│   │    │───auth       #模板子目录
│   │    │     │───login.html
│   │    │     └───register.html
│   │    └───index.html
│   │───utils           #工具包
│   └───__init__.py     #app注册蓝图、初始DB
│
│───migrations          #数据库迁移目录
│───modules             #第三方模块
│───tests               #测试目录
└───venv                #虚拟环境
 
```
### 2.开发约定

```php
控制器全名：大驼峰，以Controller结尾，如 AuthController.py
模型全名：大驼峰，以Model结尾，如 CourseModel.py
```

### 3.开发环境运行

```php
执行命令：python run.py
访问地址：http://localhost:5000
```
### 4.生产环境运行

```php
nginx + Gunicorn + flask

pip install gunicorn
gunicorn -w 4 -b 127.0.0.1:5001 运行文件名称:Flask程序实例名
```
### 5.TODO

```php
用户认证
数据迁移
unit test
```