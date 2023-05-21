
#python -m venv venv
#venv\Scripts\activate 
#pip install flask

from flask import Flask,jsonify, make_response, request
from mock import Carros

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route('/carros', methods=['GET'])
def get_carros():

    return make_response(

        jsonify(
        message='lista carros',
        data=Carros)
    )


@app.route('/carros', methods=['POST'])
def create_carro():
    carro = request.json
    Carros.append(carro)
    return  make_response(jsonify(carro)) 


if __name__ == '__main__':

    print("server read to go")
    app.run(port=8080)