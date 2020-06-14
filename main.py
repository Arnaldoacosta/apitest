from flask import Flask, request, Response
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from Servicio import servicio
from config import Production
import requests
from Modelo.model_notasMaterias import db
from Servicio.Exception_api import ApiExceptionServ



def create_app():
    app = Flask(__name__) 
    app.config.from_object(Production)
    return app

app = create_app()
db.init_app(app)


@app.route('/test', methods=['GET'])
def get_users():
    response = {'message': 'Hola Elu :), como estas?. Odio phyton :( ...'}
    return jsonify(response)

#GET subject for AlumnoID
@app.route('/materias/<int:id>', methods=['GET'])
def findNotasMateriasByAlumnoID(id):      
        return (servicio.findNotasMateriasByAlumnoID(str(id)))

#  Add subject
@app.route('/materia', methods=['POST'])
def addNotaMateria():  
    return (servicio.addNotaMateria(request))

# Delete subject by notameriaID
@app.route('/materia/<int:id>', methods=['DELETE'])
def deleteNotaMateria(id):
        return (servicio.deleteNotaMateria(id))

# Update subject               
@app.route('/materia', methods=['PATCH'])
def updateNotaMateria():
    return (servicio.updateNotaMateria(request))


@app.errorhandler(ApiExceptionServ)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


if __name__ == '__main__':
    app.run(debug=True)