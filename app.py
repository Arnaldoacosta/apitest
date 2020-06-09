
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
''''*** FIN Agregar notaMateria *** '''

app = Flask(__name__)



@app.route("/test")
def imprimirJson():
    return "Api taller VI!"



if __name__ == '__main__':
    app.run(debug=True)
