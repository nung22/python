from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return "Hello World!"

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<name>')
def say(name):
    if name.isdigit():
        return "Sorry! No response. Try again."
    else:
        return f"Hi {name.capitalize()}!"

@app.route('/repeat/<num>/<word>')
def repeat(num,word):
    if num.isdigit()&word.isdigit()==False:
        num_repeat = ""
        for i in range(int(num)):
            num_repeat += word + " "
        return num_repeat
    else:
        return "Sorry! No response. Try again."

if __name__=="__main__":
    app.run(debug=True)