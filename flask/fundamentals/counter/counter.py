from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'you shall not pass!'

@app.route('/')
def counter(increment=1):
  if 'visits' in session:
    session['visits'] = session.get('visits') + increment # reads and updates number of page visits
  else:
    session['visits'] = 1 # sets initial view for session
  if 'actualVisits' in session:
    session['actualVisits'] = session.get('actualVisits') + 1 # reads and updates number of page actual visits
  else:
    session['actualVisits'] = 1 # sets initial view for session
  return render_template("index.html", visits=session['visits'], actual_visits=session['actualVisits'])

@app.route('/adjust_increment', methods=['POST'])
def adjust_increment():
  print(request.form.get('increment'))
  increment = request.form.get('increment')
  print(increment)
  return redirect('/')

@app.route('/destroy_session')
def destroy_session():
  session.pop('visits')
  session.pop('actualVisits')
  return redirect('/')

@app.route('/plus_two')
def plus_two():
  session['visits'] = session.get('visits') + 1
  session['actualVisits'] = session.get('actualVisits') - 1
  return redirect('/')

if __name__=='__main__':
  app.run(debug=True)
