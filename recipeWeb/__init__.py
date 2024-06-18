from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from .config import Config

db = SQLAlchemy()
DB_NAME = "database.db"


def my_app(config_name=None):
    app = Flask(__name__)
    # app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
    # app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    if config_name == 'testing':
        app.config.from_object('recipeWeb.config.TestingConfig')
    else:
        app.config.from_object(Config)
        
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Recipe
    
    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app):
    if not path.exists('recipeWeb/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')