# from flask import Flask,render_template
# app = Flask(__name__)
# @app.route('/')
# def index():
#     return render_template("index.html",row=8,col=8,colorOne="black",colorTwo="red")

# @app.route('/<x>')
# def row(x):
#     return render_template("index.html",row=int(x),col=8,colorOne="black",colorTwo="red")

# @app.route('/<x>/<y>')
# def rowsAndCols(x,y):
#     return render_template("index.html",row=int(x),col=int(y),colorOne="black",colorTwo="red")

# @app.route('/<x>/<y>/<color1>/<color2>')
# def rowsAndColsAndColors(x,y,color1,color2):
#     return render_template("index.html",row=int(x),col=int(y),colorOne=color1,colorTwo=color2)

# if __name__=="__main__":
#     app.run(debug=True)

from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
@app.route('/<x>')
@app.route('/<x>/<y>')
@app.route('/<x>/<y>/<color1>')
@app.route('/<x>/<y>/<color1>/<color2>')
def rowsAndColsAndColors(x=8,y=8,color1="black",color2="red"):
    return render_template("index.html",row=int(x),col=int(y),colorOne=color1,colorTwo=color2)

if __name__=="__main__":
    app.run(debug=True)