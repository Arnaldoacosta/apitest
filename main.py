
from flask import Flask, request, jsonify, Response
from flask_sqlalchemy import SQLAlchemy
from Servicio import servicio as serv
import json
from flask_api import status
from Servicio.Exception_api import ApiExceptionServ
from Servicio.Exception_api import NotFound
import requests
import os
from config import Production

#app = Flask(__name__)


def create_app():
    app = Flask(__name__)
    app.config.from_object(Production)
    return app

app = create_app()


db = SQLAlchemy(app)

''''*** INI NotaMateria *** '''

#  Add subject
@app.route('/materia', methods=['POST'])
def addNotaMateria():  
    return (serv.addNotaMateria(request))

# Update subject               
@app.route('/materia', methods=['PATCH'])
def updateNotaMateria():
    return (serv.updateNotaMateria(request))


'''#Get all ---(Se usará en una posible futuro si crece la aplicacion)
@app.route('/materias', methods=['GET'])
def getNotasMaterias():  
    return (serv.getNotasMaterias())
'''

#GET subject for AlumnoID
@app.route('/materias/<int:id>', methods=['GET'])
def findNotasMateriasByAlumnoID(id):      
        return (serv.findNotasMateriasByAlumnoID(str(id)))

# Delete subject by notameriaID
@app.route('/materia/<int:id>', methods=['DELETE'])
def deleteNotaMateria(id):
        return (serv.deleteNotaMateria(id))

''''*** FIN Agregar notaMateria *** '''

@app.route("/test")
def imprimirJson():
    return 'yes base de datos'

@app.route("/metodo")
def metodo():
    return 'yes metodo2'

@app.route("/TestapiExterna")
def testApiExterna():
    url='https://api.met.no/weatherapi/airqualityforecast/0.1/aqi_description'
    responsefer=requests.get(url)
    return (responsefer.content)
    #return "Api taller VI!"


@app.errorhandler(ApiExceptionServ)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

if __name__ == '__main__':
    app.run(debug=False)

