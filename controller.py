
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

#app.config.from_object(os.environ['APP_SETTINGS'])
#app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:Ingreso871@localhost/Irso"
#app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://rmnyfgzfbjbygy:4843aa6bd5f1683b39b934750c6b4475b311e244179a3ca4033fff37896029c4@ec2-34-232-147-86.compute-1.amazonaws.com/da384a5ispvhh0"
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.config.from_object(config[env_name])


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
    variable_test= os.environ.get('HOME')
    print(os.getcwd())
    print(variable_test)
    return 'yes base de datos'

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

