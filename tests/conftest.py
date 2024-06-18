# tests/conftest.py
import pytest
from recipeWeb import my_app, db
from recipeWeb.models import User
from werkzeug.security import generate_password_hash

@pytest.fixture(scope='module')
def test_client():
    app = my_app('testing')
    testing_client = app.test_client()

    ctx = app.app_context()
    ctx.push()

    yield testing_client

    ctx.pop()

@pytest.fixture(scope='module')
def init_database():
    app = my_app('testing')
    with app.app_context():
        db.create_all()

        user = User(email='test@example.com', first_name='Test', password=generate_password_hash('password', method='sha256'))
        db.session.add(user)
        db.session.commit()

        yield db

        db.session.remove()
        db.drop_all()

@pytest.fixture(scope='function')
def login_default_user(test_client):
    test_client.post('/login_page', data=dict(email='test@example.com', password='password'), follow_redirects=True)
    yield
    test_client.get('/logout', follow_redirects=True)
