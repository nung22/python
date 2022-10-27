from datetime import datetime,time
from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    numStrawberries = int(request.form.get("strawberry"))
    numRaspberries = int(request.form.get("raspberry"))
    numApples = int(request.form.get("apple"))
    print(f"Charging {first_name} {last_name} for {numStrawberries+numRaspberries+numApples} fruits")
    return render_template("checkout.html",num_strawberry=numStrawberries,num_raspberry=numRaspberries,num_apple=numApples,fname=first_name,lname=last_name,studentID = request.form.get("student_id"),dateAndTime = datetime.now().strftime("%m/%d/%y")
    )
# March 23rd 2019 5:15:35 PM
@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    