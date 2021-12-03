from flask import Flask
import pickle


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    with open('model.pckl', 'rb') as file:
        MODEL = pickle.loads(file.read())
    app.run(host='0.0.0.0', port='4862')