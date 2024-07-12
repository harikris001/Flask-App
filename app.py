from flask import Flask, render_template, request
from database import get_data

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')
[]
@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

@app.route('/output', methods=['POST'])
def output():
    name = request.form['username']
    password = request.form['password']
    print(name, password)
    return f"hello {name} your password is {password}"

if __name__=="main":
    app.run()