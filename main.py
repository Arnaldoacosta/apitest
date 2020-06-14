
from flask import Flask, request, jsonify, Response
from flask_sqlalchemy import SQLAlchemy
import json
from flask_api import status
import requests
import os

#app = Flask(__name__)


def create_app():
    app = Flask(__name__)
    return app

app = create_app()


@app.route("/test")
def imprimirJson():
    return 'yes base de datos'

@app.route("/metodo")
def metodo():
    return 'yes metodo2'


if __name__ == '__main__':
    app.run(debug=False)

