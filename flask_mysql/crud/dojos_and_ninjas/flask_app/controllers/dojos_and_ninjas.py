from flask_app import app
from flask import render_template,redirect,request
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

# REDIRECT FROM INDEX TO DOJOS PAGE
@app.route('/')
def index():
  return redirect('/dojos')

# DISPLAY ALL DOJOS
@app.route('/dojos')
def dojos():
  return render_template('dojos.html', all_dojos = Dojo.get_all())

# CREATE NEW DOJO OBJECT AND REDIRECT TO DOJOS PAGE
@app.route('/create_dojo',methods=['POST'])
def create_dojo():
  print(request.form)
  Dojo.save(request.form)
  return redirect('/dojos')

# DISPLAY FORM FOR CREATING NEW NINJA
@app.route('/ninjas')
def add_ninja():
  return render_template('/ninjas.html',all_dojos = Dojo.get_all())

# CREATE NEW NINJA OBJECT AND REDIRECT TO SHOW DOJO PAGE FOR THE NINJA'S DOJO
@app.route('/create_ninja',methods=['POST'])
def create_ninja():
  print(request.form)
  Ninja.save(request.form)
  ninjas = Ninja.get_all()
  dojo_id = ninjas[len(ninjas)-1].dojo_id
  return redirect(f'/dojos/{dojo_id}')

# DISPLAY ALL NINJAS FOR A GIVEN DOJO
@app.route('/dojos/<int:dojoID>')
def show_dojo(dojoID):
  data = { 'dojo_id' : dojoID }
  d_name = ""
  for one_dojo in Dojo.get_all():
    print(one_dojo.name,one_dojo.id)
    if int(one_dojo.id) == dojoID:
      d_name = one_dojo.name
      print(one_dojo.name)
      break
  return render_template('dojo_show.html',dojo = Dojo.get_dojo_with_ninjas(data),dojo_name=d_name)