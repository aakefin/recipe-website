# recipeWeb/config.py

DB_NAME = "database.db"
class Config:
    SECRET_KEY = 'hjshjhdjah kjshkjdhjs'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{DB_NAME}'
    # app.config['SECRET_KEY'] = '
    # app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{DB_NAME}'
