from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'KBY4eBLADzZHgdyUvz3duNtHRKvRwPBuHbmQckwN5W8fUVCnW4QSJz7s2YcpBAny'

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix = '/')
    app.register_blueprint(auth, url_prefix = '/')









    return app