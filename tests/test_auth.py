import pytest
from flask import url_for
from werkzeug.security import generate_password_hash
from recipeWeb.models import User

def test_register(test_client, init_database):
    response = test_client.post('/sign_up', data=dict(
        email='newuser@example.com',
        first_name='New',
        password='newpassword',
        confirm_password='newpassword'
    ), follow_redirects=True)

    assert response.status_code == 200
    assert b'Account created!' in response.data

def test_login(test_client, init_database):
    response = test_client.post('/login_page', data=dict(
        email='test@example.com',
        password='password'
    ), follow_redirects=True)

    assert response.status_code == 200
    assert b'Logged in successfully!' in response.data

def test_logout(test_client, init_database):
    response = test_client.get('/logout', follow_redirects=True)

    assert response.status_code == 200
    assert b'Login' in response.data
