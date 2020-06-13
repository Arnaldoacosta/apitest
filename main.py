from flask import Flask
from flask import jsonify

def create_app():
    app = Flask(__name__)
    return app

app = create_app()

@app.route('/test', methods=['GET'])
def get_users():
    response = {'message': 'probando'}
    return jsonify(response)

@app.route('/metodo', methods=['GET'])
def get_metodo():
    response = {'message': 'probando2'}
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)