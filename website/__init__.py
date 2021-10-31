from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'test123'

    from .views import views
    from .auth import auth
    from .cal import cal

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(cal, url_prefix='/')

    return app
