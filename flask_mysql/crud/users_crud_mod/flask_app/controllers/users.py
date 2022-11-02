from flask_app import app
from flask import render_template,redirect,request,flash
from flask_app.models.user import User

# redirects to read(all) page from default route
@app.route('/')
def index():
  return redirect('/users')

# gets all users and returns them as a list of user objects
@app.route('/users')
def read_all():
  return render_template("read(all).html", all_users = User.get_all())

# renders page for creating a new user
@app.route('/make_new_user')
def make_new_user():
  return render_template('create.html')

# gets the info for a user given their id and return the user object for the show page
@app.route('/users/<id>')
def read_one(id):
  user_id = { 'id' : id }
  info = User.get_one(user_id)[0]
  print(info)
  return render_template('read(one).html', user_info = info)

# gets the info for a user given their id and return the user object for the edit page
@app.route('/users/<id>/edit')
def edit(id):
  user_id = { 'id' : id }
  info = User.get_one(user_id)[0]
  print(info)
  return render_template('edit.html', user_info = info)

# updates the info for a given user using the provided form info
@app.route('/users/update', methods=['POST'])
def update():
  print(request.form)
  User.edit(request.form)
  return redirect('/users')

# deletes the user object given their user id and redirects to read(all) page
@app.route('/users/<id>/destroy')
def destroy(id):
  data = { 'id' : id }
  User.delete(data)
  return redirect('/users')

# makes a new User object using the provided form info and redirects to read(one) page
@app.route('/users/new', methods=['POST'])
def create():
  print(request.form)
  User.save(request.form)
  users = User.get_all()
  last_id = users[len(users)-1].id
  return redirect('/users/'+str(last_id))