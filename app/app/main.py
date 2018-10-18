from flask import Flask
from flask import render_template
from flask import request
import json

db = '/database.json'
app = Flask(__name__)

def add_to_db(u=None):
    if u is None:
        return False

    data = json.load(db)
    data.append(u)
    json.dump(data, db)

@app.route('/')
def index():
    return "Boas vindas ao sorteio de livros **não** oficial da PythonBrasil[14]" 

@app.route('/add/')
def add_to_raffle(email=None):
    if email is None:
        return "Envie o email por POST ou GET ou através do form abaixo:"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
