from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello world'

@app.route('/name')
def print_name():
    return 'your name'