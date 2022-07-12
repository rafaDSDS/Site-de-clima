from flask import Flask

def create_app():
    app = Flask(__name__,static_folder='static',template_folder='template')
    app.config['SECRET_KEY'] = '!@#21321Fewf312R32$_#!$!@+!@$!@#'

    from .views import views

    app.register_blueprint(views,url_prefix='/')

    return app
