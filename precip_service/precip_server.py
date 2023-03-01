import random
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def get_precipitation():

    return {
        'precip_chance': 12,
        'type': 12
    }



if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5002')