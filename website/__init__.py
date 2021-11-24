from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager


db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'test123'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)




    from .views import views
    from .auth import auth
    from .cal import cal

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(cal, url_prefix='/')

    from .models import User, Note, Event

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')


#########help

from flask_mysqldb import MySQL, MySQLdb

app2 = Flask(__name__)

app2.secret_key = "caircocoders-ednalan"
app2.config['MYSQL_HOST'] = 'localhost'
app2.config['MYSQL_USER'] = 'root'
app2.config['MYSQL_PASSWORD'] = ''
app2.config['MYSQL_DB'] = 'testingdb'
app2.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app2)
