from flask import Flask
from flask import render_template
from flask import request
import json

app = Flask(__name__)

def add_to_db(u=None):
    if u is None:
        return False

    db = '/database.json'
    with open(db) as json_file:
        data = json.load(json_file)

    data['pessoa'].append(u)
    json.dump(data, db)

@app.route('/')
def index():
    return "Boas vindas ao sorteio de livros **não** oficial da PythonBrasil[14]" 

@app.route('/add/')
@app.route('/add/<email>')
def add(email=None):
    if email is None:
        return "Envie o email por POST ou GET ou através do form abaixo:"

    if email:
        add_to_db(email)
        return "Email cadastrado:" + email

@app.route('/list')
def list():
    db = '/database.json'
    with open(db) as json_file:
        data = json.load(json_file)

    return json.dumps(data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
