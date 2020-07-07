from Modelo.model_notasMaterias import NotaMateria
from flask import jsonify
import json
from main import Response
from flask_api import FlaskAPI, status
from Servicio.Exception_api import *
import requests
from Servicio.Internal_errors import CodeInternalError
from Servicio.global_variable import ADD_NEW,UPDATE

#region add materia
def addNotaMateria(request): 
    notamateria=setNotaMateria(request,ADD_NEW)
    if (existsNombreMateriaToAlumnoID(notamateria.alumno_fk,notamateria.nombremateria)):
        raise Conflict('Existe una nota para esta materia', CodeInternalError.ERROR_INTERNAL_14_REQUEST_DATA_DUPLICATED)
    else:
        try:
            notamateria.save()
            content = {'detalle': 'Registro creado.'}
            return content, status.HTTP_201_CREATED 
        except Exception as identifier:
            raise InternalServerError('Error relacionado con base de datos', CodeInternalError.ERROR_INTERNAL_11_CONEXION_BD)              
#endregion 

#region get all notas manteria by ALUMNO ID
def getNotasMateriasByAlumnoID(alumnoid):
    if not(isNumber(alumnoid)):
        raise BadResquest('AlumnoID es un tipo invalido', CodeInternalError.ERROR_INTERNAL_13_REQUEST_DATA_NOT_MATCHED)
    try:
        obj=NotaMateria.getNotasMateriasByAlumnoID(alumnoid)
    except Exception as identifier:
        raise InternalServerError(identifier, CodeInternalError.ERROR_INTERNAL_11_CONEXION_BD)          
    if obj is not None and len(obj)!=0:
        json_Str=jsonify([e.serializar() for e in obj]) 
        return json_Str
    else:
        raise BadResquest('Recurso no encontrado.',CodeInternalError.ERROR_INTERNAL_12_REQUEST_NOT_FOUND)
#endregion

#region get one notamanteriaID to an AlumnoID
def getNotasMateriasToAlumnoIDbyNotaMateriaID(alumnoid,materiaid):
    if (not(isNumber(alumnoid))):
        raise BadResquest(identifier, CodeInternalError.ERROR_INTERNAL_13_REQUEST_DATA_NOT_MATCHED)
    elif (not(isNumber(materiaid))):
        raise BadResquest(identifier, CodeInternalError.ERROR_INTERNAL_13_REQUEST_DATA_NOT_MATCHED)
    try:
        obj=NotaMateria.getNotaMateriaNotamateriaIDToAlumnoID(materiaid,alumnoid)
    except Exception as identifier:
        raise InternalServerError('Error relacionado en base de datos', CodeInternalError.ERROR_INTERNAL_11_CONEXION_BD)          
    if obj is not None and len(obj)!=0:
        json_Str=jsonify([e.serializar() for e in obj]) 
        return json_Str
    else:
        raise BadResquest('Recurso no encontrado.',CodeInternalError.ERROR_INTERNAL_12_REQUEST_NOT_FOUND)
#endregion




#region Get all NotasMaterias
def getNotasMaterias():
    materias=NotaMateria.buscarNotasMaterias()
    json_Str=jsonify([e.serializar() for e in materias]) 
    return json_Str
    '''page=NotaMateria.buscarNotasMaterias()
    final_list = []
    for element in page:
       final_list.append(element)
    return jsonify(final_list), status_code'''
#endregion
    

#region Update notamateria
def updateNotaMateria(request): 
    try:
        notamateriaID=request.json['notamateria_id']
        nombremateria=request.json['nombremateria']
        notafinal=request.json['notafinal']
        alumnoID=request.json['alumno_id']
    except Exception as identifier:
        raise BadResquest('Estructa de Json incorrecta',CodeInternalError.ERROR_INTERNAL_10_JSON_BAD_FORMED) 
    #se valida el nro de la nota
    isValidNotaFinal(notafinal)
    #if (int(notafinal)>=11 or int(notafinal)<0):
    #        raise BadResquest('Nota invalida',CodeInternalError.ERROR_INTERNAL_10_JSON_BAD_FORMED)
        #Se valida si la notamateriaID recibida corresponde al alumno en cuestión. Valida si el user no existe.
    notamateria=NotaMateria.getNotaMateriaByNotamateriaID(notamateriaID)
    if notamateria is None:
        raise BadResquest('Los datos recibidos no coinciden.',CodeInternalError.ERROR_INTERNAL_13_REQUEST_DATA_NOT_MATCHED)
    if (int(alumnoID)==int(notamateria.alumno_fk)):
        try:
            notamateria.nombremateria=nombremateria
            notamateria.notafinal=notafinal
            notamateria.save()
            return ('Recurso actualizado.')
        except Exception as identifier:
            raise InternalServerError('Error relacionado con base de datos.', CodeInternalError.ERROR_INTERNAL_11_CONEXION_BD)       
    else:
        raise BadResquest('Los datos recibidos no coinciden.',CodeInternalError.ERROR_INTERNAL_13_REQUEST_DATA_NOT_MATCHED) 
