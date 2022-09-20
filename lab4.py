from flask import Flask
from wsgiref.simple_server import make_server

from waitress import serve

from blueprint import api_blueprint

app = Flask(__name__)
with make_server('', 5000, app) as server:
    app.register_blueprint(api_blueprint, url_prefix="/api/v1")
    server.serve_forever()

if __name__ == "__main__":
    serve(app, listen='localhost:5000')

# curl -v -XGET http://localhost:5000/api/v1/hello-world-10
