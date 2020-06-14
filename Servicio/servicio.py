from Modelo.model_notasMaterias import NotaMateria
from flask import jsonify
import json
from controller import Response
from flask_api import FlaskAPI, status
from Servicio.Exception_api import *
import requests
from Servicio.Internal_errors import CodeInternalError


#add notaMateria
def addNotaMateria(request): 
    notamateria=setNotaMateria(request)
    try:
        notamateria.save()
        content = {'detalle': 'Recurso creado.'}
        return content, status.HTTP_201_CREATED 
    except Exception as identifier:
        raise InternalServerError('Error relacionado con base de datos.', CodeInternalError.ERROR_INTERNAL_11_CONEXION_BD)       
    
    
    '''return "Materia agregarda. id={}".format(notamateria.notamateria_id)'''

#get
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
            

# Get all NotasMaterias
def getNotasMaterias():
    #materias=NotaMateria.buscarNotasMaterias()
    #json_Str=jsonify([e.serializar() for e in materias]) 
    #return json_Str
    page=NotaMateria.buscarNotasMaterias()
    final_list = []
    for element in page:
        final_list.append(element)
    return jsonify(final_list), status_code

    

#Update
def updateNotaMateria(request): 
    try:
        notamateriaID=request.json['notamateria_id']
        nombremateria=request.json['nombremateria']
        notafinal=request.json['notafinal']
        alumnoID=request.json['alumno_id']
    except Exception as identifier:
        raise BadResquest('Estructa de Json incorrecta',CodeInternalError.ERROR_INTERNAL_10_JSON_BAD_FORMED) 
    #se valida el nro de la nota
    if (int(notafinal)>=11 or int(notafinal)<0):
            raise BadResquest('Nota invalida',CodeInternalError.ERROR_INTERNAL_10_JSON_BAD_FORMED)
        #Se valida si la notamateriaID recibida corresponde al alumno en cuestión. Valida si el user no existe.
    notamateria=NotaMateria.buscarNotaMateriaByNotamateriaID(notamateriaID)
    if notamateria is None:
        raise BadResquest('Los datos recibidos no coinciden.',CodeInternalError.ERROR_INTERNAL_13_REQUEST_DATA_NOT_MATCHED)
    if (int(alumnoID)==int(notamateria.alumno_fk)):
        try:
            notamateria.nombremateria=nombremateria
            notamateria.notafinal=notafinal
            '''print(notamateria.nombremateria)
            print(notamateria.notafinal)
            print(notamateria.alumno_fk)
            print(notamateria.notamateria_id)'''
            notamateria.save()
            return ('Recurso actualizado.')
        except Exception as identifier:
            raise InternalServerError('Error relacionado con base de datos.', CodeInternalError.ERROR_INTERNAL_11_CONEXION_BD)       
    else:
        raise BadResquest('Los datos recibidos no coinciden.',CodeInternalError.ERROR_INTERNAL_13_REQUEST_DATA_NOT_MATCHED) 
        
    
# Update
def updateNotaMateriasByAlumnoID(id):
    try:      
        obj=NotaMateria.buscarMateriasByAlumnoID(id)
        json_str=jsonify([e.serializar() for e in obj])
        return (json_str)
    except Exception as e:
	    return(str(e))
 
#
def deleteNotaMateria(id):
    try:
        notamateria=NotaMateria.buscarNotaMateriaByNotamateriaID(id)
    except Exception as identifier:
        raise InternalServerError('Error relacionado con base de datos.', CodeInternalError.ERROR_INTERNAL_11_CONEXION_BD)          
    if notamateria is not None:
        try:
            notamateria.delete()
            return ('Recurso eliminado.',status.HTTP_200_OK)
        except Exception as identifier:
            raise InternalServerError('Error relacionado con base de datos.', CodeInternalError.ERROR_INTERNAL_11_CONEXION_BD)   
    else:
        raise BadResquest('Recurso no encontrado en la base de datos.',CodeInternalError.ERROR_INTERNAL_12_REQUEST_NOT_FOUND)  
     

#Methods
def setNotaMateria(request):
    try:   
        notamateria=NotaMateria(
            request.json['alumno_id'],
            request.json['nombremateria'],
            request.json['notafinal'] 
        )
    except Exception as identifier:
        raise BadResquest('Estructa de Json incorrecta',CodeInternalError.ERROR_INTERNAL_10_JSON_BAD_FORMED)
    return notamateria
       

       
#def setMessajeFormatJson():
#    return ({'detail':'Estructura json no soportada'},status.HTTP_400_BAD_REQUEST)
#

def imprimirJson():
    notamateria = NotaMateria('11','estadistica','10') 
    json_data = json.dumps(notamateria) 
    print (json_data)
    return (json_data)





