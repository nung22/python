from flask import Flask, render_template
app = Flask(__name__)
@app.route('/play')
def index():
    return render_template("index.html",times=3,box_color="skyblue")

@app.route('/play/<x>')
def boxNum(x):
    return render_template("index.html",times=int(x),box_color="skyblue")

@app.route('/play/<x>/<color>')
def boxNumAndColor(x,color):
    return render_template("index.html",times=int(x),box_color=color)

if __name__=="__main__":
    app.run(debug=True)