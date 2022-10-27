from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'you shall not pass!'

@app.route('/')
def counter():
  if 'views' in session:
    session['views'] = session.get('views') + 1 # reads and updates number of page views
  else:
    session['views'] = 1 # sets initial view for session
  return render_template("index.html", views=session['views'])

@app.route('/destroy_session')
def destroy_session():
  session.pop('views')
  return redirect('/')

@app.route('/plus_two')
def plus_two():
  session['views'] = session.get('views') + 1
  return redirect('/')

if __name__=='__main__':
  app.run(debug=True)
