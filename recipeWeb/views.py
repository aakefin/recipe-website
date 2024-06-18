from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from .models import Recipe
from . import db
import json

views = Blueprint('views', __name__)

@views.route('/')
def landing_page():
    return render_template('landing_page.html',user = current_user)

@views.route('/home_page', methods=['GET', 'POST'])
@login_required
def home_page():
    page = request.args.get('page', 1, type=int) 
    recipes = Recipe.query.filter_by(created_by=current_user.id).paginate(page=page, per_page=5)
    
    return render_template("home_page.html", user=current_user, recipes=recipes)


@views.route('/recipe/<int:recipe_id>')
def recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)  # Fetch a single recipe by ID
    return render_template('recipe_view.html',user=current_user, recipe=recipe)


@views.route('/add_recipe', methods=['GET','POST'])
def add_recipe():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        ingredients = request.form.getlist('ingredients')
        instructions =  request.form['instructions']
        
        new_recipe = Recipe(title=title,description=description,ingredients=ingredients,instructions=instructions, created_by = current_user.id)
        db.session.add(new_recipe)
        db.session.commit()
        return redirect(url_for('views.home_page'))
        
    return render_template('add_recipe.html',user=current_user)


@views.route('/recipe/<int:recipe_id>/update', methods=['GET', 'POST'])
@login_required
def update_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)

    if request.method == 'POST':
        recipe.title = request.form['title']
        recipe.description = request.form['description']
        recipe.ingredients = request.form.getlist('ingredients')
        recipe.instructions = request.form['instructions']

        db.session.commit()
        flash('Recipe updated successfully', 'success')
        return redirect(url_for('views.recipe', recipe_id=recipe.id))

    return render_template('update_recipe.html', user=current_user, recipe=recipe)

@views.route('/recipe/<int:recipe_id>/delete', methods=['POST'])
@login_required
def delete_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    db.session.delete(recipe)
    db.session.commit()
    flash('Recipe deleted successfully', 'success')
    return redirect(url_for('views.home_page'))