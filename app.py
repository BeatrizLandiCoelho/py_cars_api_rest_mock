# python -m venv venv
from flask import Flask,jsonify
from mock import Carros

app = Flask(__name__)

@app.route('/carros', methods=['GET'])
def get_carros():
    return Carros

if __name__ == '__main__':

    print("server read to go")
    app.run(debug=True, port=8080)