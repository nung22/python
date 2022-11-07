from flask_app import app, render_template, request, redirect, bcrypt, session, flash
from flask_app.models.recipe import Recipe

# Redirect From Index To recipes Page
@app.route('/recipes')
def recipes():
    if 'user_id' not in session:
        return redirect('/logout')
    return render_template('recipes.html',user_name = session['first_name'],all_recipes = Recipe.get_all(), user_id = session['user_id'])

@app.route('/recipes/new')
def recipes_new():
    return render_template('recipes_new.html',user_id = session['user_id'])

# Create New recipe Object And Redirect To recipes Page
@app.route('/new_recipe',methods=['POST'])
def new_recipe():
    print(request.form)
    if not Recipe.validate_recipe(request.form):
        return redirect('/recipes/new')
    Recipe.save(request.form)
    return redirect('/recipes')

@app.route('/login', methods=['POST'])
def edit():
    print(request.form)
    recipe = recipe.get_by_email(request.form)
    if not recipe:
        flash("Invalid Credentials.")
        return redirect('/')
    pass_valid = bcrypt.check_password_hash(recipe.password, request.form['password'])
    if not pass_valid:
        flash("Invalid Credentials.")
        return redirect('/')
    session['recipe_id'] = recipe.id
    session['first_name'] = recipe.first_name
    session['last_name'] = recipe.last_name
    return redirect('/recipes')


