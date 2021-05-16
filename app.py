from flask import Flask
from routes.request_handler import configure_handler

app = Flask(__name__)

configure_handler(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
