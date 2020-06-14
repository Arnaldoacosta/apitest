from flask import Flask, request, Response
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from Servicio import servicio as serv
from config import Production
import requests

def create_app():
    app = Flask(__name__)
    app.config.from_object(Production)
    return app

app = create_app()

db = SQLAlchemy(app)

@app.route('/test', methods=['GET'])
def get_users():
    response = {'message': 'probando'}
    return jsonify(response)

@app.route('/metodo', methods=['GET'])
def get_metodo():
    response = {'message': 'probando2'}
    return jsonify(response)


''''*** INI NotaMateria *** '''

#  Add subject
@app.route('/materia', methods=['POST'])
def addNotaMateria():  
    return (serv.addNotaMateria(request))



if __name__ == '__main__':
    app.run(debug=True)