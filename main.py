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


'''@app.route('/test', methods=['GET'])
def get_users():
    response = {'message': 'Api irso'}
    return jsonify(response)'''

#  Add subject
@app.route('/alumnos/materias', methods=['POST'])
def addNotaMateria(): 
    return (servicio.addNotaMateria(request))
#region get

#GET subject for AlumnoID y materia ID
@app.route('/alumnos/<int:alumnoid>/materias/<int:materiaid>', methods=['GET'])
def getNotasMateriasByAlumnoIDToMateriaID(alumnoid,materiaid):      
    return (servicio.getNotasMateriasToAlumnoIDbyNotaMateriaID(alumnoid,materiaid))

#Get all notamaterias para un alumnoID
@app.route('/alumnos/<int:alumnoid>/materias', methods=['GET'])
def getNotasMateriasByAlumnoID(alumnoid):   
    return (servicio.getNotasMateriasByAlumnoID(alumnoid))

#endregion 

# Delete subject by notameriaID
@app.route('/alumnos/<int:alumnoid>/materias/<int:notamateriaid>', methods=['DELETE'])
def deleteNotaMateria(alumnoid,notamateriaid):
    return (servicio.deleteNotaMateria(alumnoid,notamateriaid))

# Update subject               
@app.route('/materia', methods=['PATCH'])
def updateNotaMateria():
    return (servicio.updateNotaMateria(request))


#Get all ---(Se usará en una posible futuro si crece la aplicacion)
@app.route('/materias', methods=['GET'])
def getNotasMaterias():  
    return (servicio.getNotasMaterias())

@app.errorhandler(ApiExceptionServ)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


if __name__ == '__main__':
    app.run(debug=True)