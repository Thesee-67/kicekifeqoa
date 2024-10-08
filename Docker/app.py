# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Bonjour, cette application est en cours de maintenance. délai de rétablissement établie au 22 décembre!' \
           'pile pour noël :)'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
