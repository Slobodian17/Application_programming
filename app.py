from flask import Flask
from wsgiref.simple_server import make_server
from waitress import serve
from blueprint import api_blueprint
from flask_sqlalchemy import SQLAlchemy
from config import SQLALCHEMY_DATABASE_URI
from flask_migrate import Migrate

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import *

with make_server('', 5000, app) as server:
    app.register_blueprint(api_blueprint, url_prefix="/api/v1")
    server.serve_forever()

if __name__ == "__main__":
    serve(app, listen='localhost:5000')

# curl -v -XGET http://localhost:5000/api/v1/hello-world-10
