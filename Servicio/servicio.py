from Modelo.model_notasMaterias import NotaMateria
from flask import jsonify
import json
from main import Response
from flask_api import FlaskAPI, status
from Servicio.Exception_api import *
import requests
from Servicio.Internal_errors import CodeInternalError



def findNotasMateriasByAlumnoID(id):
    try:
        obj=NotaMateria.getNotasMateriasByAlumnoID(id)
    except Exception as identifier:
        raise InternalServerError('Error relacionado con base de datos.', CodeInternalError.ERROR_INTERNAL_11_CONEXION_BD)          
    if obj is not None and len(obj)!=0:
        json_Str=jsonify([e.serializar() for e in obj]) 
        return json_Str
    else:
        raise BadResquest('Recurso no encontrado en la base de datos.',CodeInternalError.ERROR_INTERNAL_12_REQUEST_NOT_FOUND)
            
       