#endregion    
    
#region Update notamateria byAlumnoID
def updateNotaMateriasByAlumnoID(id):
    try:      
        obj=NotaMateria.buscarMateriasByAlumnoID(id)
        json_str=jsonify([e.serializar() for e in obj])
        return (json_str)
    except Exception as e:
	    return(str(e))
#endregion 

#region delete notamaterias
def deleteNotaMateria(request):    
    notamateria_json=setNotaMateria(request,UPDATE)
    if (not(isNumber(notamateria_json.notamateria_id))):
        BadResquest('NotamateriaID es un tipo invalido', CodeInternalError.ERROR_INTERNAL_13_REQUEST_DATA_NOT_MATCHED)
    if (not(existsNotaMateriaIDToAlumnoID(notamateria_json.alumno_fk,notamateria_json.notamateria_id,notamateria_json.nombremateria))):
        raise BadResquest('No existe la materia para el alumno asociado', CodeInternalError.ERROR_INTERNAL_11_CONEXION_BD)
    try:
        notamateria_delete=NotaMateria.getNotaMateriaByNotamateriaID(notamateria_json.notamateria_id)
    except Exception as identifier:
        raise InternalServerError('Error relacionado con base de datos.', CodeInternalError.ERROR_INTERNAL_11_CONEXION_BD)          
    if notamateria_delete is not None:
        try:
            notamateria_delete.delete()
            return ('',status.HTTP_204_NO_CONTENT)
        except Exception as identifier:
            raise InternalServerError('Error relacionado con base de datos.', CodeInternalError.ERROR_INTERNAL_11_CONEXION_BD)   
    else:
        raise BadResquest('Recurso no encontrado.',CodeInternalError.ERROR_INTERNAL_12_REQUEST_NOT_FOUND)  
#endregion     

#region Common Methods
def setNotaMateria(request,action):
    try:  
        request.get_json()
    except Exception as identifier:
        raise BadResquest('Estructura de archivo invalida',CodeInternalError.ERROR_INTERNAL_10_JSON_BAD_FORMED)
    isValidDataType(request)
    isValidNotaFinal(request.json['notafinal']) 
    if (action):
        notamateria=NotaMateria(
            request.json['alumno_id'],
            request.json['nombremateria'],
            request.json['notafinal'],
            0,
            ADD_NEW
        )
    else:
        try:  
            notamateria=NotaMateria(
                request.json['alumno_id'],
                request.json['nombremateria'],
                request.json['notafinal'],
                request.json['notamateria_id'],
                UPDATE
            )
        except Exception as identifier:
            raise BadResquest('Estructura de archivo invalida',CodeInternalError.ERROR_INTERNAL_10_JSON_BAD_FORMED)
    return notamateria

def isValidDataType(request):
    if (str((request.json['nombremateria'])).isnumeric()):
        raise BadResquest('Nombre de materia no es un tipo de dato valido',CodeInternalError.ERROR_INTERNAL_13_REQUEST_DATA_NOT_MATCHED)
    elif (not(isNumber((request.json['notafinal'])))):
        raise BadResquest('Nota final no es un tipo de dato valido',CodeInternalError.ERROR_INTERNAL_13_REQUEST_DATA_NOT_MATCHED)
    elif (not(isNumber((request.json['alumno_id'])))):
        raise BadResquest('Alumno id no es un tipo de dato valido',CodeInternalError.ERROR_INTERNAL_13_REQUEST_DATA_NOT_MATCHED)


''' Valida que sea entero'''         
def isNumber(json_value):
    try:
        int(json_value)
        return True
    except:
        return False

def existsNotaMateriaIDToAlumnoID(alumnoid, notamateriaid,nombremateria):
    notamateria_comp=NotaMateria.getNotaMateriaToAlumnoIDByNotamateriaIDNombreMateria(notamateriaid,alumnoid,nombremateria)
    dir(notamateria_comp)
    if notamateria_comp is None:
        return False
    else:
        return True

def existsNombreMateriaToAlumnoID(alumnoid, nombremateria):
    notamateria_comp=NotaMateria.getNotaMateriaByNombreMateria(alumnoid,nombremateria)
    dir(notamateria_comp)
    if notamateria_comp is None:
        return False
    else:
        return True
#endregion    


#region bussiness rules
def isValidNotaFinal(notafinal):
    if (int(notafinal)>=11 or int(notafinal)<0):
        raise BadResquest('Nota invalida',CodeInternalError.ERROR_INTERNAL_13_REQUEST_DATA_NOT_MATCHED)
#endregion 




