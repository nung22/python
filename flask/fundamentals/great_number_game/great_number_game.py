from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'you, SHALL NOT PASS!!'

@app.route('/')
def great_number_game():
  return render_template("index.html")

if __name__=='__main__':
  app.run(debug=True)