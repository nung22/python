from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'you, SHALL NOT PASS!!'

@app.route('/')
def dojo_survey():
  return render_template('index.html')

@app.route('/collect',methods=['POST'])
def collect():
  session['name'] = request.form["name"]
  session['location'] = request.form["location"]
  session['language'] = request.form["language"]
  session['comments'] = request.form["comments"]
  return redirect('/result')

@app.route('/result')
def result():
  return render_template('result.html',name=session['name'],location=session['location'],language=session['language'],comments=session['comments'])

if __name__=='__main__':
  app.run(debug=True)