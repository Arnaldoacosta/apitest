from flask import Flask
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy

def create_app():
    app = Flask(__name__)
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

@app.route('/metodo2', methods=['GET'])
def get_metodo2():
    response = {'message': 'probando2'}
    return jsonify(response)


@app.route("/test2")
def imprimirJson():
    return 'yes base de datos'


if __name__ == '__main__':
    app.run(debug=True)