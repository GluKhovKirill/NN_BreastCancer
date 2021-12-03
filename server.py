from flask import Flask, request
import pickle, json
import numpy as np


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        X = json.loads(request.form['X_rows'])
        pred = [int(i) for i in MODEL.predict(X)]
        print()
        return json.dumps(pred)
    return 'Please use POST method', 423

if __name__ == '__main__':
    with open('model.pckl', 'rb') as file:
        MODEL = pickle.loads(file.read())
    app.run(host='0.0.0.0', port='4862')