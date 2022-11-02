from flask import Flask, render_template, request, redirect
# import the class from user.py
from user import User
app = Flask(__name__)

@app.route('/')
def index():
  return redirect('/users')


@app.route('/users')
def read_all():
  users = User.get_all()
  print(users)
  return render_template("read(all).html", all_users = users)


@app.route('/make_new_user')
def make_new_user():
  return render_template('create.html')


@app.route('/users/<id>')
def read_one(id):
  user_id = { 'id' : id }
  info = User.get_one(user_id)[0]
  print(info)
  return render_template('read(one).html', user_info = info)


@app.route('/users/<id>/edit')
def edit(id):
  user_id = { 'id' : id }
  info = User.get_one(user_id)[0]
  print(info)
  return render_template('edit.html', user_info = info)


@app.route('/users/<id>/update', methods=['POST'])
def update(id):
  print(request.form)
  User.edit(request.form)
  return redirect('/users')

@app.route('/users/<id>/destroy')
def destroy(id):
  data = { 'id' : id }
  User.delete(data)
  return redirect('/users')


@app.route('/users/new', methods=['POST'])
def create():
  print(request.form)
  User.save(request.form)
  users = User.get_all()
  last_id = users[len(users)-1].id
  return redirect('/users/'+str(last_id))


if __name__=='__main__':
  app.run(debug=True)