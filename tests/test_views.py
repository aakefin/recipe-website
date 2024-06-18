import pytest
from flask import url_for
from recipeWeb import db
from recipeWeb.models import Recipe



def test_home_page(test_client, init_database, login_default_user):
    response = test_client.get('/home_page')
    assert response.status_code == 200
    

def test_add_recipe(test_client, init_database, login_default_user):
    response = test_client.post('/add_recipe', data=dict(
        title='Test Recipe',
        description='Test Description',
        ingredients=['Ingredient 1', 'Ingredient 2'],
        instructions='Test Instructions'
    ), follow_redirects=True)
    assert response.status_code == 200
  

def test_update_recipe(test_client, init_database, login_default_user):
    
    response = test_client.post('/add_recipe', data=dict(
        title='Test Recipe',
        description='Test Description',
        ingredients=['Ingredient 1', 'Ingredient 2'],
        instructions='Test Instructions'
    ), follow_redirects=True)
    assert response.status_code == 200


    recipe_id = db.session.query(Recipe).filter_by(title='Test Recipe').first().id


    response = test_client.post(f'/recipe/{recipe_id}/update', data=dict(
        title='Updated Recipe',
        description='Updated Description',
        ingredients=['Updated Ingredient 1', 'Updated Ingredient 2'],
        instructions='Updated Instructions'
    ), follow_redirects=True)
    assert response.status_code == 200
    assert b'Recipe updated successfully' in response.data

def test_delete_recipe(test_client, init_database, login_default_user):
    
    response = test_client.post('/add_recipe', data=dict(
        title='Test Recipe',
        description='Test Description',
        ingredients=['Ingredient 1', 'Ingredient 2'],
        instructions='Test Instructions'
    ), follow_redirects=True)
    assert response.status_code == 200

    
    recipe_id = db.session.query(Recipe).filter_by(title='Test Recipe').first().id


    response = test_client.post(f'/recipe/{recipe_id}/delete', follow_redirects=True)
    assert response.status_code == 200
    assert b'Recipe deleted successfully' in response.data
